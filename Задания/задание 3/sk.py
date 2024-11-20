


from PIL import Image


def glue(img_size, img1_size, direction):

     if direction == "1":

        img2 = Image.new("RGB", (500, 90))

        img2.paste(img_size, (0, 0))

        img2.paste(img1_size, (250, 0))

        img2.show()

        print("Склейка успешно завершена")
       
     elif direction == "2":

        img2 = Image.new("RGB", (500, 90))

        img2.paste(img_size, (0, 0))

        img2.paste(img1_size, (0, 90))

        img2.show()

        print("Склейка успешно завершена")



