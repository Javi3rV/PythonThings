import random

options = [0,1,2]
translator = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}
robot = random.randint(0,2)
try:
    user = int(input("""
    0. Rock
    1. Paper
    2. Scissors
    
    Choose an option (0-2, 0 by default): """))
    if user < 0 or user > 2:
        print("Enter a number between 0 and 2")
        exit()
    if user == robot:
        print("""
    Tie!""")
    elif options[robot] == options[user-1]:
        print("""
    You win!""")
    else:
        print("""
    You lose!""")
    print("""
    Machine: {0}
    You: {1}""".format(translator[robot], translator[user]))
except ValueError:
    print("Enter a number between 0 and 2")