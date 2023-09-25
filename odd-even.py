num = int(input("Enter a number: ")) # Taking a number as a input and then converted to the int by type casting
def isEvenOrOdd(num): # isEvenOrOdd is a function that will check a even and odd number
    if (num % 2) == 0: # A number is even if division by 2 gives a remainder of 0 else it will be a odd number
        print(num, "is a Even number")
    else:
        print(num, "is a odd number")

isEvenOrOdd(num);

