import json, copy
import numpy as np
from tqdm import tqdm

from mmengine.registry import DATASETS
from torch.utils.data import Dataset
from typing import List, Union, Callable

from mmengine.dataset.base_dataset import Compose
from multiprocessing import Pool


@DATASETS.register_module()
class EngineCocoExt(Dataset):
    def __init__(self,
                 data_path: str,
                 raster_dir_path: str,
                 vector_dir_path: str,
                 split: str = "train",
                 class_title: str = None,
                 slice: bool = False,
                 window: tuple = None,
                 stride: tuple = None,
                 pipeline: List[Union[dict, Callable]] = [],
                 max_refetch: int = 1000,
                 ignore_index: int = 255,
                 reduce_zero_label: bool = False):
        self.raster_data_path = f"{data_path}/{raster_dir_path}"
        self.vector_data_path = f"{data_path}/{vector_dir_path}"

        self.split = split
        self.slice = slice 
        self.window = window 
        self.stride = stride
        self.class_title = class_title
        self.ignore_index = ignore_index
        self.reduce_zero_label = reduce_zero_label

        self.pipeline = Compose(pipeline)
        self.max_refetch = max_refetch

        self.get_data_list()
    
    def full_init(self):
        self.get_data_info

    def load_vector_file(self, vec_path):
        vec_map = json.load(open(vec_path))

        file_name = vec_map["images"][0]["file_name"].split("/")[-1]
        file_path = f"{self.raster_data_path}/{file_name}"

        img_map = {
            "img_path": file_path,
            "img_id": vec_map["info"]["id"],
            "height": vec_map["images"][0]["height"],
            "width": vec_map["images"][0]["width"],
            "instances": [],
            "seg_fields": [],
            "reduce_zero_label": self.reduce_zero_label
        }

        for annotation in vec_map["annotations"]:
            try:
                xmin, ymin, width, height = annotation["bbox"]
                xmax,ymax = xmin+width, ymin+height
                bbox = [xmin, ymin, xmax, ymax]
                
                bbox_label = annotation["properties"][self.class_title_idx]["labels"][0]

                assert bbox_label in range(len(self._metainfo["classes"]))
                
                mask = [annotation["segmentation"][0][:-2]]

                ann_map = {
                    "bbox": bbox,
                    "bbox_label": bbox_label,
                    "mask": mask,
                    "ignore_flag": 0,
                    "extra_anns": []
                }

                img_map["instances"] += [ann_map]
            except:
                continue

        return img_map


    def get_data_list(self):
        meta_path = f"{self.vector_data_path}/metadata.json"
        metadata = json.load(open(meta_path, "r"))

        if not self.class_title:
            self.CLASSES = metadata["label:metadata"][0]["options"]
            self.class_title = metadata["label:metadata"][0]["title"].replace(" ", "-").lower()
            self.class_title_idx = 0
        else:
            for idx, question in enumerate(metadata["label:metadata"]):
                if question["title"] == self.class_title:
                    self.CLASSES = question["options"]
                    self.class_title = self.class_title.replace(" ", "-").lower()
                    self.class_title_idx = idx 

        self._metainfo = {
            "title": metadata["title"],
            "description": metadata["description"],
            "tags": metadata["tags"],
            "problemType": metadata["problemType"] if "problemType" in metadata else None,
            "question_title": metadata["label:metadata"][self.class_title_idx]["title"],
            "question_description": metadata["label:metadata"][self.class_title_idx]["description"],
            "classes": metadata["label:metadata"][self.class_title_idx]["options"],
            "reduce_zero_label": self.reduce_zero_label
        }

        vec_path_list = [f"{self.vector_data_path}/{vec_file}" for vec_file in metadata["dataset"][self.split]]

        pool = Pool(16)
        self.data_list = list(tqdm(pool.imap(self.load_vector_file, vec_path_list), total=len(vec_path_list)))
        pool.close()

    @property
    def metainfo(self) -> dict:
        """Get meta information of dataset.

        Returns:
            dict: meta information collected from ``BaseDataset.METAINFO``,
            annotation file and metainfo argument during instantiation.
        """
        return copy.deepcopy(self._metainfo)
    
    def get_data_info(self, idx: int):
        data = self.data_list[idx]
        data["sample_idx"] = idx

        return data
    
    def prepare_data(self, idx: int):
        data = self.get_data_info(idx)
        data['dataset'] = self
        return self.pipeline(data)

    def _rand_another(self):
        return np.random.randint(0, len(self))

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, idx: int):
        if self.split == "test":
            data = self.prepare_data(idx)
            if not data:
                raise Exception('Test time pipline should not get `None` data_sample')

        for _ in range(self.max_refetch+1):
            data = self.prepare_data(idx)
            if not data:
                idx = self._rand_another()
                continue

            return data
