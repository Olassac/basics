def greetings():
    print("Good morning")


greetings()
def interest(P,T,R):
    result = P*T*R/100
    print(result)

interest(1000,2,50)

def simple(P,T,R,Name):
    result = P*T*R/100
    print(Name,"Interest","is",result)

simple(5000,4,70,"Adeniyi")
def vol(*vol):
    result = vol[0]*vol[1]*vol[2]
    print(result)
vol(4,5,6,56,28,123,)

Dictionary = {
    "Denver" : 2.1,
    "Boulder" : 3.2,
    "Nederland" : 7.2,
    "Phoenix": 0.0
}
def print_snow(Dictionary):
    if Dictionary.values() > 3:
        print(Dictionary.items())
    elif Dictionary.values() == 0:
        print(Dictionary.keys(),":","No snow!")

print_snow(Dictionary)