#Decalaration arugments
def add(a, b):
    return a + b

print(add(15,18))#Passing arguments by position

#Specified Arguments
#Used for more than teo arguments to define the value while passed.print

def increment(number, by):
    return number +by 

print(increment(2, by=1)) #Passing arguments by specified name

#Default Arguments 
#When the value for the argumnets is fixed such that we can set a default value for the argument

def increment(number, by=1):
    return number + by

print(increment(2,5)) 