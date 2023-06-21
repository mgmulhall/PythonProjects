#Maggie Mulhall
#This program will calculate the circumference, area and volume of a circle with a user inputted radius
#The user input is validated and will only accept numeric values

#Import libraries
from ast import While
import math

#Prompt for radius and validate that it is a float
while True:
    entered=input("Enter the radius: ")
    try:
        radius=float(entered)
        if radius<=0:
            print('Entry must be greater than zero. Please try again')
            continue
        else:
            break
    except:
        print("Entry must be a number. Please try again")
        continue

#Calculate circumference 
cir=2*(math.pi)*radius

#Calculate area
area=math.pi*(radius**2)

#Calculate volume
volume=(4/3)*math.pi*(radius**3)

#Display output rounded to 5 decimals 
print('The circumference of a circle with a radius of',radius,'is',round(cir, 5))
print('The area of a circle with a radius of',radius,'is',round(area, 5))
print('The volume of a circle with a radius of',radius,'is',round(volume, 5))
