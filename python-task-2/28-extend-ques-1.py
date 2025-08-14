'''28. extend() 
Extends the list by appending elements from another list. 
Question 1 :Extend a list of fruits with another list of tropical fruits and print the updated list. 
Sample Input:fruits = ["apple", "banana"]tropical = ["mango", "pineapple"] 
Sample Output:["apple", "banana", "mango", "pineapple"] 
'''
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)
