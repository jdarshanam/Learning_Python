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



