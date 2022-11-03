from PIL import Image

image1 = Image.open('paisagem.png')
size = (700, 700)

image1.thumbnail(size)
image1.save('paisagem.png')

