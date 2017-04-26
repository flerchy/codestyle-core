from PIL import Image

baby = Image.open('baby.png')
square_baby = baby.resize(250,250)
flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
rotate_baby = baby.transpose(Image.ROTATE_90)


baby.show()
square_baby.show()
flip_baby.show()
rotate_baby.show()
