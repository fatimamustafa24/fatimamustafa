'''14. Compare List Lengths 
Given two lists of numbers, compare their lengths and print "First is longer" if the first list is 
longer, "Second is longer" if the second list is longer, or "Equal length" if they have the same 
length. 
Example Input: Example Input: 
list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7] 
Expected Output: 
First is longer 
'''
list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7] 
if len(list1) > len(list2):
    print("First is longer")
elif len(list1) < len(list2):
    print("Second is longer")
else:
    print("Equal length")
