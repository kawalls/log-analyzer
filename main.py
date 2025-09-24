import random

class Address(): 
    def __init__(self):  
        self.oct1 = random.randint(0, 255)
        self.oct2 = random.randint(0, 255)
        self.oct3 = random.randint(0, 255)
        self.oct4 = random.randint(0, 255)   
    def __init__(self, oct1, oct2, oct3, oct4):
        self.oct1 = oct1
        self.oct2 = oct2
        self.oct3 = oct3
        self.oct4 = oct4   
        
    def getIP(self):
        return f'{self.oct1} . {self.oct2} . {self.oct3} . {self.oct4}'
    
thing = Address
thing2 = Address(192, 18, 233, 18)

ip_address = thing.getIP()
print(ip_address)