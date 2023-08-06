from typing import Dict, List


def convert_to_xy(rectangle_coord: Dict[str, int]) -> List[int]:
    x0 = rectangle_coord["x0"]
    x1 = rectangle_coord["x1"]
    x2 = rectangle_coord["x2"]
    x3 = rectangle_coord["x3"]
    y0 = rectangle_coord["y0"]
    y1 = rectangle_coord["y1"]
    y2 = rectangle_coord["y2"]
    y3 = rectangle_coord["y3"]
    return [x0, y0, x1, y1, x2, y2, x3, y3]


def convert_to_icdar2015(polygon: List[Dict[str, int]], text: List[str]) -> List[str]:
    converted_polygons = [convert_to_xy(pl) for pl in polygon]
    formatted_results = []
    for polygon_line, text_line in zip(converted_polygons, text):
        result = ",".join([str(p) for p in polygon_line])
        result = ",".join([result, text_line])
        formatted_results.append(result)
    return formatted_results


def save_to_text(output_file_path: str, lines: List[str]):
    with open(file=output_file_path, mode="w") as f:
        for line in lines:
            f.write(line + "\n")
