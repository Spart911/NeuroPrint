import numpy as np
from PIL import Image, ImageFilter, ImageEnhance  # Добавлен импорт для ImageEnhance
import os
from ISR.models import RDN
import tensorflow as tf
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))

def enhance_image(image):
    lr_img = np.array(image)
    rdn = RDN(weights='psnr-small')
    sr_img = rdn.predict(lr_img)
    image_object = Image.fromarray(sr_img)

    lr1_img = np.array(image_object)
    rdn = RDN(weights='psnr-small')
    sr1_img = rdn.predict(lr1_img)
    image1_object = Image.fromarray(sr1_img)





    bw_image = image1_object.convert("L")
    emboss = bw_image.filter(ImageFilter.EMBOSS)




    return bw_image

def process_images(input_folder, output_folder):
    # Проверка наличия выходной папки и создание ее, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Получение списка файлов во входной папке
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        # Полный путь к текущему файлу
        input_path = os.path.join(input_folder, file_name)

        # Проверка, является ли текущий файл изображением
        if os.path.isfile(input_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Загрузка изображения с использованием библиотеки Pillow
            image = Image.open(input_path)

            # Обработка изображения
            enhanced_image = enhance_image(image)

            # Генерация пути для сохранения обработанного изображения
            output_path = os.path.join(output_folder, file_name)

            # Сохранение обработанного изображения
            enhanced_image.save(output_path)

            print(f"Обработано изображение: {file_name}")

    print("Процесс завершен.")
def Dimage_editor():
    # Укажите путь к входной папке с изображениями и путь к выходной папке
    input_folder = "CHB"
    output_folder = "res"

    # Вызов функции для обработки изображений
    process_images(input_folder, output_folder)