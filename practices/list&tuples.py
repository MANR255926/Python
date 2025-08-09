# save movies in list from user
movies = []
movies.append(input("enter movies: "))
movies.append(input("enter movies: "))
movies.append(input("enter movies: "))
print(movies)
# find palindrome in a list
palin =[]
palin.append(input("enter a list of index 1: "))
palin.append(input("enter a list of index 2: "))
palin.append(input("enter a list of index 3: "))
palin.append(input("enter a list of index 4: "))
palin.append(input("enter a list of index 5: "))
word_copy = palin.copy()
word_copy.reverse()

print('\noriginal list: ',palin)
print('reverced list: ',word_copy)

if(palin == word_copy):
    print('\npalindrome')
else:
    print('\nnot palindrome')
# count no. of A in a tup & sort them from A to D in a list
grad_tup = ('C','D', 'A','A', 'B', 'B', 'A')
print(grad_tup.count('A'))
grad_list = ['C','D', 'A','A', 'B', 'B', 'A']
grad_list.sort()
print(grad_list)