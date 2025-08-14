'''33.Given a number of seconds, compute the number of minutes and remaining seconds. Print in 
the format "X minutes and Y seconds". 
Example Input: seconds = 125Expected Output: 2 minutes and 5 seconds
'''
seconds = 125
minutes = seconds // 60       # 125 divided by 60 = 2 minutes
remaining_seconds = seconds % 60  # 125 % 60 gives 5 seconds left
print(f"{minutes} minutes and {remaining_seconds} seconds")