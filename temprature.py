def converTheTemp (fahrenheit):
    Celsius=((fahrenheit-32)*5)/9;
    return Celsius;
Fahrenheit = float(input("Enter the temprature in Fahrenheit: "));
print("Given Temprature in Fahrenheit : ", Fahrenheit);
print("Converted Temprature in Celsius: ",converTheTemp(Fahrenheit));