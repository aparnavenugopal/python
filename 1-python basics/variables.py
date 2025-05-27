# variables
'''
variables are fundamental elements in programming used to 
store data that can be referenced and manipulated in a program
'''

a=100
# declaring and assign variables

age=32
height=6.1
name="krishna"
is_student = True

print(age, height, name, is_student)

#naming convention
'''
1. naming conventions
2. variable names should be descriptive
3.they must start with a letter or an '_' and contains 
  letters, numbers, and underscores
4.variables names are case sesnitive
'''

#valid variable names

first_name = 'nana'

#invalid variable anmes

#2get =30
#first-name='krish'
#@name='krish'

#understanding variable types
'''
1.python is dynamically typed, type of a variable is 
  determined at runtime
   a. int
   b.float
   c.str
   d.bool
'''

#type checking and conversion

type(height)
age=24
print(type(age))
age_str =str(age)
print(type(age_str), age_str)
name='krish' #cant convert into int or float type

#dynamic typing
#python allows the type of  variable to change as the
#as program executes

var=10
print(var, type(var))

var = 3.14
print(var, type(var))

#input

age = int(input('what is your age'))
print(age, type(age))