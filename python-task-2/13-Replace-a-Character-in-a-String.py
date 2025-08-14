'''13. Replace a Character in a String 
Given a string, replace all occurrences of a specific character with another character. Use string 
methods you’ve learned. 
Example Input: 
text = "cat hat mat" 
old_char = "a" 
new_char = "o" 
Expected Output: 
cot hot mot 
'''
text = "cat hat mat" 
old_char = "a" 
new_char = "o"
result = text.replace(old_char, new_char)
print(result)
