for x in range (1,20,2):
    print(x)

for x in range (5):
    print(x)

for x in range (1,5):
    print(x)

table = 3
for i in range (1,13):
    print(table,"x",i, "=", table*i)

print("Good morning")
print("What table do you want?")
n = int(input())
print("What limit do you want?")
limit = int(input())
for i in range (1,limit):
    print(n,"x",i,"=", n*i)