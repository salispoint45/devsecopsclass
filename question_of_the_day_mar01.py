#Identify the type of each of the following variables and write it as a comment next to the variable
a = 299
b = 90.0
c = "145"
d = "\u0CA0_\u0CA0"
e = "True"
f = True
g = len('Sample')
h = 100**30
i = 1 >= 1
j = 30%7
k = 30/7
l = b + 7
m = 128 << 1
n = bin(255)
o = [k, l, m, n ]
p = len(o)

a = 299 #int
b = 90.0 #float
c = "145" # str
d = "\u0CA0_\u0CA0" #str
e = "True" # str
f = True # bool
g = len('sample') #int
h = 100**30 #int
i = 1 >= 1 #bool
k = 30/7 #float
m = 128 << 1 #int
n = bin(255) #str

#What value is at the end of the varialbe my_var at the end of these assignments. Add a comparison after the last statement
#in the form of my_val ==
my_var = 99
my_var += 11
my_var = str(my_var)
my_var *= 2
my_var = len(my_var)
my_var *= 4

my_var = 99
my_var += 11
my_var = str(my_var)
my_var *= 2
my_var = len(my_var)
my_var *= 4
my_var == 24

#Change the loop below so that it prints the numbers from 1 to 10
for i in range(9)
print(i)

for i in range(1, 11):
    print(i)

for in range(9):
    print(i)

#Save a copy of your favorite snack as a variable. Using that variable, print your favorite snack 100 times

favourite_snacks = "cookies"
print(favourite_snacks * 100)

#Make a list of your grocery items with prices 9.42, 5.67, 3.25, 13.40, 7.50 and store it as a variable. Using a builtin function, #find the cheapest and the most expensive items on your shopping list

grocery_price = [9.42, 5.67, 3.25, 13.40, 7.50]
print(max(grocery_price))

grocery_price = [9.42, 5.67, 3.25, 13.40, 7.50]
print(min(grocery_price))

#Import random. run dir(random.randint). Use Randint to randomly print between 0 and 100 copies of your favorite snack

import random
favourite_snacks = 'cookies'
print(random.randint(0, 100) * favourite_snacks)

#Run dir(random). Find a function in random that you can use to print a random item from your grocery list. Remember you can use #help to find out what functions do.
#Write code to randomly select items from your groceries list, round them to the nearest integer and print the result

grocery_price = [9.42, 5.67, 3.25, 13.40, 7.50]
random.choice(grocery_price)

abs(random.choice(grocery_price))

round(abs(random.choice(grocery_price)))

#Previously,we used the * operator to print a hundred copies of your favorite snack. This time use a while loop to print 50 copies of your favorite snack.
#Mix and Match! Write a while loop that uses the * operator to print multiple copies of your favorite snack per line. Print out 10 lines where the first line has one copy of your favorite snack and the last line hast 10.

favourite_snacks = "cookies"
count = 0
while count < 50:
    print(favourite_snacks)
    count += 1

count = 1
favourite_snacks = 'cookies'
while count <= 10:
    print(favourite_snacks * count)
    count += 1

#Challenge: Your neighborhood grocery store is having a weird promotion called "Win free change". A random item is picked from your #grocery list and you pay 10 dollars. If the item is less than 10 dollars, you get the item and the balance from the items price. If #the item is more than 10 dollars, you get the item and the difference in the price as change. Write the code to randomly pick a #price from your price list and print out the amount the cashier

import random
if random.choice(grocery_price) < 10:
    customer_price = random.choice(grocery_price)
    if customer_price < 10:
        print('cashier pay customer', 10 - customer_price)
    elif customer_price > 10:
        print('cashier pay customer', customer_price - 10)
    elif customer_price == 10:
        print('cashier tell customer to leave')
    else:
        print('what do you have in mind')