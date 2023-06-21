#Maggie Mulhall
#This program reads in data from "data.txt", sorts it, stores it in a linked list, and allows users to remove specific values

##!! BE SURE TO PUT DATA.TXT IN REFERENCEABLE PLACE!!
class Node:
    #Each node of list will be an instance of Node class
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    #Initalize object
    def __init__(self):
        self.head = None

    #When not found, add number to correct place
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        if current_node.value > value:
            new_node.next = current_node
            self.head = new_node
            return
        while (current_node.next is not None) and (current_node.next.value <= value):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    #When found, delete number
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current_node = self.head
        while (current_node.next.value != value) and (current_node.next is not None):
            current_node = current_node.next
        if current_node.next is None:
            return
        current_node.next = current_node.next.next

    #Create printable linked list
    def __str__(self):
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return ",".join(elements)

# Read the integers from the file
def processFile():
    
    #Open file and read numbers
    f = open("data.txt","r")
    numbers = [int(line.strip()) for line in f.readlines()]

    # Sort the list of integers
    numbers.sort()

    # Store the ordered elements in a linked list
    L = LinkedList()
    for num in numbers:
        L.insert(num)
    print(L)
    return L

def main():
    # Ask the user for an integer value x
    L=processFile()
    while True:
        try:
            print("Welcome, please enter a value! If it is in the list, we will delete it. If it is not, we will add it!")
            x = int(input("Enter an integer value: "))
            break
        except ValueError:
            print("Invalid Input. Try Again.")
            continue

    # Look for the position to insert x in L and remove x if it is already in L
    current_node = L.head
    while current_node is not None and current_node.value <= x:
        if current_node.value == x:
            print("Found it! Removing it!")
            L.delete(x)
            print(x,"has been removed from the list! Take a look:\n",L)
            exit()
        current_node = current_node.next
    
    # If X is not found, insert x in the appropriate position
    L.insert(x)
    print(x,"was not in the list... we added it! Take a look:\n",L)

if __name__ == "__main__":
    main()