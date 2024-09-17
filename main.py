import random

class Student:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
studentList = [Student("Yousef"),Student("Khalid"),Student("Ahmad")]

def printStudents(stList):
    for st in stList:
        print(st.getName())

def createRandomStudents():
    newStList = []
    for i in range(10):
        newStList.append(Student("Student number " + str(random.randint(1, 10))))

    return newStList

printStudents(createRandomStudents())