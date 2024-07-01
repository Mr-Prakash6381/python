class student:
    def __init__(self):
        print("--This is Non Parameterised Constructor-- \n")
    def show(self,name):
        self.name=name
        print(self.name)
s1=student()
s1.show("Prakash")
