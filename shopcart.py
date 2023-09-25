totalItem = int(input( "Please enter the number purchased items: "))  # Taking the No of Purchased Items
cartItemPriceList = []  # Define a empty Cart Item Price List
for i in range(0, totalItem):  # Iterate over the loop to push the price of the items
    cartItemPrice = float(input())  # Taking the price inouts
    cartItemPriceList.append(cartItemPrice)  # Appending the cart items price in the cart list
print("You have entered the following Cart Item Price: ", cartItemPriceList)  # Displaying the cart items
print("Total Cart Item Price: ", sum(cartItemPriceList))  # Calculate the Total price entered by the user using the Sum native function



