email = input("Introduce un email: ")
contArroba = 0
for letter in email:
    if letter == "@":
        contArroba += 1


if contArroba == 1:
    print("El email parece correcto")
else:
    print("El email no parece correcto")
