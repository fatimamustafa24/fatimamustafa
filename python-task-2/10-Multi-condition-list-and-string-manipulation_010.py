'''
Question: Given a list of three strings and a target string, perform the following: If the target 
string’s length is equal to the length of the second list element, and the target string’s first 
character matches the first character of the first list element, print a new string combining the 
target string and the third list element with a space. If the lengths match but the first characters 
don’t, print "Length match only". If the lengths don’t match but the first characters do, print "First 
char match only". Otherwise, print "No conditions met". 
Example Input:target = "cake"my_list = ["cat", "deer", "fox"] 
Expected Output:cake fox 
'''
target = "cake"
my_list = ["cat", "deer", "fox"]

# Check conditions
length_match = len(target) == len(my_list[1])
first_char_match = target[0] == my_list[0][0]

if length_match and first_char_match:
    print(target + " " + my_list[2])
elif length_match:
    print("Length match only")
elif first_char_match:
    print("First char match only")
else:
    print("No conditions met")
