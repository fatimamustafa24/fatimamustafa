'''
37.Given a list of three numbers, check if the sum of their leftovers when divided by 3 equals the 
leftover of their sum when divided by 3. Print "Equal" or "Not Equal". 
Example Input: numbers = [4, 7, 10]Expected Output: Equal
'''
numbers = [4, 7, 10]

# Step-by-step calculation
num1 = numbers[0] % 3
num2 = numbers[1] % 3
num3 = numbers[2] % 3

# Sum of individual numbers, then take mod 
sum_of_numbers = (num1 + num2 + num3) % 3

# Total sum of numbers, then take mod 3
total_sum_numbers = sum(numbers) % 3

# Comparison
if sum_of_numbers == total_sum_numbers:
    print("Equal")
else:
    print("Not Equal")
