#importing modules
import math
import  random
import time
import random
import os
import shutil
'''
#printing
print("I Like Pizza")
#variables
n1 = " ASamad "
n2 = 12
n3 = 14.5
#Type Casting
print("Hello "+n1+"You Are "+str(n2)+" Years Old!")
n4 = int(n3)
print(n4)
#Assigning Tactic
n5,n6,n7 = 44, 67.8, "YO!"
print(n6)#Confirmation
#String Functions
n8 = "python"
print(len(n8))#prints no of characters
print(n8.find("p"))
print(n8.capitalize())
print(n8.upper())
print(n8.lower())
print(n8.isdigit())
print(n8.isalpha())
print(n8.count("o"))
print(n8 * 5)
print(n8.replace("t","l"))
#Inputs
#n9 = input("Enter Your Name = ")
#print(n9)
#Lists
n10 = ["Apple","Banana","Mango"]
n11 = n10[0]
print(n11)
n10[1] = "Strawberry"
#print(n10)
#Lists Functions
n10.append("Franky")
print(n10)
n10.insert(4,"Brook")
print(n10.remove("Apple"))
n10.pop()
#n10.clear()
n10.sort()#Ascending Order
n10.reverse()#Descending Order
print(n10)
#Tuples
n12 = (5,4,2,3,1)
print(n12[2])
#Sets
n13 =  {"forks","Knives","spoons"}
#sets functions
n13.add("plate")
n13.remove("Knives")
print(n13)
#n13.clear()
n14 = {1,2,3,4}
n15 = {3,4,5,6}
n16 =n14.union(n15)
n17 = n14.intersection(n15)
n18 = n14.difference(n15)
print(n16 , n17 , n18)
#dictionary
n19 = {
    "Name" : "PyBro",
    "Grade" : "A",
    "Age" : 16
}
#Dictionary Functions
print(n19["Name"])
print(n19.items())
n19.update({"Color":"Orange"})
print(n19.get("Name"))
n19.keys()
n19.values()
for keys, item in n19.items():
    print(keys,item)
#Math Functions
n20 = 3.14
n21 = 4
n22 =round(n20)
n23 = math.ceil(n20)
n24 = math.floor(n20)
n25 = abs(n20)
n26 = pow(n20,5)
n27 = math.sqrt(n21)
print(max(1,2,3))
print(min(1,2,3))
print(n22,n23,n24,n25,n26,int(n27))
#String Slicing
n28 = "Hello World!"
n29 = n28[0:5]
print(n29)
n30 = n28[0:12:2]
print(n30)
n31 = n28[::-1]
print(n31)
n32 = "www.google.com"
n33 = slice(4,-4)
print(n32[n33])
#if,elif,else
n34 = int(input("Try To Enter Number From 1 - 10 = "))
if n34 % 2 == 0:
    print("Number Is Even")
elif n34 % 2 != 0:
    print("Number Is Odd")
else:
    pass
#logical operators
if n34 % 2 == 0 and n34 <= 10 and n34 >= 1:
    print("The Number Is Even")
elif n34 % 2 != 0 or n34 == 7:
    print("The Number Odd And Maybe Equal To Seven!")
else:
    print("Enter Valid Even Number Between 1 - 10")
#loops
n35 = 1
while n35 < 3:
    n35 = n35 +1
    print(n35)
print("Hey You Made It!")
n36 = ""
while len(n36) == 0:
    n36 = input("Hey, How Are Ya? : ")
for n37 in range(1,21,2):
    print(n37+1)
for n38 in "James Bond":
    print(n38)
#Time Function/Module
print("Time Func:-")
for n39 in range(10,0,-1):
    print(n39)
    time.sleep(0.5)
print("March 7th Is Yummy!")
#Nested Loops
n40,n41,n42 = 10,6,"%"
for n43 in range(n40):
    for n44 in range(n41):
        print(n42, end = " ")
    print()
#Loop Control Statemnets
for n45 in range(1,10):
    if n45 == 7:
        pass
n46 = "0302-2256341"
for n47 in n46:
    if n47 == "-":
        continue
    print(n47, end="")
while True:
    n48 = input("Enter Name = ")
    if n48 != "":
        break
#index operator []
n49 = "yy Bro !"
if n49[0].islower():
    n49 = n49.capitalize()
print(n49)
n50 = n49[0:2].lower()
n51 = n49[3:6].upper()
n52 = n49[-1]
print(n50,n51,n52)
#Functions
def holo(age,height):
    print("My Name Is Holo, I Am A Wolf! I Am "+str(age)+" Years Old And I Am  "+str(height)+" Feet Tall.")
holo(height = 5,age = 18)
print(float(input("Enter A Number = ")))
#*args
def gojo(*args):
    n54 = 0
    #args = list(args)
    for n53 in args:
        n54 += n53
        print(n53)
    return n54
print(gojo(1,2,3,4,5))
#**kwargs
def yuji(**kwargs):
        print(kwargs["a"] + "Joe Mama" + kwargs["b"])
        for  key,value in kwargs.items():
            print(value,end=" ")
yuji(a = "Sup,", b = "Yum")
#str().format
n55 = "{} Barack Obama {}"
n56 = "That"
n57 = "Is A Bitch!"
n58 = "{0} Joe Biden {1}"
n59 = "The Fat {animal} Jumped On The {item} "
n60 = 1000
n61 = 3.125112
print(n55.format(n56,n57))
print(n58.format(n56,n57))
print(n59.format(animal = "Cow", item = "Bed!"))
print("{:.2F}".format(n61))
print("{:b}".format(n60))
print("{:o}".format(n60))
print("{:x}".format(n60))
print("{:e}".format(n60))
print("{:,}".format(n60))
#Random Numbers
n62 = random.randint(6,17)
print(n62)
n63 = random.random()
n64 = ["Rock","Papers","Sccissors"]
n65= random.choice(n64)
print(n65)
random.shuffle(n64)
print(n64)
#Exception Handling
try:
    n66 = int(input("enter a number = "))
    n67 = int(input("enter a second number = "))
    n68 = n66/n67
except ValueError:
    print("Error: User Did Not Enter A Integer(Number)")
except ZeroDivisionError as e:
    print("Value Cannot Be Divided By Zero", print(e)  )
except Exception:
    print("Find The Error Yourself!")
else:
    print(n68)
finally:
    print("This Statement Will Always Execute!")
#os module(formatting files and directories)
n70 = "rana.txt"
n71 = "cod_points"
if os.path.exists(n70):
    print("The File Is In The Directory")
else:
    print("File Not Found!")
if os.path.isfile(n70):
    print("The Given Path {} Is For A File".format(n70))
if os.path.isdir(n71):
    print("The Given Path {} Is For A Directory".format(n71))
with open(n70, "r") as file:
    n72 = file.read()
    print(n72)
    file.close()
with open(n70, "w") as file:
    n74 = input("Do You Want To Overwrite This File (y / n) =  ")
    if n74 == "y":
        n73 = file.write(",Poopee")  # DANGEROUS(USED FOR OVERWRITING)
print("File Written Successfully")

#appending files
with open(n70, "a") as file:
    n75 = input("Do You Want To Append This File {}? y/n".format(n70))
    if n75 == "y":
        n70 = file.write("This Text Is Appended")
print("File Appended Successfully")
#copying files via shutil
n76 = "test.txt"
n77 = "testcopy.txt"
n78 = input("Do You Want To Copy The File: {}? (y/n) = ".format(n76))
if n78 == "y":
    shutil.copyfile(n76, n77)
    print("File Is Copied!")
#moving files
n79 = "cod_points/testcopy.txt"
try:
    shutil.move(n77, n79)
    print("File May Have Been Moved")
except Exception:
    print("File Not Found!")
'''
n80 = "testcopy.txt"
try:
    os.remove(n80)
except Exception:
    print("File Not Found!")
#
#shutil.rmtree() = removes full folders
#os.rmdir() = removes empty folders


