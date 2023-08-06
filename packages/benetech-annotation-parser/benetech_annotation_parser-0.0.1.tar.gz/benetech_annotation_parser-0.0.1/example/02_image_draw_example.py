import os
from typing import Dict
from PIL import Image, ImageDraw

from src.benetech_annotation_parser.annotation_api import AnnotationParser, Axis

def draw_rect_angle(img:Image.Image, rectangle_coord:Dict[str, int]):
    x0 = rectangle_coord['x0']
    y0 = rectangle_coord['y0']
    h = rectangle_coord['height']
    w = rectangle_coord['width']
    draw = ImageDraw.Draw(img)
    draw.rectangle([(x0, y0),(x0 + w, y0 + h)], outline="blue", width=0)


def draw_rect_angle_rotate(img:Image.Image, rectangle_coord:Dict[str,int], annotation_type:str):
    x0 = rectangle_coord['x0']
    x1 = rectangle_coord['x1']
    x2 = rectangle_coord['x2']
    x3 = rectangle_coord['x3']
    y0 = rectangle_coord['y0']
    y1 = rectangle_coord['y1']
    y2 = rectangle_coord['y2']
    y3 = rectangle_coord['y3']
    draw = ImageDraw.Draw(img)
    color = {"tick_label": (255, 0, 0), "chart_title": (0, 192, 192), "axis_title": (255, 255, 0)}[annotation_type]
    draw.line([x0, y0, x1, y1], fill=color, width=2)
    draw.line([x1, y1, x2, y2], fill=color, width=2)
    draw.line([x2, y2, x3, y3], fill=color, width=2)
    draw.line([x3, y3, x0, y0], fill=color, width=2)
    
def draw_point(img:Image.Image, coord:Dict[str, int]):
    draw = ImageDraw.Draw(img)
    draw.ellipse([(coord['x'] - 1 , coord['y']-1), (coord['x']+1, coord['y']+1)], fill="lime", outline="lime", width=10)
    
if __name__ == "__main__":
    # bentech data path (i.e. /mnt/data/train/)
    # The demo is available on a Kaggle notebook(link). 
    # Please refer to the Kaggle notebook for more details.
    data_path = 'mock/dummy_data'
    index = 0

    annotation_parser = AnnotationParser(data_path)
    ap= annotation_parser.get_annotation(index=0)
    img = Image.open(ap.image_path)

    draw_rect_angle(img, rectangle_coord=ap.plot_bb)

    polygon = ap.text(filter="polygon")
    role = ap.text(filter="role")
    for pg, rl in zip(polygon, role):
        draw_rect_angle_rotate(img=img, rectangle_coord=pg,annotation_type=rl)

    ticks_x = ap.ticks(axis=Axis.X, filter="tick_pt")
    ticks_y = ap.ticks(axis=Axis.Y, filter="tick_pt")

    for tick_x in ticks_x:
        draw_point(img, tick_x)
    for tick_y in ticks_y:
        draw_point(img, tick_y)

    img.save("sample1.png")

