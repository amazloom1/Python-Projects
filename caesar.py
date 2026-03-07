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
