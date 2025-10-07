import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'',t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','*','$']

print('Welcome to the Password Generator')
no_of_letters=int(input('How many letters do you want in your password :'))
no_of_symbols=int(input('How many symbols do you want in your password :'))
no_of_numbers=int(input('How many numbers do you want in your password :'))

password=''

for i in range(1,no_of_letters+1):
    ran_letters=random.choice(letters)
    print(ran_letters)
    password+=ran_letters
for i in range(1,no_of_symbols+1):
    ran_symbols=random.choice(symbols)
    print(ran_symbols)
    password+=ran_symbols
for i in range(1,no_of_numbers+1):
    ran_numbers=random.choice(numbers)
    print(ran_numbers)
    password+=ran_numbers
print(f'Your password is {password}')
