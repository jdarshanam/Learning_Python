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
f = open('abc.text',mode='w')
f.write("Initial line")
f.close()



