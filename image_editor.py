import numpy as np
from PIL import Image, ImageFilter, ImageEnhance  # Добавлен импорт для ImageEnhance
import os
import cv2


def enhance_image(image):
    enhanced_image = ImageEnhance.Sharpness(image).enhance(5.0)
    # Увеличение разрешения с помощью библиотеки Pillow
    super_res_image = enhanced_image.resize((enhanced_image.width * 5, enhanced_image.height * 5), Image.BILINEAR)
    # Преобразование изображения в черно-белый формат
    bw_image = image.convert("L")
    edges = bw_image.filter(ImageFilter.FIND_EDGES)
    emboss = edges.filter(ImageFilter.EMBOSS)
    emboss.show()


    # Улучшение качества изображения с помощью библиотеки Pillow


    return super_res_image

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
Dimage_editor()