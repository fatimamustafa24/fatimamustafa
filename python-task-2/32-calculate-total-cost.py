'''
32.Calculate the total cost of items after applying a 20% discount if the total is a multiple of 5. 
Print the final cost. 
Example Input: total_cost = 100Expected Output: 80.0
'''
total_cost = 100

if total_cost % 5 == 0:
    discounted_cost = total_cost * 0.8
    print(discounted_cost)
else:
    print(total_cost)
