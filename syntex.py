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