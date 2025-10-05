print('welcome to treasure island')
print('your mission is to find the treasure')
c1=input('you are at a crossroad ,where do you want to go?  "left" or "right" :')
if c1=="left":
    c2=input('You have come to a lake . Do you wanna swim to go across or wait for boat. Type "swim" or "wait" :')
    if c2=="wait":
        c3=input('You have arrived in an island . There are 3 doors which door are you choosing? Red,Green or Yellow :')
        if c3=='Red':
            print('Room is full of fire . Game over')
        elif c3=='Green':
            print('room is full of poisonous gases . Game over')
        elif c3=='Yellow':
            print('You win, you found the treasure!')
        else:
            print('The door doesnt exists . Game over')
    else:
        print('you got attacked by a bunch of crocodiles')
        
else:
    print('you fell in a hole , Game over')
