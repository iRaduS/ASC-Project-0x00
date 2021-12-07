"""
# Parola poate contine doar cifre si litere mari / mici ale alfabetului
"""
from string import ascii_letters, digits
password_contents = ascii_letters + digits # "A-Za-z0-9"

with open('output', 'rb') as outputFile, open('input.txt', 'rb') as inputFile:
    outputFileBytes = bytearray(outputFile.read())
    inputFileBytes = bytearray(inputFile.read())

    """
    # Daca parola are dimensiunea maxima de 15 caractere vom face 2 ciclii (vom parcurge primele 30 de caractere)
    # pentru a ne asigura ca se repeta aceleasi caractere din parola
    """
    for i in range(0, 30):
        for letter in password_contents:
            if (outputFileBytes[i] ^ ord(letter)) == inputFileBytes[i]:
                print(letter, end="")
