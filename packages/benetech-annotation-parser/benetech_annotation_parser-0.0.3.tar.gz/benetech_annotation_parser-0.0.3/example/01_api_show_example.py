from benetech_annotation_parser.annotation_api import AnnotationParser, Axis

annotation_parser = AnnotationParser("mock/dummy_data")

# (0) "Extract one JSON data from a list of JSON file paths."
p = annotation_parser.get_annotation(0)
"""
print(p.name)
#>>> "dummy_001"
print(p.json_path)
#>>> "mock/dummy_data/annotations/dummy_001.json"
print(p.image_path)
#>>> "mock/dummy_data/images/dummy_001.jpg"
"""

# (1) source Literal["generated", "extracted"]
print(p.source)
"""
>>> p.source
'generated'
"""
# (2) chart-type Literal["dot", "horaizontal_bar", "vertical_bar", "line", "scatter"]
print(p.chart_type)
"""
>>> p.chart_type
'vertical_bar'
"""
# (3) plot-bb
print(p.plot_bb)
"""
>>> p.plot_bb
{'height': 150, 'width': 150, 'x0': 50, 'y0': 50}
"""
# (4) text
print(p.text())
"""
>>> p.text()
[
{'id': 0, 'polygon': {'x0': 10, 'x1': 10, 'x2': 10, 'x3': 10, 'y0': 10, 'y1': 10, 'y2': 10, 'y3': 10}, 'text': 'Dummy_title', 'role': 'chart_title'}, 
{'id': 1, 'polygon': {'x0': 20, 'x1': 20, 'x2': 20, 'x3': 20, 'y0': 20, 'y1': 20, 'y2': 20, 'y3': 20}, 'text': 'Dummy_title', 'role': 'axis_title'}, 
{'id': 2, 'polygon': {'x0': 30, 'x1': 30, 'x2': 30, 'x3': 30, 'y0': 30, 'y1': 30, 'y2': 30, 'y3': 30}, 'text': 'Dummy_title2', 'role': 'axis_title'}, 
{'id': 3, 'polygon': {'x0': 30, 'x1': 30, 'x2': 30, 'x3': 30, 'y0': 30, 'y1': 30, 'y2': 30, 'y3': 30}, 'text': '10', 'role': 'tick_label'}, 
{'id': 5, 'polygon': {'x0': 40, 'x1': 40, 'x2': 40, 'x3': 40, 'y0': 40, 'y1': 40, 'y2': 40, 'y3': 40}, 'text': '20', 'role': 'tick_label'}, 
{'id': 6, 'polygon': {'x0': 50, 'x1': 50, 'x2': 50, 'x3': 50, 'y0': 50, 'y1': 50, 'y2': 50, 'y3': 50}, 'text': 'dummy_country1', 'role': 'tick_label'}, 
{'id': 7, 'polygon': {'x0': 60, 'x1': 60, 'x2': 60, 'x3': 60, 'y0': 60, 'y1': 60, 'y2': 60, 'y3': 60}, 'text': 'dummy_country2', 'role': 'tick_label'}
]
"""
## (4-1) text/id
print(p.text(filter="id"))
"""
>>> p.text(filter='id')
[0, 1, 2, 3, 5, 6, 7]
"""
## (4-2) text/polygon
print(p.text(filter="polygon"))
"""
>>> p.text(filter='polygon')
[
    {'x0': 10, 'x1': 10, 'x2': 10, 'x3': 10, 'y0': 10, 'y1': 10, 'y2': 10, 'y3': 10}, 
    {'x0': 20, 'x1': 20, 'x2': 20, 'x3': 20, 'y0': 20, 'y1': 20, 'y2': 20, 'y3': 20}, 
    {'x0': 30, 'x1': 30, 'x2': 30, 'x3': 30, 'y0': 30, 'y1': 30, 'y2': 30, 'y3': 30}, 
    {'x0': 30, 'x1': 30, 'x2': 30, 'x3': 30, 'y0': 30, 'y1': 30, 'y2': 30, 'y3': 30}, 
    {'x0': 40, 'x1': 40, 'x2': 40, 'x3': 40, 'y0': 40, 'y1': 40, 'y2': 40, 'y3': 40}, 
    {'x0': 50, 'x1': 50, 'x2': 50, 'x3': 50, 'y0': 50, 'y1': 50, 'y2': 50, 'y3': 50}, 
    {'x0': 60, 'x1': 60, 'x2': 60, 'x3': 60, 'y0': 60, 'y1': 60, 'y2': 60, 'y3': 60}
]
"""
## (4-3) text/text
print(p.text(filter="text"))
"""
>>> p.text(filter='text')
['Dummy_title', 'Dummy_title', 'Dummy_title2', '10', '20', 'dummy_country1', 'dummy_country2']
"""
## (4-4) text/role
print(p.text(filter="role"))

"""
>>> p.text(filter='role')
['chart_title', 'axis_title', 'axis_title', 'tick_label', 'tick_label', 'tick_label', 'tick_label']
"""


# (5) axes
print(p.axes)
"""
>>> p.axes
{
    'x-axis': {'ticks': [{'id': 6, 'tick_pt': {'x': 40, 'y': 50}}, {'id': 7, 'tick_pt': {'x': 50, 'y': 60}}], 'tick-type': 'markers', 'values-type': 'categorical'}, 
    'y-axis': {'ticks': [{'id': 3, 'tick_pt': {'x': 55, 'y': 65}}, {'id': 4, 'tick_pt': {'x': 65, 'y': 75}}], 'tick-type': 'markers', 'values-type': 'numerical'}
}
"""
## (5-1) axes/{x|y}-axis
### (5-1-x) axes/x-axis
print(p.axis(axis=Axis.X))
"""
>>> p.axis(Axis.X)
{'ticks': [{'id': 6, 'tick_pt': {'x': 40, 'y': 50}}, {'id': 7, 'tick_pt': {'x': 50, 'y': 60}}], 'tick-type': 'markers', 'values-type': 'categorical'}
"""
### (5-1-y) axes/y-axis
print(p.axis(axis=Axis.Y))
"""
>>> p.axis(axis=Axis.Y)
{'ticks': [{'id': 3, 'tick_pt': {'x': 55, 'y': 65}}, {'id': 4, 'tick_pt': {'x': 65, 'y': 75}}], 'tick-type': 'markers', 'values-type': 'numerical'}
"""
## (5-2) axes/{x|y}-axis/ticks
print(p.ticks(axis=Axis.X))
"""
>>> p.ticks(axis=Axis.X)
[{'id': 6, 'tick_pt': {'x': 40, 'y': 50}}, {'id': 7, 'tick_pt': {'x': 50, 'y': 60}}]
"""
### (5-2-1) axes/{x|y}-axis/ticks/id
print(p.ticks(axis=Axis.X, filter="id"))
"""
>>> p.ticks(axis=Axis.X, filter='id')
[6, 7]
"""
### (5-2-2) axes/{x|y}-axis/ticks/tick_pt
print(p.ticks(axis=Axis.X, filter="tick_pt"))
"""
>>> p.ticks(axis=Axis.X, filter='tick_pt')
[{'x': 40, 'y': 50}, {'x': 50, 'y': 60}]
"""
### (5-2-3) axes/{x|y}-axis/tick-type
print(p.tick_type(axis=Axis.X))
"""
>>> p.tick_type(axis=Axis.X)
markers
"""
### (5-2-4) axes/{x|y}-axis/values-type
print(p.values_type(axis=Axis.X))
"""
>>> p.values_type(axis=Axis.X)
"categorical"
"""
# (6) data-series/{x|y}
print(p.data_series())
"""
>>> p.data_series()
[{'x': 'dummy_country1', 'y': 15.66666}, {'x': 'dummy_country2', 'y': 5.555555}]
"""
## (6-x) data-series/x
print(p.data_series(filter="x"))
"""
>>> p.data_series(filter='x')
['dummy_country1', 'dummy_country2']
"""
## (6-y) data-series/y
print(p.data_series(filter="y"))
"""
>>> p.data_series(filter='y')
[15.66666, 5.555555]
"""
