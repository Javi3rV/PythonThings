import nltk, time
nltk.download("punkt")
nltk.download("words")
nltk.download('cess_esp')
from nltk.tokenize import word_tokenize as wtokenize
import CaesarCipher as cCrypt
dict = "abcdefghijklmñopqrstuvwxyz"
wordListEng = set(nltk.corpus.words.words())
wordlistEsp = set(nltk.corpus.cess_esp.words())
text = input("Enter text to crack: ")
for key in range(len(dict)):
    resultText = cCrypt.decrypt(text, key)
    tokens = wtokenize(resultText)
    tokenCount = 0
    for token in tokens:
        if token in wordListEng or token in wordlistEsp:
            tokenCount += 1
    if tokenCount > 0:
        print("\nPossible key found! %d rotations --> Result: %s\n" % (key,resultText))
    else:
        print("Test #%d - Result: %s" % (key, resultText))
    time.sleep(0.25)
        