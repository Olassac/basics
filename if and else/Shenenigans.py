Dictionary = {
    "Denver" : 2.1,
    "Boulder" : 3.2,
    "Nederland" : 7.2,
    "Phoenix": 0.0
}
def print_snow(Dictionary):
    if Dictionary.values() >= 3:
        print(Dictionary.items())
    elif Dictionary.values() == 0:
        print(Dictionary.keys(),":","No snow!")

print_snow(Dictionary)
