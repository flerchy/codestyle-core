class Mario():
    def move(self):
        print("im moving")

class Shroom():
    def eat_shroom(self):
        print("now im big")

class BigMario(Mario, Shroom):
    #inherits mario and Shroom
    pass
    ##pass passes an error

    cam = BigMario()
    cam.move()
    cam.eat_shroom()
