# from random import sample 
import random



def start_game():
    print('\n')
    print('Welcome to The Mystery Word Game!\n')
    
def difficulty_level():    
    print('Please choose your difficulty level:')
    difficulty_choice = input('(E)asy (N)ormal (H)ard\n')

    while difficulty_choice[0].upper() not in ["E", "N", "H"]:
        difficulty_choice = input("Please select E, N, or H\n")
        
    return difficulty_choice[0].upper()

def select_word_length(difficulty_choice):
    word_length = 0
    E = [4, 5, 6]
    N = [6, 7, 8]
    H = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    if difficulty_choice == "E":
        word_length = random.choice(E)
    if difficulty_choice == "N":
        word_length = random.choice(N)
    if difficulty_choice == "H":
        word_length = random.choice(H)
    return word_length

def choose(word_length):
    word = []
    with open("words.txt") as words_file:
        for w in words_file.readlines():
            if len(w.strip()) == word_length: 
                word.append(w.strip())
                chosen_word = (random.choice(word)).lower()
    return chosen_word

def show_word_thus_far(word_choice,guesses):
    for char in word_choice:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_", end=" ")
    print('\n')

def is_win(word_choice,guesses):
    for char in word_choice:
        if char not in guesses:
            return False
    return True

if __name__ == "__main__":
    start_game()
    difficulty = difficulty_level()
    print('You selected ' + difficulty)
    print('\n')
    word_length = select_word_length(difficulty)
    print('Starting a game with ' + str(word_length) + ' letters')
    word_choice = choose(word_length)
    # print('The word selected is ' + word_choice)
    guesses = []
    wrong_guesses = []
    while (len(wrong_guesses) < 8):
        print("You've made " +  str(len(wrong_guesses)) + ' wrong guesses')
        print(wrong_guesses)
        show_word_thus_far(word_choice,guesses)
        letter_choice = input("Please select a letter\n")
        letter_choice = letter_choice[0].lower()
        if letter_choice in word_choice:
            guesses.append(letter_choice)
        else:
            wrong_guesses.append(letter_choice) 
        if is_win(word_choice,guesses):
            break

    if is_win(word_choice,guesses):
        show_word_thus_far(word_choice,guesses)
        print('You won!')
    else:
        print('The word selected was ' + word_choice)