from math import factorial

#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else: 
        return c 
print(max_num(32,12,4))   #multiple prints to test each outcome 
print(max_num(22,75,7))
print(max_num(2,12,40))





#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*args):
    result = 1
    for x in args:
        result = result * x
    return result

print(mult_list(5,3,7))
print(mult_list(12,12))
print(mult_list(1,2,2,2,1,))




#Write a Python function called rev_string() to reverse a string.
def rev_string(backwards):      #reversing a single string
    return backwards[::-1]

print(rev_string("testing testing"))

def rev2_string(*args):       #reversing a list of string objects
    return args[::-1]

print(rev2_string("python", "testing"))





#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(n, begining, end):
    if begining <= n and n <= end:
        return True
    else:
        return False

print(num_within(2,1,3)) #True
print(num_within(56,32,42)) #False




# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    for i in range(n):
        for j in range(n-i+1):

            print(end=" ") #left spacing

        for j in range (i+1):
            
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")  #end= is right spacing
        
        
        print() #creates new line


print(pascal(1))
print(pascal(6))








