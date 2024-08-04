#These Are Modules/Packages
import math
import time
import random
import os
import shutil
import module #as mdl(nickname)
#or from module import hello(importing a specific function from a module/script)
#Variables
fstnme = "Rana"
lstnme = "smd"
fnme = fstnme + " " + lstnme
age = 21
age = age +2
age += 2
height = 255.5
isbot = True
a ,b = 2 , 3
c, d , e = 45 , "hi", 22.75

#Program
'''
#Basic Logic And Type Casting...
#print("Hello World!")
#print("goodbye")
#joe_biden = "sleepy"
#print(type(joe_biden))
#print(joe_biden+ " trump")
#print("hello " + fnme )
#print(type(age))
print("Your  Age Is =  "+ str(age))
#print(type(height))
print("your height is ="+ str(height) + "ft")
print(type(isbot))
print("The Fact That The Object Is A Bot Is = "+ str(isbot))
#Moving Forward
print(a + b)

# String Functions
print(len(d))
print(d.find("i"))
print(d.capitalize())
print(d.upper())
print(d.lower())
print(d.isdigit())
print(d.isalpha())
print(d.count("i"))
print(d.replace("i","o"))
print(d*7)

# More Type Casting(Converting The Data Type Of One Variable To Another In A Print Function Or Outside While Assigning)
x = 3
y=6.8
z="4"
z = int(z)
x = float(x)
print(int(y))
print(x)
print(z)

#Taking Inputs
age = int(input("Whats Yo Age? :"))
#print("My Age Is:"+age )
#age = int(age)
print(age+55)
tallness = float(input("Whats Yo Height Bro?: "))
print("Yu RAe "+str(tallness)+"mm tall wtf?")

#Math Functions:-
pi = 3.14
even = 4
i,j,g= 2,3,6

#Round Number
print(round(pi))
#Round To Highest
print(math.ceil(pi))
#Round To Lowest
print(math.floor(pi))
#Find The Absolute Value
print(abs(pi))
# Raise To A Exponent
print(pow(pi,67))
#Take Square Root
print(math.sqrt(even))# pi have no sqrt
#Find The Largest Among Variables
print(max(i,j,g))
#Find The Smallest Among Variables
print(min(i,j,g))

#string slicing

#index[::] function
namae = "Dude Man"
fnamae = namae[0:4]
print(fnamae)
lnamae = namae[5:8]
print(lnamae)
haha = namae[0:8:2]
reverse = namae[ : :-1]
print(reverse)
#slice() function
website1 = "http://youtube.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])


#if , else, elif yadda yadda
ages =  int(input("Whats Yo Age? ="))
if ages == 100:
    print("You Are 100 Years Old!")
elif ages >= 18:
    print("You Are An Adult!")
elif ages < 0:
    print("You Have Not Been Born Yet")
else:
    print("You Are Still A Child")

#logical operators
wind = 12
temp = int(input("Enter Temp  = "))
 # and operators can be used to check if both conditions are true or not
if temp >= 0 and temp <= 30:
    print("Touch Grass")
# or operators see if one of the following conditions are true and if they are the program executes else not
elif temp < 0 or temp > 30:
    print("Crank 90's n Chill")
#not operators
elif not(wind == 12):
    print("Its Safe Outside!")

#while loop
#while 1 == 1:
#    print("Hi")
namee = ""
nameee = None
while len(namee) == 0:
    namee = input("Enter Ya Name = ")
print("Hello " + namee)
#Another Way Of Writing while
while not nameee:
    nameee = input("Enter Yo Mamas Name = ")

#for statements
for i in range(12, 101,2):
    print(i)
for j in "Joe Biden":
    print(j)
#time.sleep() // delays the execution of code by secs
for k in range(10,0,-1):
    print(k)
    time.sleep(0.5)
print("Happy New Year!")


#nested loops

#The end parameter in the print function is used to add any string. At the end of the output of the print statement in python. By default, the print function ends with a newline. 
#Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.

rows = int(input("Enter Rows = "))
columns = int(input("Enter Columns = "))
symbol = input("Enter A Symbol = ")
for m in range(rows):
    for n in range(columns):
        print(symbol, end  ="")
    print()

#The empty print() statement at the end of the code serves to print a newline character after each row of symbols has been printed in the nested for loop.
#Without this empty print() statement, the symbols would be printed continuously without any separation, resulting in a single line of symbols.
#By including print() without any arguments, it adds a newline character after each row of symbols, creating a visual separation between rows and forming a rectangular 
#pattern of symbols based on the specified number of rows and columns.


#loop Control statements
#break
while True:
    name1 = input("Enter Your Name =  ")
    if name1 != "":
        break
#continue
phone = "0305-2774693"
for i in phone:
    if i == "-":
        continue
    print(i, end ="")
for o in range(10,20):
    if  o == 12:
        pass
    else:
        print()

#llists
food = ["biryani", "pizza", "karahi"]
food[0] = "fish pulao"
#List Functions
food.append("ice cream")
food.insert(5, "Jenifer")
#food.remove("Jenifer")
food.pop()
#food.clear()
food.sort()
food.reverse()
#print(food[0])
for q in food:
    print(q)

#2D List Is A List Of Lists;-
cake = ["milk", "eggs"]
water = ["hydrogen", "oxygen"]
stuff = [cake, water]
#print(stuff)
print(stuff[0][1]) #prints eggs

#List Comprehension
yum_fruit = ["apple","banana","kiwi","mango"]
newlist = [x for x in yum_fruit if "a" in x]
print(newlist)

#Tuples = Similar To Lists But Cannot Be Modified After Creation And Is Ordered
person = ("Hello", "My Age Is ", 23)
print(person.count("Hello"))
print(person.index(23))
for b in person:
    print(b)

#sets
set1 ={1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
set_a = {"Hello" ,"World"}
set_b = {"Goodbye","World"}
#sets Functions
#set1.add(0)
#set2.remove(10)
#set2.clear()
#print(str(set1) + str(set2))
#print(set_a.update(set_b))
union_set = set1.union(set2)
print(union_set)
inter_set = set2.intersection(set1)
print(inter_set)
diff_set =  set1.difference(set2)
print(diff_set)

#dictionary = A dictionary is also a non-homogeneous data structure that stores key-value pairs.
friends ={"BFF" : "Kashan",
                  "Buddy" : "Meesum",
                  "Sideman" : "Sobi" }
friends.update({"Rival" : "Ali Naem"}) #adds element
print(friends["Buddy"])
print(friends.get("Foe : Zaid")) #checks existance of  an element
#friends.pop("BFF") # removes an element
print(friends.keys())
print(friends.values())
print(friends.items())
for keys, item in friends.items():
    print(keys,item)

#index operator [] = gives access to sequence element, can be ued in a str, list, tuples 
name2 = "bro Code$"
#if(name2[0].islower()):
#    name2 = name2.capitalize()
first_name2 = name2[0:3].upper()
last_name2 = name2[4:8].lower()
final_char = name2[-1]
print(first_name2, last_name2, final_char)

#functions
y = 12
w = 6
def hello(fname,lname,ages):
    print("Hello"+" "+fname+" "+lname )
    print("You Are "+str(ages)+" Years Old"+", You Like Python.")
hello("Abdus","Samad.", 16)#positional arguments
#while y > w:
#    hello("Abdus","Samad.", 16)
#    w = w+1

#return statement[] = returns values in functions to the caller
def mul(n1,n2):
    mul1 =  n1 * n2
    return mul1
print(mul(12,39))

#def alag():
#    n3 = 10
#    print(n3)
#    return n3
#print(alag())

# keyword arguments for def = can be in different order and we can assign the name of the parameters to the  arguments
def bye(first,last):
    print("Goodbye "+first+" "+last)
bye(last="Samad",first="Abdus")

#nested function calling = just what you would expect
#instead of:-
#n = input("Enter Your Age")
#n = float(n)
#print(n)
#we can do:-
print(float(input("Enter Your Age  =  ")))

#Variable Scope = Region Where Variable Is Recognized And Executed In Order  Of LEGB
#e.g
naam = "Rana"#global variable
def dname():
    naam = "Tigrina"#local variable
    print(naam)
print(naam)#global and local variables can be of the same name but can be printed differently
dname()#a global variable can be accessed by a function but a local variable cannot be accessed outside a function

#*args = parameter taht will pack arguments into a tuple, it can be used for a varying amount of arguments
def argss(*args):
    sum = 0
    #args is a tuple so we can change it into a list
    #args = list(args)
    # sum[0] = 0 and set the first argument as 0
    for t in args:
        sum += t
    return sum
print(argss(1,2,3,4,10))

#**kwargs = parameter taht will pack arguments into a dictionary, it can be used for a varying amount of keywords arguments
def mrfeet(**kwargs):
    print(kwargs["st"] + ", I Said! ")
          #items,value
    for key,value in kwargs.items():
        print(value,end=" ")
mrfeet(st = "Hello",nd = "I'm",rd = "MrFeet")

#str.format()
#{} = Format Field ( Placeholder for items or variables )
animal = "cow"
item = "moon"
#print("The {} jumped over the {}".format("cow", "moon"))
#print("The {} jumped over the {}".format(animal, item))
#print("The {1} jumped over the {0}".format(animal, item))#positional argument
#print("The Fat {animal} jumped over the {item} and the {animal}".format(animal = "cow", item = "moon"))#keyword args
text = "The {} Jumped Over The {}"
print(text.format(animal,item))
pi =3.14159
print("The Number Pi Is {:.2f}".format(pi))#prints decimal values n number of times after decimal point e.g = {:nf}.format()
numero = 1000
print("The Number  Is {:b}".format(numero))#prints binary value
print("The Number  Is {:o}".format(numero))#prints octal value
print("The Number  Is {:x}".format(numero))#prints Hexadecimal Value
print("The Number  Is {:e}".format(numero))#prints number in scientific notation
print("The Number  Is {:,}".format(numero))#prints a comma after the first digit

#Random Numbers
s = random.randint(1,10)#prints two ints in a specific range
print(s)
v = random.random()#prints random value b/w 0 and 1
print(v)
myList = ["Rock","Paper","Scissors"]
e = random.choice(myList) #random.choice = Choose a random element from a non-empty sequence.
print(e)
nameList = ["Mr. ","Rana", "Abdus", "Samad"]
random.shuffle(nameList)#shuffles a number of elements in a list
print(nameList)

#exception = events that disturb the flow of a program during execution
try:#tries code that might be dangerous
    numerator = int(input("Enter A Number As The Numerator = "))
    denominator = int(input("Enter A Number As The Denominator = "))
    result =  numerator/denominator
    print(result)
except ZeroDivisionError as e:#error statement from console is stored in e , #Zero Div Error: checks for error of division by 0
    print(e)
    print("Fuck Off Man, Its Gyattdayum Error!")
except ValueError:#checks if the value is valid or not
    print("Enter Integer Numbers Only :3")
except Exception: #Checks Code For Error In Execution And Executes Its Associated Code
    print("Error Code 69")
#else: #You Can Put A Else Statement To Be Executed If No Exception Occurs
#    print(result)
finally:
    print("The 'Finally' Will Always Execute!")

#File Handling:-
#Checking File Existence
path = "C:\\Users\\asama\\3D Objects\\hentai.txt"#\\ is the escape sequence for displaying \ In A String!
path2= "C:\\Users\\asama\\3D Objects\\18+"
if os.path.exists(path):
    print("The Path '{}' Exists!".format(path))
    if os.path.isfile(path):
        print("It Is A File!")
    if os.path.exists(path2):
        print("The Path '{}' Also Exists!".format(path2))
        if os.path.isdir(path2):
            print("The Directory '{}' Exists!".format(path2))
else:
    print("The Path '{}' Does Not Exist!".format(path))

#Reading Files
try:
    with open("rana.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Error Code 69: File Not Found!")

#Writing Files
yamete = "Mou Yamete Kudasai!\nAh Ah Ah Ah\n EEIAAAA!!! "
with open("test.txt","w") as file:
    file.write(yamete)
#writing something else and keeping 'w' in  with open will overwrite the file to add something else to the end of file by appending(changing 'w' by 'a')
#for example
udasai = "YOOOO!"
with open("rana.txt","a") as file:
    file.write(udasai)

#Copying A File (by importing shutil)
#shutil has functions like copyfile() = copy contents of  a file /// copy() = copyfile() + persmission mode + destination of that file or directory /// copy2() = copy() +  files craetion and modification times
shutil.copy("rana.txt","ranacopy.txt")#src,dst

#Moving A File And Directory
source = "ranacopy.txt"
destination  = "C:\\Users\\asama\\3D Objects\\ranacopy.txt"
#os.replace(source,destination)
shutil.move(source,destination)
if os.path.exists(destination):
    print("The File Has Been Successfully Moved!")
src = "cod_points"
des  = "C:\\Users\\asama\\3D Objects\\cod_points"
os.replace(src,des)
if os.path.exists(des):
    print("The Directory Has Been Successfully Moved!")

#Deleting A File
sponge = "krabby_patty.formula.txt"
try:
   os.remove(sponge)
   print("The File Has Been Successfully Removed!")
except:
    if FileNotFoundError:
        print("The File Does Not Exist In The Given Address...")
#This Does Not Delete Empty Folders So,
folpath = "testfol"
try:
    #os.remove(folpath) #os.remove will not work for empty folders
    os.rmdir(folpath) #os.rmdir will not work for folder containing files
    #shutil.rmtree(folpath) = is used to delete folders containing files
except FileNotFoundError:
    print("File Has Been Removed Or Does Not Exist!")
except PermissionError:
    print("You Dont Got Permission To Copeh Dat Foldher,Eh?")

#modules
module.hello()
module.goodbye()
#lambda
d = lambda a, b : a * b
print(d(5, 6))

#---------------------------------OOP (CS50P's)------------------------------------
def main():
    student = get_student()
    print(f"{student['naam']} from {student['house']}")
    #print(f"{student[0]} from {student[1]}")
def get_student():
    #naam = input("Name: ")
    #house = input("House: ")
    #return naam,house
# Could Become A Tuple By Adding () Or Lists Or Mutability By Adding [] and vice versa

    #Using Dictionary
    student = {}
    student["naam"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    #Could Become A Tuple By Adding () Or Lists Or Mutability By Adding [] and vice versa
if __name__ == '__main__':
    main()

#CS50's OOP CLASS
#1. Encapsulation
class Student:
    def __init__(self,name,house,tribe):
        if not name:
            raise ValueError("Data Not Found!")
        self.name = name
        self.house = house
        self.tribe = tribe
    def __str__(self):
        return f"{self.name} from {self.house} and says {self.tribee()}"
    def tribee(self):
        match self.tribe:
            case "Punjabi":
                return "Balle Balle"
            case "Sindhi":
                return "Saale Biryani Kidhar Hai"
            case "Balochi":
                return "JEEEEEOOOOOO!"
            case "Pathan":
                return "Marha Meri Naswar Kidhar He?"
            case _:
                return "ALLAH U AKBAR!"
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        tribe = input("Tribe: ")
        return cls(name, house, tribe)
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in ["Lahore", "Peshawar", "Karachi", "Gawadar"]:
            raise ValueError("Data Not Found!")
        self._house = house
def main():
    student = Student.get()
    #student.house = "Number 29, Hafiz Gardens" #wrong syntax
    #print(f"{student.name} from {student.house}")
    print(student)

#def get_students():
#    name = input("Name: ")
#    house = input("House: ")
#    tribe = input("Tribe: ")
#    student = Student(name,house,tribe)
#    return student

if __name__ == "__main__":
    main()

class Hat:
    houses = ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]
    @classmethod
    def sort(cls,name):
        print(name,"is from",random.choice(cls.houses))
#hat = Hat()
Hat.sort("Harry")

'''
#2. Inheritance
class Wizard:
    def __init__(self, name):
        self.name = name
        if not name:
            raise ValueError("INVALID VALUE")

class Student2(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Bear")
studentz = Student2("Harry", "Gryffindor")
professor = Professor("Roxy", "Water Saint Magic")

