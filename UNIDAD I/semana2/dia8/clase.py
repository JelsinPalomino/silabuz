from PIL import Image

im = Image.open("yo.jpg")
out = im.resize((128, 128))

out.show()
