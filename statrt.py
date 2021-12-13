x = "hello word"
print(x)


for x in range(5):
    print (x)

for x in range (2,10,2 ):
    print (x)

x = "Hello"
position = x[3]
print(position)

x = "House"
length = len(x)
print (length)

Word = "Criminals are hard element in Akure"
check = ("Akure" in Word)
print (check)

Word = "Criminals are hard element in Akure"
if "Akure" in Word:
    print ("Yes it is")

x = "Hello Akure"
slice =x[:5]
print (slice)
slice1 = x[:7]
print (slice1)
slice2 = x[6:]
print (slice2)

# I am new to coding
x = "Welcome Home"
Case = x.upper()
print(Case)
Case1 = x.lower()
print (Case1)
Case2 = x.strip()
print(Case2)
Case3 = x.replace("Home", "You")
print(Case3)
Case4 = x.replace("Welcome","Going")
print(Case4)

print("Good morning!")
Username = input("enter username")
print('Hi',Username,"Welcome")

print("Good morning!")
Username = input("enter username")
print("Hi", Username.upper(),"Welcome")
# The ".upper()" has been used to uppercase the name


num = 12
for i in range(13):
    print(num,"*",i,"=",num*i)


num = 2
for i in range(12):
    print(num,"*",i,"=",num*i)