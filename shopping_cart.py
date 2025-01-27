"""
Author: Liza Hamadi
Date: 2025-01-26

This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.

"""
from logging import exception

price = []
name = []
qnt = []
try:
    print("Welcome to the Shopping Cart Program!")

    for i in range(3):
        iname = (input("Enter the item name :"))
        name.append(iname)
        pitem=int(input(f"Enter the number of item {name[i]}:"))
        price.append(pitem)
        iqnt=int(input(f"Enter the quantity {name[i]} :"))
        qnt.append(iqnt)

    total_cost=price[i]*qnt[i]
    print(f"The total cost is: {total_cost}")



except :
    print('Invalid input')

#############
