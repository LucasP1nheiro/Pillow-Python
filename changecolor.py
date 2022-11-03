from PIL import Image

image1 = Image.open('paisagem.png')

image1.convert(mode='L').save('paisagem.png')
