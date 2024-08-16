class vehicle:
    def start(self,brand):
        self.brand=brand
        print(self.brand,"Vehicle Started !")
class car(vehicle):
    def drive(self,model):
        self.model=model
        print(self.brand,self.model, "Car is being drive !")
class electric_car(car):
    def charge(self,capacity):
        self.battery_capacity=capacity
        print(self.brand,self.model,"Electric Car is Being charged.Bettery Capacitey" , self.battery_capacity)
objec=electric_car()
objec.start("Tesla")
objec.drive("Model 3")
objec.charge("75 Kwh")
        
