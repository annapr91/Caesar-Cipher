from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)



def caesar(caesar_text, caesar_shift,caesar_direction):
    new_word = ''
    if caesar_direction == 'decode':
        caesar_shift *= -1
    for letter in caesar_text:
        if letter  not in alphabet:
            new_word += letter
        else:
            index = alphabet.index(letter)

            new_position = index + caesar_shift
            new_word += alphabet[new_position]

    print(f"The {caesar_direction} text is {new_word}")

should_continuo = True
while should_continuo:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26

    caesar(caesar_text = text, caesar_shift = shift, caesar_direction = direction)
    answer = input('Do you want to continue yes/no:\n')
    if answer == 'no':
        should_continuo = False
        print('Goodbye')
