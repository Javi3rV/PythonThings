import re
import random

dict = "abcdefghijklmnñopqrstuvwxyz1234567890#$%&_-.,"
while True:
    while True:
        try:
            passLength = float(input("Introduce la longitud de la contraseña: "))
            break
        except:
            print("Por favor sigue los formatos (numero)")
    while True:
        try:
            numAmount = float(
                input("Introduce la cantidad de numeros de la contraseña: "))
            break
        except:
            print("por favor sigue los formatos (numero)")
    while True:
        try:
            symAmount = float(
                input("Introduce el numero de simbolos de la contraseña: "))
            break
        except:
            print("por favor sigue los formatos (numero)")
    if numAmount+symAmount<=passLength:
        break
    else:
        print("numeros y simbolos suman mas caracteres que la contraseña")

# rellenar de letras
passwd = ""
while len(passwd) < passLength:
    if random.randint(0, 1) == 1:
        passwd += random.choice(dict[:27])
    else:
        passwd += random.choice(dict[:27]).upper()

# agregar numeros
passwd = list(passwd)
while len(re.findall("[0-9]", "".join(passwd)))<numAmount:
    randPos = random.randint(0, passLength-1)
    if not passwd[randPos] in dict[27:37]:
        passwd[randPos] = random.choice(dict[27:37])

# agregar simbolos
while len(re.findall("[#$%&/_-]", "".join(passwd)))<symAmount:
    randPos = random.randint(0, passLength-1)
    if not passwd[randPos] in dict[27:37]:
        passwd[randPos] = random.choice(dict[37:])

print("".join(passwd))
