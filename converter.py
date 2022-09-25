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
    selectionMain = int(input("""What would you like to convert?\n1. Length(Working)\n2. Speed and Velocity(NOT WORKING)
    \n3. Mass(NOT WORKING)\n4. Volume(NOT WORKING)\n5. Temperature(NOT WORKING)\n6. Time(NOT WORKING)\n7. Exit\n"""))
    while (selectionMain != 1 and selectionMain != 7):
        print("Select option 1-7\n")
        selectionMain = int(input("""What would you like to convert?\n1. Length\n2. Speed and Velocity
        \n3. Mass\n4. Volume\n5. Temperature\n6. Time\n7. Exit\n"""))
    if (selectionMain == 1):
            value = int(input("What is the value of the original number? "))
            counter = 1
            for i in prefixes:
                print(str((counter)) +": "+ i)
                counter += 1
            originalPrefixSelection = int(input("What is the original prefix: "))
            while (originalPrefixSelection not in range(1, 11)):
                originalPrefixSelection = int(input("Please enter a number from 1 to 10: "))
            desiredPrefix = int(input("What is your desired prefix: "))
            while (desiredPrefix not in range(1, 11)):
                desiredPrefix = int(input("Please enter a number from 1 to 10: "))
            originalPrefixSelection = prefixKeys[originalPrefixSelection]
            desiredPrefix = prefixKeys[desiredPrefix]
            if (desiredPrefix == "None"):
                print(str(Length(value, originalPrefixSelection, desiredPrefix)) +" meters")
            else:
                print(str(Length(value, originalPrefixSelection, desiredPrefix)) +" "+ desiredPrefix +"meters")
    if (selectionMain == 7):
        exit = True
        break
        
        

#elif (selectionMain == 2):
    #Speed and velocity code
#elif (selectionMain == 3):
    #Mass code
#elif (selectionMain == 4):
    #Volume code
#elif (selectionMain == 5):
    #Temp
#elif (selectionMain == 6):
    #Time


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