def calcTheSI(principal,rateOfIntr,time):
    simpleInterest = float((principal * rateOfIntr * time)/100);
    return simpleInterest;
principal = float(input("Enter the Principal Amount: "));
rateOfIntr = float(input("Enter the rate of Interest: "));
duration=int(input("Enter the tenure of the Loan: "));
print("Interest will be: ",calcTheSI(principal,rateOfIntr,duration));

