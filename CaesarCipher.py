dict = "abcdefghijklmnñopqrstuvwxyz"
def crypt(text, rots):
    text = list(text.lower())
    for index, letter in enumerate(text):
        if letter in dict:
            originalIndex = dict.index(letter)
            cipheredIndex = (originalIndex+rots) % len(dict)
            text[index] = dict[cipheredIndex]
    return "".join(text)
def decrypt(text, rots):
    text = list(text)
    for index, letter in enumerate(text):
        if letter in dict:
            cipheredIndex = dict.index(letter)
            originalIndex = cipheredIndex-rots
            text[index] = dict[originalIndex]
    return "".join(text)

opt = input("Encrypt or Decrypt? (E/D): ")
if opt.lower() == "e":
    try:
        text = input("Input text to encrypt: ")
        rots = int(input("Number of rotations: "))
    except:
        print("Something went wrong, please enter data correctly")
    print(crypt(text, rots))
elif opt.lower() == "d":
    try:
        text = input("Input text to decrypt: ")
        rots = int(input("Number of rotations: "))
    except:
        print("Something went wrong, please enter data correctly")
    print(decrypt(text, rots))
