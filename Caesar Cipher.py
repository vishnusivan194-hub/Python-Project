alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text,shift_amount,encode_decode):
    cipher_text=""
    if direction=='decode':
            shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text+=letter
        else:
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position%=len(alphabet)
            cipher_text+=alphabet[shifted_position]
    print(f'Your {direction}d text is {cipher_text}')
should_continue=True
while should_continue:
    direction=input('Type if you want to decode or encode :').lower()
    text=input('Enter the text you want to encode or decode :').lower()
    shift=int(input('Enter the amount you want to shift :'))
    caesar(original_text=text,shift_amount=shift,encode_decode=direction)

    restart=input('Type yes if you want to continue or type no to discontinue :').lower()
    if restart=='no':
        print('Goodbye')
        break



    



