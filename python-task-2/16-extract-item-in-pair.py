'''Hard Difficulty Questions 
16. Combine Two Lists Alternately 
Given two lists of numbers, create a new list by alternating elements from both lists. Assume 
both lists have exactly 3 elements each. 
Example Input: 
list1 = [1, 3, 5] 
list2 = [2, 4, 6] 
Expected Output: 
[1, 2, 3, 4, 5, 6]'''
list1 = [1, 3, 5] 
list2 = [2, 4, 6] 
combined = [item for pair in zip(list1, list2) for item in pair]
print(combined)