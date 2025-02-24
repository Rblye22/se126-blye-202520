# W8D1 in class demo - Dictionaries

#--Imports----------------------------------------------------------




#--Main Executing Code-----------------------------------------------

#--Start by ctreating a populated dictionary
myCar = {
    # 'key': value,
    "make": "Ford",
    "model": "SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black",
    # keys cannot be repeated/ NO DUPLICATES allowed if repeated last value will replace the first value
    "color": "red"
}

# display the entire dictionary -> 'myCar'
print(myCar)
# display  just the "make" and "model" valuse of the sictionary 'mycar'
#print(f"My care is a {myCar["make"]} {myCar["model"]}")

# dictionaryname["kayName"] --> acesses stored value
# "keyName" will always be a string index, created by dev

#keys cannot be repeated within a dictionary, but they can be reused acrross unique dictionary names: myCar vs yourCar
yourCar = {
    # 'key': value,
    "make": "GMC",
    "model": "Canyon",
    "year": 2019,
    "name": "Jolly",
    "color": "black",
    # keys cannot be repeated/ NO DUPLICATES allowed if repeated last value will replace the first value
    "color": "red",
    "friends": ["Ray", "Matt", "Duncan"]
}

print(f"Robs car is a {yourCar['make']} {yourCar['model']}")

# print Duncan
#print(f"{yourCar["friends"][2]}")

# processing through a dictionary and its keys
for key in yourCar:
    print(f"{key.upper()} : {yourCar[key]}")

yourCar["plate"] = "12345"

