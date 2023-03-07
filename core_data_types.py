#Core data types, such as integers, floats, strings, and lists, and how to declare and use variables of these types
#Control flow statements, such as if-else statements, loops, and switch statements
#Functions and function arguments, including keyword arguments and default values
#Passing functions as arguments, extracting multiple return values from functions (tuple unpacking)
#Built-in functions and modules, such as math, string, numpy, and random
#Python Standard Library modules, such as os, sys, and time
#Python data structures, such as dictionaries and tuples

#core data types
x1 =3
print(x1)#prints integer
print(type(x1))

x2 = 4.0
print(x2)
print(type(x2))

x3 = True
print(type(x3))

#Strings
#print('George') and print("George") are the same
#EX:
y = 10
#print(y + "Dollars") #this code line wilkl produce type error as y is int and "Dollars"is a string
print(str(y)+ " Dollars") #This is correct way to do it.

#TWO WAYS TO CREATE LISTS
example = list()#list constructor
example = []#brackets

primes = [2,3,5,7,11,13]
primes.append(17)
primes.append(19)
#>>>list is now [2,3,5,7,11,13,17,19]. Append added numbers to the end of list. In lists, order is everything, while in sets they are not
#primes[0] would access the first element in the list while primes[-1 will access the last and so on]
#SLICING EX: 
primes[2:5] #would output [5, 7, 11] beginning index is inclued but ended one is not
#IN PYTHON MULTIPLE DATA TYPES AND DUPLICATE VALUES CAN BE PUT INTO A LIST.
#Combining lists can be done with a plus sign but beware of order 

#Control flow statements
#If statement example
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("Its nice")
else:#will only print if both conditionals are not met
    print("Its cold")
print("Done")#will always print as it is outside of conditional

#WHILE LOOPS are useful for looping until a condition is ture but be careful as it can cause an infinite loop if not careful
red_light = True
while red_light:
    if red_light:
        print("WAIT")
    else:
        print("DRIVE")

#FOR LOOPS
for x in range(1,11):
    print(x)#prints 1-10

for x in reversed(range(1,11)):#reversed function iterates backwards from 10-1
    print(x)#now prints 10,9,8,7...

for x in range(1,11,3):#the third paramerter is the"step" so now the for loop will iterate how ever much the step says
    print(x)#now prints 1,4,7,10

#continue and break
for x in range(1,21):
    if x == 13:
        continue #will skip over this iteration
    elif x ==19:
        break #will cut the iteration at 18
    else:
        print(x)

#SWITCH STATEMENTS
def my_func(argument):
    switcher = {
        0:"first option",
        1:"second option",
        2:"third option",
    }
    return switcher.get(argument, "default")
print(my_func(2))#If number not in dictionary above is called it will just print default.

#FUNCTIONS -- USER DEFINED
def greet(name): #Just this line alone Initializes function called greet but will return error as there is no body. name parameter is the argument.
    print("Hello",name)#prints string and argument
    print("How do you do")

greet("Jack")#calls function above and returns two print statents with one with the argument "Jack"

#PASSING MULTIPLE FUNCTION ARGUMENTS
def add_numbers(n1, n2):
    result = n1 + n2
    return result #function terminates at return
number1 = 5.4
number2 = 6.7
result = add_numbers(number1, number2) #return value is assigned to result variable
print("The sum is", result)

#OTHER PYTHON FUNCTIONS --- BUILT IN
float()
int()
input()

#EX.
marks = [55, 64, 75, 80, 34]
length = len(marks)
print(length) #prints number of values in marks list

#Positional arguments ex.
def add_numbers(n1, n2): 
    sum = n1 + n2
    return sum
result = add_numbers(5.4)#This function returns a type error as add_numbers() missing 1 required positional argument: 'n2'
print(result)

#DEFAULT ARGUMENTS
#to fix this issue you can add DEFAULT VALUES
def add_numbers(n1 = 100, n2 = 150): 
    sum = n1 + n2
    return sum
result = add_numbers(5.4)#This function returns 155.4 as now n2 is now default at 150 and we have updated the n1 argument as 5.4
print(result)

#KEYWORD ARGUMENTS
def greet(name, message):
    print("Hello",name)
    print(message)
greet("Jack", "Whats going on?")
greet(message = "Howdy?", name = "Jill")#passes arguments by name, order does not matter because they are name-specified

#Making functions return multiple values with TUPLES
#Tuples can contain multiple values like a list but it is immutable(cannot modify value)
even_nums = (2, 4, 6)#initializes the tuple
print(type(even_nums))
a, b, c = even_nums #unpacks the tuple into multiple variables, a,b,c in that order.
second_num = even_nums[1]#You can access tuple elements using zero-indexing like a list

#Returning multiple values ex.
def raise_both(value1, value2):#Function that raises value1 to power of value2 andvice vers
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)#initializes tuple taking both new values

    return new_tuple
result = raise_both(2,3)
print(result)


#data structures - Dictionaries - ORDER DOES NOT MATTER WITHIN DICTIONARIES(NOT SORTED), You can only retrieve values with the key.
d= {"michael":765765, "mike":36767585, "kevin":656766756}
print(d)#prints entire dictionary
print(d["mikey"])#KeyError: 'mikey' because key is not in dictionary | NameError: name 'mikey' is not defined