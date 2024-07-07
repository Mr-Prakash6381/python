class emp:
    def __init__(self,id,name):
        self.id=id
        self.name=name
e1=emp(102,'prakash')
print("Id= ",e1.id)
print("Name=",e1.name)
print("Id= ",e1.__id)
print("Name=",e1.__name)

