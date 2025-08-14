'''
38.Given a total number of items, calculate how many groups of 4 can be formed and how many 
items are left over. Print in a sentence: "You can form X groups with Y items left over". 
Example Input: items = 17Expected Output: You can form 4 groups with 1 item left over 
'''
items = 17
groups = items // 4
leftover = items % 4

print(f"You can form {groups} groups with {leftover} items left over")
