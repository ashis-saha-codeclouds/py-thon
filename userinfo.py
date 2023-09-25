def displayTheUserInfo(name,age,favcolor):
    userinfo = "Hello this is ", name, "My age is ", age ," And my favourite color is ", favcolor;
    print (userinfo);
def getTheUserInfo():
    name = input("Please Enter your name: ")
    age = int(input("Please enter your age: "))
    favcolor = input("Please enter your Favourite color: ")
    displayTheUserInfo(name, age, favcolor);
getTheUserInfo();


