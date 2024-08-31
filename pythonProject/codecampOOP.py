class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name: str,price: float,quantity=0):
        #ASSERTION:-
        '''
        x = "hello"
        # if condition returns True, then nothing happens:
        assert x == "hello"
        # if condition returns False, AssertionError is raised:
        assert x == "goodbye"

        and

        #1(Most User Friendly In My Opinion)
        try:
           #code
        except Assertion Error:
          print("Error")
        #2
        assert a >= 0
        #3
        if -3 < 0:
          raise AssertionError("Input A Positive Value!!!")
        '''
        assert price >= 0
        assert quantity >=0
        self.price = price
        self.quantity = quantity
        self.name = name

        Item.all.append(self)
    def sales(self):
       return self.price * self.quantity
    def discount(self):
        return self.price * Item.pay_rate
    def __repr__(self):
        return f"Item({self.name},{self.price},{self.quantity})"
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
print(item1.name)
print(item1.sales())
print(int(item1.discount()))
#print(Item.__dict__,item1.__dict__)#Checking The Attributes Of Class Vars And Instance Vars Respectively in dict
for instance in Item.all:
    print(instance.name,end=" ")

#continue from 51:00
