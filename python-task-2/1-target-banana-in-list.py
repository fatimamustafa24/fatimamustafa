'''
1. Check if a string is in a list 
Question: Given a list of strings and a target string, check if the target string exists in the list and 
print "Found" if it does, or "Not Found" if it doesn’t. 
Example Input:my_list = ["apple", "banana", "orange"]target = "banana" 
Expected Output:Found
'''
my_list = ["apple", "banana", "orange"]
target = "banana"
if target in my_list:
    print("found")
else:
    print("not found")