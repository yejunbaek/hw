import math

#asks for the raidus of the balloon
radius = int(input("what is the radius of your balloon? The price is $0.75/cm3: "))

#asks for how many ballons do they want to purchase
balloon = int(input("how many balloons do you want? Each balloon costs $0.45/cm2: "))

#finds the volume of the balloon
vsphere = int((4*math.pi*radius**3)/3)

#finds the surface area of the balloon
sasphere = int(4*math.pi*balloon**2)

#finds the price of the balloon
ballooncost = int((0.45*sasphere))
#displays the price of the balloons
print("the price of the balloons: $",ballooncost)

#finds the price of helium
heliumcost = int(0.75*vsphere)
#displays the price for the helium
print("the price of the helium is: $",heliumcost)

#payment for balloon and helium
payment = ballooncost+heliumcost

#adds tax
taxcost = int(payment*0.05)
finalcost = int(payment+taxcost)

#print the finalcost
print("Your final cost is:", finalcost,"\n \n")

#receipt
print("receipt")
print("cost for balloons: $",ballooncost)
print("cost for helium: $", heliumcost)
print("tax: 5%")
print("cost with tax: $", finalcost)