Animals = {
    "Family":"Cat",
    "Example":"Lion",
    "Sound":"Roar",
    "Age":100,
    "Food":"Flesh",
    "OtherAnimals":["Tiger","Cheater","Wolf"]
}
print(Animals)
print(Animals["Sound"])
print(Animals["OtherAnimals"][1])
print(Animals.values())
print(Animals.items())
print(Animals.keys())
Animals["Family"]="Pisces"
print(Animals)
Animals.update({"Feed":"Plankton"})
print(Animals)
Animals.update({
    "Fishtype":["Tilapia","Titus"]
})
print(Animals)
Animals.pop("Sound")
print(Animals)
Animals.popitem()
print(Animals)
for x in Animals:
    print(x)
    for x,y in Animals.items():
        print(x,y)
Fishes = Animals
Avians = Animals.copy()
Avians.update({ "Family":"Birds"})
print(Avians)
print(Animals)