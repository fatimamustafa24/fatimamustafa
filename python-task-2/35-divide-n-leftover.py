'''35.Given a number, print a sentence stating the result and leftover when divided by 7. 
Example Input: number = 23Expected Output: 23 divided by 7 gives result 3.2857 and leftover 2 
'''
number = 23
quotient, remainder = divmod(number, 7)
result = number / 7
print(f"{number} divided by 7 gives result {result:.4f} and leftover {remainder}")
