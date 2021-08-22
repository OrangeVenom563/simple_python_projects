letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def caesar(start_text, shift_amt, direction):
    end_text = ''
    if direction == 'decode':
        shift_amt *= -1
    for letter in start_text:
        position = letters.index(letter)
        if position+shift_amt > 36:
            position = shift_amt - (36-position)
        else:
            position += shift_amt

        end_text += letters[position]
    print(end_text)


opr = input('Enter "encode" to encrypt "decode" to decrypt: ')
message = input('Enter the message to encrypt: ').lower()
shift = int(input('Enter the shift amount: '))
shift %= 36
caesar(start_text=message, shift_amt=shift, direction=opr)
