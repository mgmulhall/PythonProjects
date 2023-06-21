#Maggie Mulhall
#Removing People from Stack
#This program reads in a list of people from people.csv, stores them in a queue, and allows the user to removed the first X amount of people until the list is empty


#Imports and Initializations
from collections import deque
queue=deque()

#Person class to save people's information
class person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age  = age
    def getName(self):
        return self.name
    def getFullName(self):
        return self.name+" "+self.famN
    def getFamilyName(self):
        return self.famN
    def getAge(self):
        return self.age

#Read in info from the file
def readPeople(fileName):
    infile = open(fileName, "r")
    people = {}
    for line in infile:
        info = line.split(",")
        people.update({info[0]:person(info[1], info[2], int(info[3]))})
    return people

#Display all persons in person class
def printPeople(people):
    print("==========================")
    print(" Nickname  Name           ")
    print("==========================")
    for k in people.keys():
        print("{0:>9}  {1:<15}".format(k,people[k].getFullName()))
    print("==========================")

#Store nicknames in queue
def makeQueue(people):
    for k in people:
        person=k
        queue.append(person)
    #print("queue: ",queue)
    return queue

#Prompt for/validate user input
#Delete specified number of people from queue
def promptUser(queue):
    print("We are going to remove people from the begining of the queue.\nHow many would you like to remove?")
    while True:
        try:
            print("")
            num=int(input("Please enter a number 1-4: "))
            #Handle input out of range
            if num>4 or num<1:
                print("Value must be between 1 and 4, inclusive. Try Again.")
                continue
            
            #Remove people
            elif len(queue)>num:
                for i in range(num):
                    queue.popleft()
                print("")
                print(num,"name(s) removed\nFirst person in queue:",queue[0])
                continue
            
            #Handle input if requested removal number is greater than number of people left in queue
            elif len(queue)<num: 
                print("Not enough items in queue left, there are only ",len(queue),"name(s) left")
                continue
            
            #Exit when queue is empty
            else:
                print("All people have been removed... thanks for playing!")
                break
        
        #Handle non integer input
        except ValueError:
                print("Invalid Input. Try Again.")
                continue

#Main function
#Read in data, save data, display data, create queue of data, remove data
def main():
    fileName = "people.csv"
    everyone = readPeople(fileName)
    printPeople(everyone)
    queue=makeQueue(everyone)
    promptUser(queue)

#Call main function 
main()
