# Maggie Mulhall
#This program will calculate the perimeter and area of a rectangle with inputted dimensions
#Will calculate the volume of the related parallelepiped with inputted height

#Rectangle class
class Rectangle:
    
    #Initalize object
    def __init__(self,width,length):

        #Set length and width
        self.length=length
        self.width=width
    
    #Calculate perimeter
    def Perimeter(self):
        self.perimeter= 2*(self.length+self.width)
        return(self.perimeter)

    #Calculate area
    def Area(self):
        self.area=self.width*self.length
        return(self.area)

    #Display attributes to user
    def display(self):
        print("\nLength: ",self.length)
        print("Width: ",self.width)
        print("Perimeter: ",self.Perimeter())
        print("Area: ",self.Area())

#Child parallelepiped class (inherites from parent Rectangle class)
class Parallelepiped(Rectangle):

    #Initalize object
    #Get length and width from parent, set height
    def __init__(self,length,width,height):
        Rectangle.__init__(self,length,width)
        self.height=height

    #Calculate volume
    def Volume(self):
        self.vol=(self.height*self.width*self.length)
        return (self.vol)

#Verify user input is valid
def verify(input):
        if input.isdigit() and int(input) > 0:
            input=int(input)
            return input
        else: return -1 

#Main function
def main():
    print('\nPlease enter whole numbers only\n')
    #Ask for and verfiy width
    while True:
        w=input('Enter a width: ')
        w=verify(w)
        if w!=-1:
            break
        else: print("Invalid Entry, Try again!")

    #Ask for and verfiy length
    while True:   
        l=input('Enter a length: ')
        l=verify(l)
        if l!=-1:
            break
        else: print("Invalid Entry, Try again!")

    #Create rectangle
    myRec=Rectangle(w,l)
    myRec.display()

    #User input for parallelepiped
    while True:
        h=input('\nEnter a height: ')
        h=verify(h)
        if h!=-1:
            break
        else: print("Invalid Entry, Try again!")

    #Create parallelepiped
    myPara=Parallelepiped(l,w,h)
    print("Volume: ",myPara.Volume())

#Call main function
if __name__ == "__main__":
   main()


