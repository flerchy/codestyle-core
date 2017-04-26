from PIL import Image

sister = Image.open("sister.png")
r,g,b = sister.split()

new_img = Image.merge('RGB', (g,r,b))

new_img.show()

bucky = Image.open('bucky.rpg')
r1,g1,b1 = sister.split()
r2,g2,b2 = bucky.split()

new_img1 = Image.merge('RGB', (r2,g1,b2))
new_img1.show()
