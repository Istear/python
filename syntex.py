import keyword
#white space and indentation
def addSeries():
    i=0
    max=10
    while(i<max):
        print(i)
        i=i+1

addSeries()

#Continuation of statements
a=True
b=False
c=True
if (a == True) and (b == False) and \
   (c == True):
    print("Continuation of statements")

# Identifiers are names that identify variables, functions, modules, classes, and other objects in Python.

# The name of an identifier needs to begin with a letter or underscore (_). The following characters can be alphanumeric or underscore.

# Python identifiers are case-sensitive. For example, the counter and Counter are different identifiers.

# In addition, you cannot use Python keywords for naming identifiers.
    
print('Python keywords')

print(keyword.kwlist)

# String literals
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)

#variable
first_variable=0
second_variable=0
variable = 1

# string
message = 'This is a string in Python'
print(message)
message = "This is also a string"
print(message)
message = "It's a string"
print(message)
message = '"Beautiful is better than ugly.". Said Tim Peters'
print(message)
message = 'It\'s also a valid string'
print(message)
message = r'C:\python\bin'
print(message)
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)

name = 'John'
message = f'Hi {name}'
print(message)

greeting = 'Good ' 'Morning!'
print(greeting)

greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

str = "Python String"
print(str[0]) # P
print(str[1]) # y

str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

str = "Python String"
str_len = len(str)
print(str_len)

#The str[0:2] returns a substring that includes the character from the index 0 (included) to 2 (excluded).
str = "Python String"
print(str[0:2])

#When want to modify a string, you need to create a new one from the existing string. For example:
str = "Python String"
new_str = 'J' + str[1:]
print(new_str)

#for string
# In Python, a string is a series of characters. Also, Python strings are immutable.
# Use quotes, either single quotes or double quotes to create string literals.
# Use the backslash character \ to escape quotes in strings
# Use raw strings r'...' to escape the backslash character.
# Use f-strings to insert substitute variables in literal strings.
# Place literal strings next to each other to concatenate them. And use the + operator to concatenate string variables.
# Use the len() function to get the size of a string.
# Use the str[n] to access the character at the position n of the string str.
# Use slicing to extract a substring from a string.

