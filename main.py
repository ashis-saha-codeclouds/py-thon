# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print ("Ashis\n"*3);
print ("Rajdeep dar Pathshala"[2:5])
print ("     Ashis Saha  ".strip())
print("Ashis Saha".replace("Ashis Saha","Aashis Ssaha"))
print("Welcome - {}".format("Ashis Saha"))
print("Ashis Saha"!="Ashis")
print("Ashis "<"Ashis Saha")
print("Ashis".find("A"))
print("Ashis".index("A"))
print(str(55))
print("Ashis Saha".split(" "))
print(" ".join(["Ashis", "Saha"]))
print("Ashis".startswith("A"))
print("Ashis".endswith("s"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
para= "Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances"
print(para.count('Python'))
print(para.replace("Python","PYTHON"))
strr = "malayalam"
print(int(len(strr)))
print(int(len(strr)/2))
print(int(len(strr))-0-1)
for i in range(0, int(len(strr))):
    #print(i," = ",strr[i])
    print(strr[i]," = ",strr[len(strr)-i-1])
