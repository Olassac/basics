class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
#Create a method
    def greeter(self):
        print("Good morning",self.name)
Student1 = Person("Bayo",16)
#Acessing the Student1
print(Student1.name)
print(Student1.age)
Student1.greeter()

class Temperature:
    def __init__(self,celcius,farenheit):
        self.celcius = celcius
        self.farenheit = farenheit
    def far2cel(self):
        result = ((5*self.farenheit)-160)/9
        print(self.farenheit, "to celcius is",result)
    def cel2far(self):
        result = ((self.celcius*9)+160)/5
        print(self.celcius,"to farenheit is",result)
temp = Temperature(60,45)
temp.cel2far()
temp.far2cel()


#User Friendly
print("""
Enter 1 : Celcius to Farenheit
Enter 2 : Farenheit to Celcius
""")
choice = int(input())
if choice == 1:
    print("Enter your celcius value")
    celval = float(input())
    condition1 = Temperature(celval,0)
    condition1.cel2far()
elif choice ==2:
    print("Enter your farenheit value")
    farval = float(input())
    condition2 = Temperature(0,farval)
    condition2.far2cel()
else:
    print("Wrong Value")