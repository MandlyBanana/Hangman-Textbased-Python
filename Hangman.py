from os import system
from words import words
import random
from colorama import Fore, init

# function to print everything on stage
def print_hangman(stage=0):
    print("     _______________")
    print("     ⎪    /        |")
    print("     ⎪   /         |")
    print("     ⎪  /          |")
    if stage == 0:
        print("     ⎪ /")
        print("     ⎪/")
        print("     ⎪")
        print("     ⎪")
    elif stage == 1:
        print("     ⎪ /          ( )")
        print("     ⎪/")
        print("     ⎪")
        print('     ⎪')
    elif stage == 2:
        print("     ⎪ /          ( )")
        print("     ⎪/            ‖ ")
        print("     ⎪")
        print('     ⎪')
    elif stage == 3:
        print("     ⎪ /          ( )")
        print("     ⎪/           /‖ ")
        print("     ⎪")
        print('     ⎪')
    elif stage == 4:
        print("     ⎪ /          ( )")
        print("     ⎪/           /‖\ ")
        print("     ⎪")
        print('     ⎪')
    elif stage == 5:
        print("     ⎪ /          ( )")
        print("     ⎪/           /‖\ ")
        print("     ⎪             ‖")
        print('     ⎪')
    elif stage == 6:
        print("     ⎪ /          ( )")
        print("     ⎪/           /‖\ ")
        print("     ⎪             ‖")
        print(r'     ⎪            /  ')
    elif stage == 7:
        print("     ⎪ /          ( )")
        print("     ⎪/           /‖\ ")
        print("     ⎪             ‖")
        print(r'     ⎪            / \ ')



    print('     ⎪')
    print("   ‾‾‾‾‾‾         ", end="")
    for i in word:
        if i in letters_lower or i in letters_higher:
            print(i, end="")
        else:
            print("▨ ",end="")
    print("")
    print("                   ____________")
    print("                   |", end="")
    a = 0
    for i in letter_print:
        if i.lower() not in word or i.upper() not in word:
            a += 1
            if a > 5:
                print("|")
                print("                   |", end="")
                print(f'{i.lower()}', end=" ")
                a = 1
            else:
                print(f'{i}', end=" ")
    
    for i in range(a, 5):
        print("", end="  ")
    print("|")
    print("                   ‾‾‾‾‾‾‾‾‾‾‾‾")

letters_higher = []
letters_lower = []
letter_check = []
letter_print = []
letters_staged = []
word = []
stage = 0
playing = True
inp = ""
amount_letters = 0
correct_guessed = 0
first = True

# finding a word from words list
rand = random.randint(0, len(words)-1)
temp = words[rand]
for i in temp:
    word.append(i)

amount_letters = len(word)







print(word)



while playing == True:
    
    system('cls')
    print("")
    

    print_hangman(stage)
    if stage == 7:
        playing = False
        print(f'{Fore.RED}You lost. :({Fore.WHITE}\n\n')
        print(f'The word was {word}')
        break
    
    if first == False:
        if inp.lower() in word or inp.upper() in word: #checks if user guessed letter correctly
            if inp.lower() not in letter_check and inp.upper() not in letter_check:
                print(f"\nYay you guessed the lettter {inp}!\n")
                letter_check.append(inp)
            else:
                print(f"You have already guessed {inp}.")
        else:
 #           if 
            print(f"The letter {inp} is not part of the word.")

    if len(letter_check) == len(word):
        print_hangman(stage)
        print(f"{Fore.YELLOW}You won!{Fore.WHITE}")
        playing = False
        break

    while True: #ask user for letter
        inp = input("Enter a letter to guess the word --> ")
        if len(inp) == 1:
            break
        else:
            print("\nPlease enter only 1 letter at a time.")

    if inp not in letters_lower and inp not in letters_higher: # checks if letter has already been guessed
        letters_lower.append(inp.lower())
        letters_higher.append(inp.upper())
        
        if inp.lower() not in word and inp.upper() not in word:
            letter_print.append(inp.lower())
            print(inp, "\n", letters_higher, "\n", letters_lower, "\n", letter_check)
    
    if inp.lower() not in word and inp.upper() not in word and inp.lower() not in letters_staged: #checks if user guessed letter correctly and adds a stage
        stage += 1
        letters_staged.append(inp.lower())
    first = False
    
#    input("asd")




"""
print("     ⎪ /          ( )")
print("     ⎪/           /‖\ ")
print("     ⎪             ‖")
print(r'     ⎪            / \ ')
"""