class Vehicle:
    licenseCode = "" 
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Air conditioner is turned on.")
class Car:
    licenseCode = "" 
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Air conditioner is turned on.")
class Pickup:
    licenseCode = "" 
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Air conditioner is turned on.")
class Van:
    licenseCode = "" 
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Air conditioner is turned on.")
pickup1 = Pickup()
pickup1.licenseCode = "1234"
pickup1.serialCode = "5678"
pickup1.turnOnAirConditioner()
