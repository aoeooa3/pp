


from PIL import Image

def siz(path, path2):
     
     img = Image.open(path)

     img1 = Image.open(path2)

     img_size = img.resize((250, 90))

     img1_size = img1.resize((250, 90))

     return img_size, img1_size

     