def sum(a,b):
    return a + b

n1=int(input('enter number: '))
n2=int(input('enter number: '))

s = sum(n1,n2)
print('your sum is: ', s)

# function recursion/loop.
def show(n):
    if (n == 0): #stop condition.
        return
    print(n) 
    show(n-1) #calling function in side the function to making it loop.
    
show(5) #calling a function out side the function for user & giving it value.