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
        self.__price = price
        self.quantity = quantity
        self.__name = name #adding two inderscores jsut makes it a private attribute

        Item.all.append(self)
    def sales(self):
       return self.__price * self.quantity
    @classmethod
    def clsmethod(cls):
        return "Class Methods Are Used When We Need To Work With Something That's Not An Instance Of A Class"
    @staticmethod
    def check_number(number):
        """
        Checks the type of the number and returns it as an integer if it's a float equivalent to an integer.

        :param number: The number to check.
        :return: The number as an integer if it's a float equivalent to an integer, otherwise the original number.
        """
        if isinstance(number, int):
            return number
        elif isinstance(number, float): #isinstance(object, type) "Used For Checking(Returns True Or False)"
            if number.is_integer(): #only works in decimal vals like 1.0 or 3.14
                return int(number)  # Convert to int if it's a float equivalent to an integer
            return number
        else:
            raise ValueError("The input must be an integer or a float.")
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.__price},{self.quantity})"
    @property
    def price(self):
        return self.__price
    def discount(self):
        return self.__price * Item.pay_rate
    def increment(self, increper):
        return self.__price + self.__price * increper

    @property #Getters Are Immutable After Initialization
    def name(self):
        return self.__name
    @name.setter # you can use getters and setter to execute specific code with it when  taking or  asssinging value to a variable
    def name(self,value):
        self.__name = value

item1 = Item("Phone", 120, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
#From Here
item5 = Item("Keyboard", 75, 5)
print(item1.name)
print(item1.sales())
print(int(item1.discount()))
#print(Item.__dict__,item1.__dict__)#Checking The Attributes Of Class Vars And Instance Vars Respectively in dict
for instance in Item.all:
    print(instance.name,end=" ")
#CSV FILE = COMMA SEPERATED VALUE FILE. In This File, Each Line Represents A Structure Of Data From Which We Can
#Access Our Code Only Avalaible In Pycharm Pro :(
print(Item.clsmethod())

numbers = [10, 10.5,12.0]
for num in numbers:
    result = Item.check_number(num)
    print(f"Before = {num}, After = {result}")

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0, fquantity=0):
        super().__init__(
            name, price, quantity
        )
        assert price >= 0
        assert quantity >= 0
        assert broken_phones >= 0
        self.broken_phones = broken_phones
        self.fquantity = fquantity
        Phone.all.append(self) #Can Be Removed
    def real_price(self):
        pass

phone1 = Phone("IPhone 12",500.0,8,1)
print(phone1.sales())
phone1.real_price()

print(Phone("IPhone 13 Pro",800.0,8,2))
print(Item("IPhone 13",800.0,8))
print(item1.increment(0.3))

# 1) Encapsulation = Restricting Attributes To Be Accessed Outside The Class
# 2) Abstraction = Only Shows Necessary Info Hides Unnecessary Info :3
#For Example:-
class Example:
    def __foo(self):
        test_num = 5+89
        return print(test_num)
    def result(self):
        self.__foo()
ex1 = Example()
ex1.result()
#Inheritance = Child Classes Inheriting From Parents
#Polymorphism =  The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
#For Example;-
class Keyboard(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_boards=0, fquantity=0):
        super().__init__(
            name, price, quantity
        )
        assert price >= 0
        assert quantity >= 0
        assert broken_boards >= 0
        self.broken_boards = broken_boards
        self.fquantity = fquantity
        Keyboard.all.append(self) #Can Be Removed
    def real_price(self):
        pass
keyboard1 = Keyboard("GXT Gaming Keyboard",3400)
print(keyboard1.discount())
