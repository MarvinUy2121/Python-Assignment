'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
letter=input().lower()
shift=int(input())
def shift_letter(letter,shift)
letter_total= 26
alphabet_list = [chr(i) for i in range(97, 123)]
for letters in alphabet_list:
    if letter == letters:
        index=alphabet_list.index(letters)
        shifted_letter= int(index)+ int(shift)
        if shifted_letter <= letter_total:
            print(alphabet_list[shifted_letter])
        else:
            wrapped_letter= shifted_letter - letter_total 
            print(alphabet_list[wrapped_letter])
    elif:
        letter == " "
        print(" ")
    else:
        print("Please input a valid letter")

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
message=str(input())
shift=int(input())
def caesar_cipher(message, shift):
    cipher_text = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text
    print(cipher_text)
caeser_cipher(message,shift)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
letter = input().lower()
shift = input().lower()

def shift_letter(letter, shift):
    letter_total = 26
    alphabet_list = [chr(i) for i in range(97, 123)]

    for shift_letters in alphabet_list:
        if shift == shift_letters:
            shift_index = alphabet_list.index(shift_letters)
            break 

    for letters in alphabet_list:
        if letter == letters:
            index = alphabet_list.index(letters)
            shifted_letter = index + shift_index
            if shifted_letter <= letter_total:
                print(alphabet_list[shifted_letter])
            else:
                wrapped_letter = shifted_letter - letter_total 
                print(alphabet_list[wrapped_letter])

shift_letter(letter, shift)

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
message=str(input())
key= str(input())
def vigenere_cipher(message, key):
    message = message.upper()
    key = key.upper()

    message = message.replace(" ", "")

    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]

    alphabet_list = [chr(i) for i in range(65, 91)]

    result = ""

    for i in range(len(message)):
        message_letter = message[i]
        key_letter = key[i]
        message_index = alphabet_list.index(message_letter)
        key_index = alphabet_list.index(key_letter)
        shifted_index = (message_index + key_index) % 26
        result += alphabet_list[shifted_index]

    return result
vigenere_cipher(message,key)