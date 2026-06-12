## lambda map function 
def square(num):
    return num ** 2

nums = [1,2,3,4,5]
for num in nums:
    print(square(num))

#above execution with lambda map
sqrs = list(map(square,nums))
print(sqrs)


def check_len(str):
    if len(str) % 2 == 0:
        return 'EVEN'
    else:
        return str[0]

names = ['Jagan','Jaya','Swecha']
n = list(map(check_len,names))
print(n)


## lambda filter function, returns only bool value
#### FILTER
################
def check_even(num):
    return num % 2 == 0

nums = [1,2,3,4,5,6]
print(list(filter(check_even,nums)))


## LAMBDA functions
nums = [1,2,3,4,5,6]

def square(num):
    return num ** 2

print(list(map(square,nums)))

# the above def square could be converted into
def square(num): return num ** 2

print(list(map(square,nums)))

#further converted into
square = lambda num : num ** 2

print(square(5))

print(list(map(square,nums)))

# Now, below is lambda expression 
# square = lambda num : num ** 2 
# this could be used in conjuction with map or filter functions.
squared_nums = list(map(lambda num : num **2, nums)) 
print(squared_nums)

first_letter_in_names = list(map(lambda name : name[0], names))
print(first_letter_in_names)

even_nums = list(filter(lambda num : num % 2 == 0, nums))
print(even_nums)
 




