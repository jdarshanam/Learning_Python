x = 0.1
y = 0.2

if (x + y) == 0.3:
    print("0.1 + 0.2 EQUAL TO 0.3")
else:
    print("0.1 + 0.2 NOT EQUAL TO 0.3")

print(1/2)
print(3**3)
print(3^3)


print("Hello world"[8])

# list
print("\n\n####### list #########")
l = [1,2,3]
print(l)
print(f"list pop - {l.pop()}") # list pop removes always last element.
print(l)


#set (mutable) & frozenset (immutable)
print("\n\n####### set #########")
s = {"as",11,21,3,3,3,3.0,3.0001}
print(f"multiple occurance of element 3 (including 3.0) in set is ignored - {s}")
s.add(4)
print(s)
print(f"set pop - {s.pop()}") # set pop removes arbitary value, based on hash value of the element.
print(s)

safe_set = {1, "hello world", 3,5.6}
print(f"safe_set - {safe_set}")

try:
    unsafe_set = {1,2.4,[22,33]}
    #print(f"unsafe_set -{unsafe_set}") #cannot use 'list' as a set element (unhashable type: 'list'). because list would be growing, thus hash changes, thus impacts set structure.
except TypeError as error:
    print(f"Error: {error}")

print("\n\n####### frozenset #########")
try:
    fs = frozenset({1,2,3})
    print(fs)
    print(fs.add(4)) #'frozenset' object has no attribute 'add'
except AttributeError as e:
    print(f"exception - {e}")

print("\n\n####### dictionary #########")
week_dict = {0:'Sunday',1:'Monday'}
print(f"week_dict - {week_dict}")
print(f"dictionary keys - {week_dict.keys()}")
print(f"dictionary values - {week_dict.values()}")
print(f"dictionary items (keys & values as dict_items) - {week_dict.items()}")

print("\n\n####### tuples #########")
t = (1,1,2,3,2,2,2,22.5,"sunday",[22,3])
print(f"tuple t - {t}")
try:
    print(f"tuple element occurance count - {t.count(2)}")
    print(f"tuple element 'sunday' index - {t.index('sunday')}")
    print(f"tuple element index - {t.index('Not in the tuple')}")
except ValueError as ve:
    print(f"ValueError - {ve}")

print("\n\n####### files #########")
f = open('../abc.text',mode='w')
f.write("Initial line")
f.close()

print("\n\n####### string #########")
st = "Print only the words that start with s in this Sentence"
for w in st.split(" ") :
    if w[0].lower() =='s' :
        print(w)

for w in st.split(): print(w) if w[0].lower() == 's' else None

print("\n\n####### range #########")
print(f"even numbers upto 10 {list(range(0,10+1,2))}")

print("\n\n####### string #########")
def myfunc(*args):
    return sum(args)

print(myfunc(10,20,30))

def myfunc(*args):
    return [arg for arg in args if arg % 2 == 0]

print(myfunc(1,2,3,4,5,6))

def myfunc(st):
    result = []
    for index, e in enumerate(st):
        if index % 2 == 0:
            result.append(e.upper())
        else:
            result.append(e.lower())
    return "".join(result)

print(myfunc("Anthropomorphism"))

def summer_69(nums: list) -> int:
    total = 0
    add = True
    for num in nums:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1,2,3,4,5,6,7,8,9,10]))

#solution-I
def spy_game_007(nums: list) -> bool:
    only_zeros_seven = []
    for num in nums:
        if num in [0,7]:
            only_zeros_seven.append(num)
    print(f"only_zeros_seven - {only_zeros_seven}")
    str_only_zeros_seven = "".join(str(n) for n in only_zeros_seven)
    print(f"str_only_zeros_seven - {str_only_zeros_seven}")
    if '007'in str_only_zeros_seven:
        return True
    else:
        return False    


#print(spy_game_007([1, 2, 4, 0, 0, 7, 5,1, 2, 4, 0, 0, 7, 5]))  # Returns True
#print(spy_game_007([1, 0, 2, 4, 0, 5, 7]))  # Returns True
#print(spy_game_007([1, 7, 2, 0, 4, 5, 0]))  # Returns False

#solution-II
def spy_game_007_sol_2(nums: list) -> bool:
    code = [0,0,7]
    for num in nums:
        if num == code[0] :
            code.pop(0)
    
        if not code: # code list is empty, means we noticed pattern
            return True
        
    return False
    
print(spy_game_007_sol_2([1, 2, 4, 0, 0, 7, 5,1, 2, 4, 0, 0, 7, 5]))  # Returns True
print(spy_game_007_sol_2([1, 0, 2, 4, 0, 5, 7]))  # Returns True
print(spy_game_007_sol_2([1, 7, 2, 0, 4, 5, 0]))  # Returns False

#Solution-I
def count_primes(num: int) -> int:
    if num < 2:
        return 0
    
    # 2 or greater
    #list to store our prime numbers
    primes = [2]
    # Counter going upto input num
    x = 3

    while x < num:
        #check if x is prime
        for y in range(3,x,2): # step 2 , because we are interested only odd numbers, as evens are divisible by 2.
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(f"primes - {primes}")
    return len(primes)
print(count_primes(100))

#Solution-II
def count_primes_improved(num: int) -> int:
    if num < 2:
        return 0
    
    # 2 or greater
    #list to store our prime numbers
    primes = [2]
    # Counter going upto input num
    x = 3

    while x < num:
        #check if x is prime
        for y in primes: # step 2 , because we are interested only odd numbers, as evens are divisible by 2.
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(f"primes - {primes}")
    return len(primes)

print(count_primes_improved(100))

#Solution-III
def count_primes_fast(num: int) -> int:
    if num < 2:
        return 0

    primes = [2]
    x = 3

    while x <= num:
        # Only check against primes we've already found, up to sqrt(x)
        for p in primes:
            if p * p > x:  # Past the square root? It's prime!
                primes.append(x)
                break
            if x % p == 0:  # Divisible by a prime? Not prime!
                break
        x += 2

    print(f"primes - {primes}")
    return len(primes)
print(count_primes_fast(100))

