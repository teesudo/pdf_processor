import codecs
import pyocr.builders

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

builder = pyocr.builders.TextBuilder()
with codecs.open("toto.txt", 'r', encoding='utf-8') as file_descriptor:
    txt = builder.read_file(file_descriptor)
    # txt is a Python string