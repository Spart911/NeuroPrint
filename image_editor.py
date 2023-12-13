import numpy as np
from PIL import Image, ImageFilter
import os
from ISR.models import RDN

def enhance_image(image, rdn):
    lr_img = np.array(image)
    sr_img = rdn.predict(lr_img)
    sr1_img = rdn.predict(sr_img)
    image_object = Image.fromarray(sr1_img)

    bw_image = image_object.convert("L")
    emboss = bw_image.filter(ImageFilter.EMBOSS)

    return bw_image

def process_images(input_folder, output_folder, max_image_size=(1024, 1024)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    rdn = RDN(weights='psnr-small')

    file_list = os.listdir(input_folder)

    for file_name in file_list:
        input_path = os.path.join(input_folder, file_name)

        if os.path.isfile(input_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image = Image.open(input_path)

            if image.size[0] > max_image_size[0] or image.size[1] > max_image_size[1]:
                image.thumbnail(max_image_size, Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else 3)  # Используйте 3, если нет ANTIALIAS


            enhanced_image = enhance_image(image, rdn)

            output_path = os.path.join(output_folder, file_name)
            enhanced_image.save(output_path)

            del enhanced_image
            image.close()

            print(f"Обработано изображение: {file_name}")

    print("Процесс завершен.")

def Dimage_editor():
    input_folder = "CHB"
    output_folder = "res"
    process_images(input_folder, output_folder)

Dimage_editor()