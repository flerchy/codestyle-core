from PIL import Image

img = Image.open("bucky.jpeg")
#pillow object allows manipulation

print(img.size)
print(img.format)

img.show()
