''' Extend a list of numbers with another list of even numbers and print the updated 
list. 
Sample Input:numbers = [1, 3, 5]evens = [2, 4, 6] 
Sample Output:[1, 3, 5, 2, 4, 6]
'''
numbers = [1, 3, 5]
evens = [2, 4, 6]
numbers.extend(evens)
print(numbers) 
