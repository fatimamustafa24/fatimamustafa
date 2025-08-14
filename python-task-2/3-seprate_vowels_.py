'''
3. Count vowels in a string 
Question: Given a string, count the number of vowels (a, e, i, o, u, case-insensitive) in it and 
print the count. Use string indexing and conditions to check each character. Assume the string is 
short enough to check manually without loops. 
Example Input:text = "hello" 
Expected Output:2
'''
text = "hello"
vowels = "a,e,i,o,u,A,E,I,O,U"
count = 0
if text[0] in vowels:
    count += 1
if text[1] in vowels:
    count += 1
if text[2] in vowels:
    count += 1
if text[3] in vowels:
    count += 1
if text[4] in vowels:
    count += 1
print(count)
