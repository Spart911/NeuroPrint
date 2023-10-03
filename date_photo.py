from PIL import Image, ImageOps
import os
import numpy
path_to_origin = "image_ii/" 
output_folder = "res_image_ii/"
img_names = os.listdir(path_to_origin)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
def mirror(path_to_origin, img_name, output_folder):
    im = Image.open(path_to_origin + img_name)
    ImageOps.mirror(im).save(output_folder+"mirror"+img_name, "JPEG")
    
def rotate(path_to_origin, img_name, output_folder):
    im = Image.open(path_to_origin + img_name)
    im.rotate(250).save(output_folder+"rotate_"+img_name, "JPEG")

for img in img_names:
    rotate(path_to_origin, img, output_folder)
