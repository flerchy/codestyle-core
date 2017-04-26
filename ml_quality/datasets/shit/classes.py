class Enemy

life = 3

def attack(self):
    #self = use something from your own task
    print("ouch!")
    self.life -= 1
    #accesses variables inside class

def checklife(self):
    if self.life <= 0 :
        print("I am dead")
    else:
        print(str(self.life) + "life left")

## accessing your class by an object

enemy1 = Enemy()
enemy2 = Enemy()


enemy1.attack()
enemy1.checklife()
enemy1.attak()
enemy1.attack()
enemy2.checklife()
enemy1.attack()
