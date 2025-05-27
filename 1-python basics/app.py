##basic syntax rules in python
''' 
 1. case sensitivity- python is case sensitive
 2. python uses indentation to define blocks of code.
    consistent use of spaces or a tab is required
'''

name='krishna'
Name='shiva'

print(name)
print(Name)

age=233

if age>30:
    print(age)

## line continuation

total = 1+2+3+4+5+6+7+\
4+6+7
print(total)

##multiple statements on a single line

x=5;y=7;z=x+y
print(z)

#understanding semantics in python

#variable assignment
age = 32 ## age is a integer
n = 'jan'

print(age,n)

##type inference
print(type(age))
age=True
print(type(age))

##name error
#a=b