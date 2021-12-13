# Testing Numbers
testnumbers = 25
eventest = testnumbers % 2
oddtest = testnumbers % 2
primetest = testnumbers % 2
finalprimetest = primetest / 2
if eventest == 0:
    print("The number", testnumbers, " is Even")
elif oddtest > 0:
    print("The number", testnumbers, "is ODD")
elif finalprimetest == 0.5:
    print("The number", testnumbers,"is PRIME")
else:
    print ("Something is wrong")

# While if and while else LOOP
words = "connections"
i = 1

while i < len(words):
    print("Great")
    i += 1
else:
    print("That's wrong!")
# Sum of integers from 0 to 100
x = 0 
s = 0
while x <= 10:
    s = s + x
    x = x + 1

else:
    print("The sum of first 9 integer:", s)