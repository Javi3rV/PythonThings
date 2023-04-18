email = input("Introduce un email: ")
contArroba = 0
for letter in email:
    if letter == "@":
        contArroba += 1

def emailDomain(email):
    domain = ""
    for index, letter in email:
        if letter == "@":
            domain = email[index+1:]
    return domain
def domainTLD(domain):
    tld = "err"
    if domain.count(".")==1:
        for index, letter in domain:
            if letter == ".":
                if len(domain[index+1:]) in range(2,4):
                    tld = domain[index+1:]

    return tld



if contArroba == 1 and domainTLD(emailDomain(email)) != "err":
    print("El email parece correcto")
else:
    print("El email no parece correcto")

