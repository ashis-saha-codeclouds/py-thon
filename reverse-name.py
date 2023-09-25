fullname=input("Enter your full name: ")
def reverseTheName(fullname):
    names = fullname.split(" ")
    #print(name[0],name[1])
    revname = ""
    nameInitials = ""
    resData = []
    for name in reversed(names):
        #print(name)
        #print(' '.join(name))
            nameInitials = name[0] + "." + nameInitials.upper()
            revname = revname + name + " "
            resData=[len(revname.strip()), revname.strip(), nameInitials]
    #print(resData)
    #return revname.strip(),nameInitials
    return resData
_responseData = reverseTheName(fullname)
#print(_responseData)
print("Name Before Reverse: ",fullname)
print("Total No. of Characters: ",_responseData[0])
print("Name After Reverse: ", _responseData[1])
print("Name Initials: ", _responseData[2])


