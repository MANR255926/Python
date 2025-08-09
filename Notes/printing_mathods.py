# concatenation
str0 = input("enter string: ")
str1 = input("enter string: ")
f_str = str0 + str1
print ('allyan'+'nadeem') # all of these give same answer -> print (str0 + str1), print (f_str)
print (str0 + ' ' + str1)

# length function
print (len(str0),len(str1))

# slicing OR making substring
print(str0[1 : 4])
#print by -ve sing oder
print (str0[-6:-1])

#other functions for printing:
print(str0.capitalize(),str1.capitalize())
print(str1.count("a"))