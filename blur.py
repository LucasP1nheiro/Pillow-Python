from PIL import Image, ImageFilter

image1 = Image.open('paisagem.png')

image1.filter(ImageFilter.GaussianBlur(15)).save('paisagem.png')

