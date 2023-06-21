#Maggie Mulhall
#Manual build of a deque

#Initalizations
choice=0
item=0
list=[]

#Accept data and add to queue
class Make_deque:
    def __init__(myDeque,item,choice):
        #Set list, item and choice to object's instance
        myDeque.list = []
        myDeque.item=item
        myDeque.choice=choice

    def Add(myDeque,item,choice):
        myDeque.item=item
        myDeque.choice=choice

        #Add item to beginning  
        if myDeque.choice=="1":
            myDeque.list.insert(0,myDeque.item)
                                     
        #Add item to end
        elif myDeque.choice=="2":
            myDeque.list.append(myDeque.item)
        list=myDeque.list
        
        #Return list to display when needed
        return list

    #Prompt user for item to add to list
    def Prompt_Item(myDeque):
        myDeque.item=input("\nEnter another item: ")
        item=myDeque.item
        return item
    
    #Prompt user for where to add item to list
    def Prompt_Choice(myDeque):
        while True:
            myDeque.choice=input("Enter a 1 or 2: ")
            choice=myDeque.choice

            #Verify user enters a valid choice
            if choice=="1" or choice=="2":
                break
            else:
                print("Invalid choice, try again!")
        return choice

    #Display contents of the list in order
    def Display(myDeque):
        print("\nTo-Do List:")
        for i in myDeque.list:
            print(i)

#Main function
def main():
    print("\nLets Make a To-Do List!\nEnter a To-Do Item or 'EXIT' to quit")
    
    #Ask for initial input
    while True:
        item=input("Enter an Item: ")
        #Only exit if user inputs "EXIT"
        if item=="EXIT":
            break
        #Ask for initial item location to add to queue
        else:
            print("\nWhere in the list would you like to add this?\n Beginning: 1\n End: 2")
            while True:
                choice=input("\nEnter a 1 or 2: ")
                if choice=="1" or choice=="2":
                    break
                else:
                    print("Invalid choice, try again!")
            myDeque=Make_deque(item,choice)

            #Continuously add items to list until user exits out
            while True:
                myDeque.Add(item,choice)
                item=myDeque.Prompt_Item()
                if item=="EXIT":
                    break
                else:
                    choice=myDeque.Prompt_Choice()
            
            #Display List when user exits out
            myDeque.Display()
            break

#Call main function
if __name__ == "__main__":
   main()