# list: it is like an array in other languages
INT = [1, 2, 55, 99]
FLOAT = [0.1, 1.1, 2.5, 3.2]
CHAR = ['a', 'B', 'c', 'D']
mix_data = ['Allyan', 22, 5.3, 'L']
# Printing
print(INT)
print(FLOAT)
print(CHAR)
print(mix_data)
# printing lenth & type
print(type(INT))
print(len(INT))
# slicing or making sublist
print(INT[0:3])
# methods os list
print("\nMethods")
INT.append(69)
INT.sort()
print(INT)
INT.sort(reverse = True)
print(INT)

# Tuple is immutable(the value cannot be chang at any index) & and diff. is only from list is the "()"
print("\nTuples")
tup_int = (1, 2, 5, 9, 0) #if we want to make single value tuple it should have "," after the value e;g
tup_int2 = (1,) #other wise it is consider as int value
print(tup_int)
print(type(tup_int))