fullName = input("Enter your full name: ") # Get the name from User
def getTheNameInitial(fullName): # getTheNameInitial function to take the name as input to generate the initials of the given name
    nameInitials = "" # Define a empty nameInitials to store the intial char of the given name
    splitName=fullName.split(" ") # Spliting the name using Split() native function
    for name in splitName:
        #print(name[0])
            nameInitials = nameInitials + name[0].upper() + "."
    return nameInitials # returning the intials

nameAfterInitials=getTheNameInitial(fullName)
print("Full Name: ", fullName)
print("Initial Name: ", nameAfterInitials)