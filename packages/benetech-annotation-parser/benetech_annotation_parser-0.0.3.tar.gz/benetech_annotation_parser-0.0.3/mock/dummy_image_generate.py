from PIL import Image

# 001
width, height = 500, 500
green = (0, 255, 0)
image = Image.new("RGB", (width, height), green)
image.save("./dummy_data/images/dummy_001.jpg")

## 002
width, height = 600, 400
green = (0, 255, 0)
image = Image.new("RGB", (width, height), green)
image.save("./dummy_data/images/dummy_002.jpg")

## 003
width, height = 400, 600
green = (0, 255, 0)
image = Image.new("RGB", (width, height), green)
image.save("./dummy_data/images/dummy_003.jpg")
