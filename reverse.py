def reverseTheString(string): # Function to generate the reverse string
    reverseStr="" #Emplty string to store the reversed string
    for i in string: #For loop to iterate over the char of string
        #reverseStr = reverseStr + i
        reverseStr = i+reverseStr #concat the string in a reverse order
    return reverseStr; #It will return the reverse string
string = input("Enter the string to reverse: "); #Taking the user Input
print(reverseTheString(string)); # Calling the Reverse String function


