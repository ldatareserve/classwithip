# if statements
a = 1 
b = 2
if a < b:
    print('A is less then B')

n = 1000
j = 100

if n > j:
    print('N is greater then J')


# if statement (more complex)
price = input('What is the monthly rent? ')
price = int(price)
if price > 800:
    fees = 125
    print(f'Your added fees amount to ${fees}')

option_tag = int(input('How much is the totality of car option prices? '))
if option_tag > 15000:
    reduction = 10
    print(f'Congratulations, you receive {reduction}% off.')


# else statements
y = 57
w = 92
if y > w:
    print('Y is greater than W')
else:
    print('Y is less then W')

u = 899
o = 324
if u < o:
    print('O is greater than U')
else:
    print('U is greater than O')



#  else statement (more complex)
price = input('What is the monthly rent? ')
price = int(price)
if price > 800:
    fees = int(125)
    print(f'Your added fees amount to ${fees}')
else:
    print('You have no added fees')

option_tag = int(input('How much is the totality of car option prices? '))
reduction = 10
reduction2 = 5
if option_tag > 15000:
    print(f'Congratulations, you receive {reduction}% off.')
else:
    print(f'Congratulations, you receive {reduction2}% off.')



# elif statement
r = 12
s = 12
if r < s:
    print('R is less than S')
elif r == s:
    print('R is equal to S')

f = 9
e = 10
if f == e:
    print('F is equal to E')
elif f < e:
    print('F is less then E')


# if, elif, else together
v = 600
z = 500
if v < z:
    print('V is less than Z')
elif v == z:
    print('V is equal to Z')
else:
    print('V is greater than Z')

n = 80
p = 45
if n > p:
    print('N is greater than P')
elif n == p:
    print('N is equal to P')
else:
    print('N is less than P')


# and operator
j = 500
t = 900
q = 400
if j > q and q < t:
    print('Both conditions are true')

k = 1200
l = 2000
m = 4700
if m > l and l > k:
    print('Both conditions are true')


# or operator
j = 500
t = 900
q = 400
if q > j or q < t:
    print('One of the conditions is true')

k = 1200
l = 2000
m = 4700
if m > l or k > m:
    print('One of the conditions is true')


# not operator
j = 500
t = 900
q = 400
if not j == q:
    print('It appears J is not equal to Q')

k = 1200
l = 2000
m = 4700
if not l < k:
    print('It appears L is not less than K')