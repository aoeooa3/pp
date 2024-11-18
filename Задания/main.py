from PIL import Image

import size

import sk 

direction = input("Выберите направление склейки (вертикальное/горизонтальное): ")

if direction == "горизонтальное":
    
    image1_path = input("Введите путь к первому изображению: ")
    
    image2_path = input("Введите путь ко второму изображению: ")
    
    size.resize_image(image_path, new_size)
    
    sk.merge_images(image1_path, image2_path, direction)

else:

    image1_path = input("Введите путь к первому изображению: ")
    
    image2_path = input("Введите путь ко второму изображению: ")

    size.resize_image(image_path, new_size)
     
    sk.merge_images(image1_path, image2_path, direction)

sk.merge_images.show()

print("Изображения успешно склеены")     
