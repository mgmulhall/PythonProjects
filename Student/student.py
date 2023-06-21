#Maggie Mulhall
#This program creates a student class with Engineer and Doctor Subclasses
#Inheritance

#Main Student class
class Student:

    #Create student
    def __init__(self,name,age):
        self.name=str(name)
        self.age=str(age)

    #Display instance of Student
    def display(self):
        print("\nName: ",self.name)
        print("Age: ",self.age)

#Child Engineer class
class Engineer(Student):

    #Create Engineer, inheriting name and age from Student class
    def __init__(self,name,age,course):
        Student.__init__(self,name,age)
        self.course=course
    
    #Display instance of Engineer
    def displayEngineer(self):
        print("\nName: ",self.name)
        print("Age: ",self.age)
        print("Course: ",self.course)

#Child Doctor class
class Doctor(Student):
    #Create Doctor, inheriting name and age from Student class
    def __init__(self,name,age,hospital):
        Student.__init__(self,name,age)
        self.hospital=hospital
    
    #Display instance of Doctor
    def displayDoctor(self):
        print("\nName: ",self.name)
        print("Age: ",self.age)
        print("Hospital: ",self.hospital)

def main():
    #Create and display an Engineer
    Maggie=Engineer("Maggie",23,"Foundations")
    Maggie.displayEngineer()

    #Create and display a Doctor
    Sharon=Doctor("Sharon","23","MGH")
    Sharon.displayDoctor()

#Call main function
if __name__ == "__main__":
   main()