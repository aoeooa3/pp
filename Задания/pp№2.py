n = input('Какая Вам нужна склейка, горизонтальная или вертикальная:')

if n == 'вертикальная' :
    
    from PIL import Image 
    
    img = Image.open("1811492764_328_0_2995_1500_1920x0_80_0_0_b03cf85d06b51a87722a4e2c47b7d94f.jpg")

    img1 = Image.open("4ad8747451b58d973017132cddbe75ce.jpg") 

    img.size 

    img1.size 

    img_size = img.resize((250, 90)) 

    img1_size = img1.resize((250, 90)) 

    img2 = Image.new("RGB", (250, 180)) 

    img2.paste(img_size, (0, 0)) 

    img2.paste(img1_size, (0, 90) )

    img2.show()

else:
    
    from PIL import Image 

    img = Image.open("1811492764_328_0_2995_1500_1920x0_80_0_0_b03cf85d06b51a87722a4e2c47b7d94f.jpg") 

    img1 = Image.open("4ad8747451b58d973017132cddbe75ce.jpg")

    img.size 

    img1.size 

    img_size = img.resize((250, 90)) 

    img1_size = img1.resize((250, 90)) 

    img2 = Image.new("RGB", (500, 90)) 

    img2.paste(img_size, (0, 0)) 

    img2.paste(img1_size, (250, 0)) 

    img2.show()


