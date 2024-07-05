class student:
    def __init__(self,name):
        print("This is Parametrized Constructor--")
        self.name=name
    def show(self):
        print("Hello",self.name)
s1=student("Prakash")
s1.show()
