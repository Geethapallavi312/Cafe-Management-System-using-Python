'''-------------------------(Cafe Management System)----------------------------------------------------------------------------------------------'''
class My_cafe:

    def __init__(self):
        print("\n\"Welcome to Little_Delights cafe Shop\"")
        print("\nThe Menu is here. Please order and enjoy our Service.")
        self.menu={
        'Cheese_Pizza':250,
        'Corn_Pizza':300,
        'Panner_Pizza':350,
        'White_Souse_Pasta':169,
        'Red_Souse_Pasta':150,
        'Fruit_Salad':80,
        'Coffee':50,
        'Bread':60,
        'Coke':120,
        'Water Bottle':20
        }
        print("\nMenu:")
        for item, price in self.menu.items():
            print(f"{item}: Rs {price}")

    def order(self,item_name):
        order_total=0
        if item_name in self.menu:
            print("Your item {} is added to the orders.".format(item_name))
            return self.menu[item_name]
        else:
            print("Sorry..! Your item {} is currently unavaliable. Please order something else.".format(item_name))
            return 0
        
cafe=My_cafe()

total_bill=0

while True:
    item_name=input("Please enter your item name:")
    total_amount=cafe.order(item_name)
    total_bill+=total_amount
    option=input("Do you want to add another item ? [Yes\ No]: ")
    if option=='No':
        print("Your total bill for the order to pay is: Rs {} ".format(total_bill))
        break
    
print("Thank you for visiting us. Please come again..!")



    



        
