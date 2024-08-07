class animal:
    def disp_animal(self):
        self.name="cat"
        print("I am in Animal Class")
class dog(animal):
    def disp_dog(self):
        print(self.name)
        print("I am in Dog Class")

d1=dog()
d1.disp_animal()
d1.disp_dog()
