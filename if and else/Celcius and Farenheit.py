c = int(input("collect celcius temperature"))
f = int(input("collect farenheit temperature"))
def fah2cel(f):
    result=((5*f)-160)/9
    print(f, "to celcius is", result)


def cel2fah(c):
    result =((c*9)+160)/5
    print(c,"to farenheit is",result)

fah2cel(f)
cel2fah(c)




