from PIL import Image

sister = Image.open('sister.jpeg')
girl = Image.open('girl.png')

area = (100,100,300,300)
sister.paste(girl, area)

sister.show()
