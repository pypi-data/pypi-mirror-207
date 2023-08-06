import glob
import json
import os
from enum import Enum
from typing import Any, Dict, List, Literal, Optional


class Axis(Enum):
    X = "x-axis"
    Y = "y-axis"


class BentechFormatParser:
    def __init__(self, annotation_json: Dict[str, Any], json_file_path: str, image_file_path: str):
        self._annotation_json = annotation_json
        self._json_file_path = json_file_path
        self._image_file_path = image_file_path

    @property
    def name(self) -> str:
        return os.path.splitext(self._json_file_path)[0].split(os.sep)[-1]

    @property
    def json_path(self) -> str:
        return self._json_file_path

    @property
    def image_path(self) -> str:
        return self._image_file_path

    @property
    def source(self) -> Literal["generated", "extracted"]:
        return self._annotation_json["source"]

    @property
    def chart_type(self) -> Literal["dot", "horaizontal_bar", "vertical_bar", "line", "scatter"]:
        return self._annotation_json["chart-type"]

    @property
    def plot_bb(self) -> Dict[str, Any]:
        return self._annotation_json["plot-bb"]

    def text(self, filter: Optional[Literal["id", "polygon", "text", "role"]] = None):
        if filter is None:
            return self._annotation_json["text"]
        elif filter in ["id", "polygon", "text", "role"]:
            return self._filter_extract_key(self._annotation_json["text"], filter_key=filter)
        else:
            raise ValueError(f"Invalid filter: {filter}. Expected id, polygon, text or role")

    @property
    def axes(self):
        return self._annotation_json["axes"]

    def axis(self, axis: Axis = Axis.X):
        if axis == Axis.X or axis == Axis.X.value:
            return self._annotation_json["axes"]["x-axis"]
        elif axis == Axis.Y or axis == Axis.Y.value:
            return self._annotation_json["axes"]["y-axis"]
        else:
            raise ValueError(f"Invalid axis: {axis}. Expected Axis.X or Axis.Y.")

    def ticks(self, axis: Axis = Axis.X, filter: Optional[Literal["id", "tick_pt", "tick-type", "values-type"]] = None):
        axis_annotation = self.axis(axis)
        if filter is None:
            return axis_annotation["ticks"]
        elif filter in ["id", "tick_pt"]:
            return self._filter_extract_key(axis_annotation["ticks"], filter_key=filter)
        else:
            raise ValueError(f"Invalid filter: {filter}. Expected id, tick_pt, tick-type or values-type.")

    def tick_type(self, axis: Axis = Axis.X) -> str:
        axis_annotation = self.axis(axis)
        return axis_annotation["tick-type"]

    def values_type(self, axis: Axis = Axis.X) -> Literal["categorical", "numerical"]:
        axis_annotation = self.axis(axis)
        return axis_annotation["values-type"]

    def data_series(self, filter: Optional[Literal["x", "y"]] = None):
        if filter is None:
            return self._annotation_json["data-series"]
        elif filter in ["x", "y"]:
            return self._filter_extract_key(self._annotation_json["data-series"], filter_key=filter)
        else:
            raise ValueError(f"Invalid filter: {filter}. x, y.")

    @staticmethod
    def _filter_extract_key(dict_data: List[Dict[str, Any]], filter_key: str) -> List[Any]:
        extract_key_data = [d[filter_key] for d in dict_data if filter_key in d]
        return extract_key_data


class AnnotationParser:
    def __init__(self, root: str, images_path: str = "images", annotations_path: str = "annotations") -> None:
        self._root = root
        self._images_path = images_path
        self._annotations_path = annotations_path

        self._annotations = sorted(glob.glob(os.path.join(self._root, self._annotations_path, "*.json")))

        self._images = sorted(glob.glob(os.path.join(self._root, self._images_path, "*.jpg")))

    def __len__(self):
        return len(self._annotations)

    def _json_load(self, json_path: str, image_path: str) -> BentechFormatParser:
        with open(json_path, mode="r") as f:
            annotatation_json = json.load(f)
            parser_api = BentechFormatParser(
                annotation_json=annotatation_json, json_file_path=json_path, image_file_path=image_path
            )
        return parser_api

    def get_annotation(self, index: int):
        """
        # todo file_name_or_indx
        if isinstance(file_name_or_index, str):
            for anno_path in self._annotations:
                if file_name_or_index == anno_path:
                    return self._json_load(anno_path)
        """
        if isinstance(index, int):
            return self._json_load(self._annotations[index], self._images[index])
        else:
            raise TypeError((f"Invalid file_name_or_index type: {index.type}. expected type `int`"))
