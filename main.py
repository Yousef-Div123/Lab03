class Student:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
studentList = [Student("Yousef"),Student("Khalid"),Student("Ahmad")]

def printStudents():
    for st in studentList:
        print(st.getName())

printStudents()