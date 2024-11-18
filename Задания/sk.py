from PIL import Image

from size import resize_image

def merge_images(image1_path, image2_path, direction):
    image1 = img.resize((250, 90)) 
    image2 = img1.resize((250, 90)) 

    if direction == 'вертикальное':
        result_image = Image.new('RGB', (image1.size[0], image1.size[1] + image2.size[1]))  
        result_image.paste(image1, (0, 0))                                             
        result_image.paste(image2, (0, image1.size[1]))                               
    elif direction == 'горизонтальное':
        result_image = Image.new('RGB', (image1.size[0] + image2.size[0], image1.size[1])) 
        result_image.paste(image1, (0, 0))                                           
        result_image.paste(image2, (image1.size[0], 0))                              

    result_image.save('merged_image.jpg')  