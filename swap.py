def swapTheNumbers(n1,n2):
    n1 = int(n1+n2); #2+6=8
    n2 = int(n1-n2); #8-6=2
    n1 = int(n1-n2); #8-2=6
    nums = dict();
    nums['num1'] = n1
    nums['num2'] = n2
    return nums;
num1 = int(input("Enter the first number: "));
num2 = int(input("Enter the second number: "));
print("Numbers before the swap: ", num1, "And", num2);
swappedNo = swapTheNumbers(num1,num2);
print("Numbers After the swap: ",swappedNo['num1'], "And", swappedNo['num2']);