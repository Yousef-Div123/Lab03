class Student:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
st1 = Student("Yousef")
print(st1.getName())

print("something")