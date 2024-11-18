from main import image1_path, image2_path

def resize_image(image_path, new_size):
    img = Image.open(image_path)
    img_size = img.resize((250, 90)) 

    img1_size = img1.resize((250, 90)) 

