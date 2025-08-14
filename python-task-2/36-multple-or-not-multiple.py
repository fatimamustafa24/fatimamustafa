'''
36.Given two numbers, check if their sum is a multiple of their difference. Print "Multiple" or "Not 
Multiple". 
Example Input: num1 = 15, num2 = 5 Expected Output: Multiple 
'''
num1 = 15
num2 = 5
sum = num1 + num2 
diff= num1 - num2
if sum % diff == 0:
    print("multiple")
else:
   print("not multiple")