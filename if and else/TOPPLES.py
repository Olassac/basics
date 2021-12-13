Class1 = ("Ayo",13,80,"Enugu")
AyoAddress = Class1[3]
print (AyoAddress)
AyoRange = Class1[:3]
print(AyoRange)

# Updating a tupple
# Convert to List
Class2 = list(Class1)
Class2.append("Banjo")
print(Class2)
# Return back to Tuple
Class3 =tuple(Class2)
print(Class3)
