prefixKeys = {
    1: "Tera",
    2: "Giga",
    3: "Mega",
    4: "Kilo",
    5: "Deci",
    6: "Centi",
    7: "Mili",
    8: "Micro",
    9: "Nano",
    10: "None"
}
prefixes = {
    "Tera": 10**12,
    "Giga": 10**9,
    "Mega": 10**6,
    "Kilo": 10**3,
    "Deci": 10**-1,
    "Centi": 10**-2,
    "Mili": 10**-3,
    "Micro": 10**-6,
    "Nano": 10**-9,
    "None": 1
}

time = { # Based on seconds
    "Hour": 3600,
    "Minute": 60,
    "Day": 86400
}

other = {
    "Miles": 1.60934 # Based on km
}

def Length(value,originalPrefix,desiredPrefix):
    result = 0
    desiredPrefix = float(prefixes[desiredPrefix])
    originalPrefix = float(prefixes[originalPrefix])
    result = value * (originalPrefix / desiredPrefix)
    return(result)


# Calculator has 21 spaces to  print out something horizontally
# 6 Spaces to print vertically
exit = False
while exit != True:
    selectionMain = int(input("""1. Length(Working)\n2. Speed and Velocity(NOT WORKING)
3. Mass(NOT WORKING)\n4. Volume(NOT WORKING)\n5. Time(NOT WORKING)\n6. Exit\n"""))
    while (selectionMain != 1 and selectionMain != 7):
        selectionMain = int(input("""1. Length\n2. Speed and Velocity
3. Mass\n4. Volume\n5. Time\n6. Exit\n"""))
    if (selectionMain == 1):
            value = int(input("Original Number: "))
            for x, i in enumerate(prefixes):
                print(str((x+1)) +": "+ i)
            originalPrefix = input("Original Prefix: ")
            while (originalPrefix not in range(1, 11)) or (type(originalPrefix) != int ):
                for x, i in enumerate(prefixes):
                    print(str((x+1)) +": "+ i)
                originalPrefix = int(input("Original Prefix: "))
            desiredPrefix = input("Desired Prefix: ")
            while (desiredPrefix not in range(1, 11)) or type(desiredPrefix) != int :
                for x, i in enumerate(prefixes):
                    print(str((x+1)) +": "+ i)
                desiredPrefix = int(input("Desired Prefix: "))
            originalPrefix = prefixKeys[originalPrefix]
            desiredPrefix = prefixKeys[desiredPrefix]
            if (desiredPrefix == "None"):
                print(str(Length(value, originalPrefix, desiredPrefix)) +" meters")
            else:
                print(str(Length(value, originalPrefix, desiredPrefix)) +" "+ desiredPrefix +"meters")
    if (selectionMain == 6):
        exit = True
        break
"""
The plan for SpeedAndVelocity is to have it call to the distance and time method seperately
in order to keep code simple
This means that the main piece of code is going to have if statements that
call the other methods such as speed, length, mass, volume etc...
What I'm thinking right now is that the arguments for:
SpeedAndVelocity will remain empty
Length, mass, and time will have value and prefix
Temperature will not have any and contain everything in the def
Rest will be the same
Will have global variable that users can save variables to. Ex if you convert 
km to m and you also want to convert kg to g.
"""