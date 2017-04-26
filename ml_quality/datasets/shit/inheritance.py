class Parent():
    def printlastname(self):
        print("buckingham")

class Child(Parent):
    ###look for parent class, get all info, and pass it on to Child
    def printfirstname(self):
        print("cam")

        ##can override inheritance as wel
    ##def printlastname(self):
        ##print("Guerrero")

        cam = Child()
        cam.printfirstname
        cam.printlastname
