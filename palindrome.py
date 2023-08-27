text = input("Enter a text: ")
text = text.replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
if text == text[::-1]:
    print("It's a palindrome!")
else :
    print("It's not a palindrome")