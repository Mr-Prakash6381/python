class emp:
    def __int__(self,id,name):
        self.id=id;
        self.name=name;
    def disp(self):
        print("Id=",self.id);
        print("Name=",self.name);
e1=emp(101,"Santhos");
e2=emp(102,"Prakash");
e1.disp();
e2.disp();
