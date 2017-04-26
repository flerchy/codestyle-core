from PIL import Image

sister = Image.open("sister.png")
r,g,b = sister.split()

r.show()
g.show()
b.show()
