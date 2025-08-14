'''
15. Check String Prefix and Suffix 
Given a string, check if it starts with "Py" and ends with "n". Print "Both" if both conditions are 
true, "Prefix only" if it starts with "Py", "Suffix only" if it ends with "n", or "Neither" if neither 
condition is true. 
Example Input: 
text = "Python" 
Expected Output: 
Both
'''

text = "Python" 
if text.startswith("Py") and text.endswith("n"):
    print("Both")
elif text.startswith("Py"):
    print("Prefix only")
elif text.endswith("n"):
    print("Suffix only")
else:
    print("Neither")
