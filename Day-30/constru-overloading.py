class conover:
    def __init__(self,x=1,y=2):
        self.xx=x
        self.yy=y
    def disp(self):
        print("X Value=%d, Y Value=%d "%(self.xx,self.yy))
c1=conover(10)
c2=conover(20,30);
c1.disp()
c2.disp()
              
