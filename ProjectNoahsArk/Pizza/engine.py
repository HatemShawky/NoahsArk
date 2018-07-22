import math
class Pizza:
    def __init__(self,radius=0,height=0,price=0):
        """ takes self and 3 attributes """
        self.radius=radius
        self.height=height
        self.price=price
        #print (f"{self.radius} , {self.height} , {self.price}")
        
    def getratio(self):
        """when invoked on self, returns the Volume:Price ratio as float"""
        #print (f"{self.radius} , {self.height} , {self.price}")
        self.Volume=(self.radius)*(self.radius)*(self.height)*(math.pi)
        #print (f"Volume: {self.Volume}")
        #print (f"price: {self.price}")
        self.VPratio = self.Volume/self.price
        #print (f"PVR: {self.VPratio}")
        return self.VPratio
    
    def __sub__(self,other):
        """ when invoking an <obj> - <obj> this returns float "Diff" which is the abs difference of the 2 VPratios"""
        selfVPratio=self.getratio()
        otherVPratio=other.getratio()
        return abs(selfVPratio-otherVPratio)

#Pizza1=Pizza(radius=1, height=2, price=3)

#Pizza2=Pizza(radius=4, height=5, price=6)
#Pizza1.getratio()
#Pizza2.getratio()
#diff=Pizza1-Pizza2

#print(Pizza1.getratio()),print(Pizza2.getratio()),print(diff)

"""test example:
p1r=2 p2r=5 Vol1=37.7   VPR2=67.32
p1h=3 p2h=6 Vol2=471.24 diff=57.89
p1p=4 p2p=7 VPR1=9.425  #2 better   
"""