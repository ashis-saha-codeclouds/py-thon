userString = input("Enter the string where you want to count a specific character: ")
charToCount = input("Enter the character to count within the string: ")
def countTheChar(userString,charToCount):
    charCount = 0
    for char in userString:
        if char == charToCount.lower() or char == charToCount.upper():
            charCount = int(charCount + 1)
    return charCount
totalChar = countTheChar(userString, charToCount)
print(totalChar)
