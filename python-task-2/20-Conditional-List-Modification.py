'''20. Conditional List Modification 
Given a list of numbers, create a new list where each element is doubled if it is even, or tripled if 
it is odd. Assume the list has exactly 4 elements. 
Example Input: 
numbers = [1, 2, 3, 4] 
Expected Output: 
[3, 4, 9, 8
'''
numbers = [1, 2, 3, 4]
result = [x * 2 if x % 2 == 0 else x * 3 for x in numbers]
print(result)
