


from PIL import Image
import os
import sk
import size

direction = input("Выберите направление склейки (1-вертикальное/2-горизонтальное):")

if direction == "1":
    
    path = input("Укажите путь к первому изображению:")

    path2 = input("Укажите путь к второму изображению:")

    img = size.siz(path, path2)
    
    sk.glue(img[0], img[1], direction)

    print("Изображения успешно склеены")

elif direction == "2":

    path = input("Укажите путь к первому изображению:")

    path2 = input("Укажите путь к второму изображению:")

    img = size.siz(path, path2)

    sk.glue(img[0], img[1], direction)

    print("Изображения успешно склеены")


