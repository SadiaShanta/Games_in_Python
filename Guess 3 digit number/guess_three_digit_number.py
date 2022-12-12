import random

def generate_three_digit():
    mylist=["0","1","2","3","4","5","6","7","8","9"]
    random.shuffle(mylist)
    str=""
    for i in range(3):
        str=str+mylist[i]
    return str


def get_user_guess():
    digits=input('Enter 3 digit number: ')
    return digits


def clues(computer_code,user_guess):
    if computer_code==user_guess:
        print("Code Cracked")
    clues = []
    for i in range(3):
        if computer_code[i]==user_guess[i]:
            clues.append("match")
        elif user_guess[i] in computer_code:
            clues.append("Close")

    if clues==[]:
        return ["Nope"]
    else:
        return clues

print("Welcome to guess 3 digit number!")
secret_code= generate_three_digit()
clue=[]
while clue!="Code Cracked":
    guess= get_user_guess()
    clue_report=clues(secret_code,guess)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)