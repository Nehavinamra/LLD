# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#remote: type:Bluetooth/Infrared, brand: Sony/LG/Panasonic, battery:AAA/AA,
#buttons: Power, Volume:HIGH/LOW, Channel: UP/DOWN, HOME, BACK, INPUT: USB/Bluetooth/HDMI, EXIT
class Remote:
    def __init__(self, typeofcommunication, brand, battery):
        self.typeofcommunication = typeofcommunication
        self.brand = brand
        self.battery = battery
        print("It supports " + str(typeofcommunication) + " communication")
        print("It is of brand " + str(brand))
        print("It has " + str(battery) +" batteries")
        
    def power(self, powerbutton):
        self.powerbutton = powerbutton
        self.currVolume = 15
        self.currChannel = 200
        if powerbutton == "ON":
            print("Power is ON")
            print("Current volume " + str(self.currVolume))
            print("Current Channel " + str(self.currChannel))
        elif powerbutton == "OFF":
                print("Power is OFF")
        else:
            print("Switch ON the power")
            
        
    def volume_up(self):
        if self.powerbutton == "ON":
            self.currVolume+=1
            print("New Volume "+ str(self.currVolume))
        else:
            print("Error, Power is OFF")
            
    def volume_down(self):
        if self.powerbutton == "ON":
            self.currVolume-=1
            print("New Volume "+ str(self.currVolume))
        else:
            print("Error, Power is OFF")
    
    def channel_up(self):
        if self.powerbutton == "ON":
            self.currChannel+=1
            print("New channel " + str(self.currChannel))
        else:
            print("Error, Power is OFF")
        
    def channel_down(self):
        if self.powerbutton == "ON":
            self.currChannel-=1
            print("New channel " + str(self.currChannel))
        else:
            print("Error, Power is OFF")
        
            
        
        
Remoteobj = Remote("infrared", "Sony", "AA")
Remoteobj.power("OFF")
Remoteobj.volume_up()
Remoteobj.power("ON")
Remoteobj.volume_down()
Remoteobj.volume_down()
Remoteobj.volume_up()
Remoteobj.channel_up()




