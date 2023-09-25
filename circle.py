def findTheCircleArea (r) : # findTheCircleArea is Function which will take the radius as r
    PI = 3.14; # Defined the value of PI as 3.14 whoch is fixed
    return PI * (r*r); # The Function returned the area of the circle PI * (r*r)
radius = float(input(("Enter the Radius of the Circle: "))); # Taking the Radius input
print("Given Radius: ", radius); # printing the Radius entered by the User
print("Area of the Circle is: ", findTheCircleArea(radius)); # Calling the Function to calc the are of the circle and displaying the outpiut




