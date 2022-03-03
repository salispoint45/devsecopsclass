# if we list all numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these numbers is 23.
# Write some code to find the sum of all  multiples of 3 and 5 between 0 and 1000.
# take in a number
def solution(number):
    # create a list to populate
    answers = []
    
    # loop through all numbers in the range
    for i in range(number):
        # if divisible by 3 or 5 and within range
        if (i%3==0 or i%5==0) and i<number and i>0:
            # add to the answers list
            answers.append(i)
        
    # return the sum of the answers
    return sum(answers)

#Write a python program to count the number of occuring characters in a given string.
#Sample String : google.com'

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'

def change_char(str1):  
  char = str1[0]  
  length = len(str1)  
  str1 = str1.replace(char, '$')  
  str1 = char + str1[1:]  
  
  return str1  
  
print(change_char('restart'))  

#Given the following list, list1 = [100, 200, 300, 400, 500], reverse the list
#expected result: [500, 400, 300, 200, 100]

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#so if given:
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#Expected output should be: ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# Write a Python program to iterate over dictionaries using for loops.

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)