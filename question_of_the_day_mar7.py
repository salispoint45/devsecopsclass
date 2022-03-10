#write some code that randomly picks a price from your price list (9.42, 5.67, 3.25, 13.40, 7.50) and prints True if the price is greater than 10 or false if its not.
price = [9.42, 5.67, 3.25, 13.40, 7.50]
import random
random.choice(price)


price_list = random.choice(price)
if price_list > 10:
    print(True)
else:
    print(False)

#You are provided with the following list ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']. Write code to print True if the following items ['bread', 'rice', 'okra', 'water', 'egusi'] are found in the list. Can you do this with a for loop?
list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
list1 = ['bread', 'rice', 'okra', 'water', 'egusi']
if list == list1:
    print(True)
else:
    print(False)

#Write a for loop that prints every letter in the phrase "Blood-oxygenation level dependent functional magnetic resource imaging"
phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
for i in phrase:
print(i)

#Create a grocery list. Now use a for loop to print the words "Note to self, buy" and the grocery item.
list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
for i in list:
    print('Note to self,buy', i)

#Now create a for loop that prints a numbered list of your grocery items.
list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
for i, item in enumerate(list,1):
    print(i,"." + item, sep="")

#Evidently your favorite snack is more important than anything else in your grocery list. Modify the last exercise to stop if and when it finds your favorite snack in your grocery list.
list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
favorite_snack = 'egusi'
for i in list:
if i == favorite_snack:
   break
print(i)

#Use the string split method, to segment all the words in the phrase ""Blood-oxygenation level dependent functional magnetic resource imaging" using a for loop.
phrase = "Blood-oxygenation level dependent functional magnetic resource imaging"
i = phrase.split()
 print(i)

#Use the range method to write a for loop to print out a numbered grocery list. if you have not created a groucery list, create it.
 print(i)

#Use enumerate to print out a numbered grocery list. if you don't have a grocery list, create one
list = ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']
for i, item in enumerate(list,1):
    print(i,"." + item, sep="")
#Use enumerate to print out a numbered grocery list. if you don't have a grocery list, create one.