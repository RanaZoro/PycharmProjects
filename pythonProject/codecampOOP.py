class Item:
    def __init__(self,name):
        print(f"Instance Is Created {name}")
    def sales(self,price,quantity):
       return price * quantity
item1 = Item()
item1.name = "ThinkPad"
item1.price = 35000
item1.quantity = 3
print(item1.sales(item1.price,item1.quantity))

#continue from 18:08