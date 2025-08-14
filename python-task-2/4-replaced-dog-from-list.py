first occurrence with "Replaced" and print the modified list. If the target is not in the list, print "No 
change". 
Example Input:my_list = ["cat", "dog", "bird"]target = "dog" 
Expected Output:['cat', 'Replaced', 'bird'] 
'''
my_list = ["cat", "dog", "bird"]
my_list[1] = "Replaced"

print(my_list)