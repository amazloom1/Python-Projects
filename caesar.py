# Caesarian cipher encryption
# Take in message
# Take in shift number
# Move message by shift number
# Output encrypted message


# from collections import deque

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l',
#            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

def cShift(c, shift):
    return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))


def encrypt(shift, message):
    newString = ''
    for char in message:
        if char.isalpha():
            char = char.lower()
            shifted = cShift(char, shift)
            newString += shifted
        else:
            newString += char
    return newString


print(encrypt(3, 'hello'))
