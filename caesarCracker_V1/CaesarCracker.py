import CaesarCipher as cCrypt
dict = "abcdefghijklmnñopqrstuvwxyz"
englishDict = open("caesarCracker_V1/englishDict.txt", "r", encoding="utf-8", errors="ignore").read().replace("\n", " ").split()
spanishDict = open("caesarCracker_V1/spanishDict.txt", "r", encoding="utf-8").read().replace("\n", " ").split()
text = input("Text to crack: ")
found = 0
for key in range(len(dict)):
    testResult = cCrypt.decrypt(text, key)

    tokens = []
    token =""
    if len(testResult)<4:
        limit = 2
    else:
        limit = 4
    for index, letter in enumerate(testResult):
        token += letter
        if len(token)==limit:
            tokens.append(token)
            token = ""
        if len("".join(tokens))+limit > len(testResult):
            tokens.append(testResult[index:])
            break
    

    tokenCount = 0
    for token in tokens: 
        if "a".join(englishDict).count(token.strip())>3 or "a".join(spanishDict).count(token.strip())>3:
            tokenCount += 1
    if tokenCount > 2:
        print("\nPossible result found! -> Key: {0} rotations - Result: {1}\n".format(key, testResult))
        found += 1
    else:
        print("test {0} rotations - result: {1}".format(key,testResult))
if found == 0:
    print("\n---------Nothing apparently found, retrying-----------\n")
    for key in range(len(dict)):
        testResult = cCrypt.decrypt(text, key)

        tokens = testResult.split()
            

        tokenCount = 0
        for token in tokens: 
            if len(token)<3:
                continue
            if "a".join(englishDict).count(token.strip())>3 or "a".join(spanishDict).count(token.strip())>3:
                tokenCount += 1
        if tokenCount > 0:
            print("\nPossible result found! -> Key: {0} rotations - Result: {1}\n".format(key, testResult))
            found += 1
        else:
            print("test {0} rotations - result: {1}".format(key,testResult))

