n = int(input('enter any positive number '))

n1 = 1
while n1<=10:
    print(n, ' x ', n1, ' = ',n*n1)
    n1+=1
    
lis = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for is used for only to print sequence or search *(tuple, list, string)
# for variable_name in *()
for num in lis:
    if num == 4:
        print(num)
    