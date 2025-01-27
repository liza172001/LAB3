"""
Author: Liza Hamadi
Date: 2025-01-26

This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.

"""
def shop():

    price = []
    name = []
    qnt = []
    total_cost=0

    try:
        print("Welcome to the Shopping Cart Program!")

        for i in range(3):
            i_name = (input("Enter the item name :"))
            name.append(i_name)
            p_item=int(input(f"Enter the price of item {name[i]}:"))
            price.append(p_item)
            i_qnt=int(input(f"Enter the quantity {name[i]} :"))
            qnt.append(i_qnt)

          # total_cost=price[i]*qnt[i]
          #   print(f"The total cost is: {total_cost}")



    except ValueError:
        print('Invalid input')

    #############
    #total_cost=0

    for i in range(len(price)):
        total_cost = price[i] * qnt[i] + total_cost

    print(total_cost)
    if total_cost > 100:
        discount = total_cost * 0.1
        total_cost -= discount
        print(f"\nYou saved ${discount:.2f} with a 10% discount!")
        print(f"Discounted Total: ${total_cost:.2f}")

while True:
    restart = input("\nWould you like to shop again? (yes/no): ").lower()
    if restart == "yes":
        shop()

    else:
     print("Thank you for shopping with us!")




