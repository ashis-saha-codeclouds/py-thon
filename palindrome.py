def isPalindrome (inputString): # isPalindrome is a function to check a string is a palindrome or not
    if len(inputString) > 0: # Checking the length of the entered string
        for i in range(0, int(len(inputString)/2)): # If the length greater than 0 then running the loop to the half of the string
            if inputString[i] != inputString[int(len(inputString))-i-1]: # Checking the strings first and last character
                return False # Returning False if the given string is not a palindrome
            return True # Returning True if the given string is palindrome
    else:
        print("Please enter a string with a valid length")
        return False

inputString = input("Please enter the string to check the palindrome: ")

if isPalindrome(inputString):
    print(inputString, "is a palindrome String")
else:
    print(inputString, "is not a palindrome String")


