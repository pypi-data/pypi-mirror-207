import base64
from PIL import Image
from io import BytesIO
import random


def Png2Svg(image_path, save_file_path, width=None, height=None):
    def png_image_to_base64(image_path):
        image = Image.open(image_path)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return "data:image/png;base64," + img_base64, image

    b, image = png_image_to_base64(image_path)
    w, h = image.width, image.height
    
    if width and height:
        w, h = width, height
    
    uniqueid = str(int(random.random() * 100000))
    
    pre = '<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" overflow="hidden"><image width="{}" height="{}" xlink:href="'.format(
        w, h, w, h)
    post = '" preserveAspectRatio="none" id="{}"></image></svg>'.format(uniqueid)
    content = pre + b + post

    # Open the file in write mode and save the content
    with open(save_file_path, "w") as file:
        file.write(content)
