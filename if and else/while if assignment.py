print("What is your initializer?")
i = int(input())
print("What is your limit?")
limit = int(input())
initial = i % 2
if initial == 0:
    s = 0
    while i <= limit:
        s = s + i
        i = i + 2
    else:
        print("The sum of the even number is", s)


elif initial == 1:
    s = 0
    while i <= limit:
        s = s + i
        i = i + 2
    else:
        print("The sum of odd number is", s)