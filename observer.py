#Parking lot displaying the status
#Observer: Screen, spots available for all types diff
#Subject: Parking lot

#parking lot: vehicle type, parking spot, parking level
#parking spot:  Large, Medium, Small

class Parkinglot:
    def __init__(self):
        self.largespots = 50
        self.mediumspots = 40
        self.smallspots = 10

    def entry_parkvehicle(self, vehicletype,parkinglevel):
        if vehicletype == "car":
            if self.mediumspots>0:
                self.mediumspots-=1
            else:
                print("No capacity for vehicle")
                
        elif vehicletype == "Two wheeler":
            
            if self.smallspots ==0:
                print("Sorry, Capacity full")
            else:
                self.smallspots -=1
                
        elif vehicletype == "heavy load":
            if self.largespots ==0:
                print("Sorry, Capacity full")
            else:
                self.largespots -=1

                
        else:
            print("Vehicle Not Allowed")
            
    def exit_parkvehicle(self,vehicletype):
        self.vehicletype = vehicletype
        
        if self.vehicletype == "car":
            if self.mediumspots<50:
                self.mediumspots +=1
            else:
                print("No more spots to add")
            

        elif self.vehicletype == "Two wheeler":
            if self.smallspots<10:
                self.smallspots+=1
            else:
                print("No more spots to add")
                
        elif self.vehicletype == "heavy load":
            if self.vehicletype<40:
                self.largespots +=1
            else:
                print("No more spots to add")
        else:
            print("Unrecognized Vehicle")
        

    def parkspot_counter(self):
        print("The total number of Large spots vacant:" + str(self.largespots))
        print("The total number of Medium spots vacant:" + str(self.mediumspots))
        print("The total number of Small spots vacant:" + str(self.smallspots))
        
class ParkingDisplay:
    def __init__(self):
              
    
Parkingobj = Parkinglot()
Parkingobj.entry_parkvehicle("car", "1")
Parkingobj.entry_parkvehicle("Two wheeler", "1")
Parkingobj.parkspot_counter()
Parkingobj.exit_parkvehicle("car")

