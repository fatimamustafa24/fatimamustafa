'''19. Split String into List 
Given a string of words separated by commas, create a list of the words, removing any leading 
or trailing spaces from each word. 
Example Input: 
19. Split String into List 
Given a string of words separated by commas, create a list of the words, removing any leading 
or trailing spaces from each word. 
Example Input: 
text = "apple, banana,  orange ,grape" 
Expected Output: 
['apple', 'banana', 'orange', 'grape'] 

'''
text = "apple, banana,  orange ,grape"
words=text.split(",")
filter = [word.strip() for word in words]
print(filter)