menu = {
    'Pizza': 40, 
    'Pasta': 50,
    'Burger': 20,
    'Salad': 60,
    'Maggi': 30,
    'Coffee': 80,
    'Water Bottle': 20
}

print("Welcome TO Our Python Resturent")
print("Pizza: 40 Rs\nPasta: 50 Rs \nBurger: 20 Rs\nSalad: 60 Rs\nMaggi: 30 Rs/nCoffee: 80 Rs/nWater Bottle: 20 Rs ")

order_Total = 0

item1 = input("Enter The Name Of The Item!\n")
if item1 in menu:
    order_Total += menu[item1]
    print(f"Your item {item1} has been added in your order ")

else:
    print(f"order item {item1} is not avaialable yet!!")
 

another_order = input("Do you want to add another item to your order (Yes/No)")

if another_order == "Yes":
    item2 = input("Enter the name of item you want to order\n")
    if item2 in menu:
        order_Total += menu[item2]
        print(f"Item{item2} has been added to your order ")
    else:
        print(f"Order item {item2} is not avaialable!!")

print(f"The total amoount Of Order is {order_Total}")


