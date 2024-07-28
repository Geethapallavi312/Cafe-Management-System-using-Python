'''--------------------------------------------------------Cafe Management System (Project)--------------------------------------------------------'''
menu={
    'Cheese_Pizza':250,
    'Corn_Pizza':300,
    'Panner_Pizza':350,
    'White_Souse Pasta':169,
    'Red_Souse_Pasta':150,
    'Fruit_Salad':80,
    'Coffee':50,
    'Bread':60,
    'Coke':120,
    'Water Bottle':20
}
print("Welcome To Little_Delights Coffee Resutrant")

print("Cheese_Pizza : Rs 250\nCorn_Pizza : Rs 300\nPanner_Pizza : Rs 350\nWhite_Souse_Pasta : Rs 169\nRed_Souse_Pasta : Rs 150\nFruit_Salad : Rs 80\nCoffee : Rs 50 \nBread : Rs 50\nCoke :Rs 120\nWater_Bottle: Rs 20")

order_total=0

item_1=input("The name of item you want to order =")

if item_1 in menu:
    order_total+=menu[item_1]
    print("Your item {} has been added to your order".format(item_1))
else:
    print("Your ordered item {} is not avaliable. Please order something else.".format(item_1))

another_order=input("Do you want to add another item ? (Yes/No)")

if another_order=='Yes':
    item_2=input("The name of item  you want to order is:")
    if item_2 in menu:
        order_total+=menu[item_2]
        print("Your item {} has been added to your orders.".format(item_2))
    else:
        print("Your ordered item {} is not avaliable. Please order something else.".format(item_2))

print("The total amount of your order to pay is: {}".format(order_total))

