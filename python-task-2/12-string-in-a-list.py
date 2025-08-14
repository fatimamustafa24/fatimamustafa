'''
12. Check if a String is in a List 
Given a list of strings and a target string, check if the target string is present in the list. Print 
"Found" if it is, otherwise print "Not Found". 
Example Input: items = ["apple", "banana", "orange"] 
target = "banana"
Expected Output: 
Found 
'''
items = ["apple", "banana", "orange"] 
target = "banana"
if target in items:
    print("Found")
else:
    print("Not Found")
