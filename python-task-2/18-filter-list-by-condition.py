'''18. Filter List by Condition 
Given a list of numbers, create a new list containing only the numbers that are greater than 10 
and less than 50. Assume the list has at least 5 elements, and manually check each of the first 
5 elements. 
Example Input: 
numbers = [5, 15, 30, 60, 45, 20] 
Expected Output: 
[15, 30, 45, 20] 
'''
numbers = [5, 15, 30, 60, 45, 20]
filtered = []

if 5 > 10 and 5 < 50:
    filtered.append(5)
if 15 > 10 and 15 < 50:
    filtered.append(15)
if 30 > 10 and 30 < 50:
    filtered.append(30)
if 60 > 10 and 60 < 50:
    filtered.append(60)
if 45 > 10 and 45 < 50:
    filtered.append(45)
if 20 > 10 and 20 < 50:
    filtered.append(20)

print(filtered)
