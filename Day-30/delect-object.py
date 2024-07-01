class emp:
    def disp(self):
        self.name="Prakash"
        self.age=21
        self.dgree="B.sc"
        print("Name=%s age=%d dgree=%s "%(self.name,self.age,self.dgree))
e1=emp()
e1.disp()
del e1
e1.disp()
