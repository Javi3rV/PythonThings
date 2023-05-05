# count char occurrences in a book
def charFileCount(file):
    file = open(file, mode="r", encoding="utf-8")
    data = file.read()
    found = []
    for letter in data:
        if letter not in found:
            found.append(letter)
            print(letter, " -> ", data.count(letter))

if __name__ == "__main__":
    charFileCount("CharFrequency in a book/frankenstein.txt")