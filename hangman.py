""" 
Hangman game made by Anh Đức
Github profile: https://github.com/anhduc261209
"""
# import modules
import random
import time
# Variables
global words, chosenword, lives, guess, guessList
words = ['python', 'c#', 'c++', 'c', 'java', 'html', 'css', 
        'javascript', 'php', 'visualbasic', 'typescript', 'rust', 'scheme',
        'kotlin', 'perl', 'scala', 'swift', 'sql', 'r', 'go', 'ruby', 'f#',
        'fortran', 'assembly', 'delphi', 'pascal', 'objectivec', 'lua',
        'lisp', 'ada', 'cobol', 'basic', 'haskell', 'matlab', 'octave']
chosenword = random.choice(words)
lives = 9
guess = ''
guessList = [''] * len(chosenword)
# function that display hangman
def printHangman(lives):
    no = 9 - lives
    if no == 1:
        print('_')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 2:
        print('_________')
        print('|        ')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 3:
        print('_________')
        print('|       |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 4:
        print('_________')
        print('|       |')
        print('|       O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 5:
        print('_________')
        print('|       |')
        print('|       O')
        print('|       |')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 6:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 7:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|')
        print('|')
        print('|')
        print('|')
    elif no == 8:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|      /')
        print('|')
        print('|')
        print('|')
    elif no == 9:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|      / \\')
        print('|')
        print('|')
        print('|')

# Main prograd
def main():
    
    print('Welcome to this amazing game - Hangman!')
    time.sleep(2)
    print("In this game, you have to guess a word about programming languages")
    time.sleep(2)
    print(f"The word has {len(chosenword)} characters and the first character is {chosenword[0]}!")

    # Loop until the player lose or win
    while ''.join([str(char) for char in guessList]) != chosenword:
        # print the underscores
        for i in range(len(guessList)):
            if guessList[i] != chosenword[i]:
                print('_', end = ' ')
            elif guessList[i] == chosenword[i]:
                print(chosenword[i], end = ' ')
        # Move the cursor to a new line
        print()
        done = False
        # Get the input character from the player
        guess = str(input("Guess a letter or the word: ")).lower()
        if guess == chosenword:
            print(f"You win! The word is {chosenword}!")
            break
        elif len(guess) > 1:
            print("You can only guess 1 character!")
        elif len(guess) < 1:
            print("You have to guess at least 1 character!")
        elif guess in guessList:
            print('You already guessed that character!')
        else:
            # Check if the guessed character is in the word
            for x in range(len(chosenword)):
                if guess == chosenword[x]:
                    if done == False:
                        print('The character you guessed is in the word :)')
                    guessList[x] = guess
                    done = True
            if done == False:
                print("The character you guessed is not in the word :((")
                lives -= 1
                printHangman(lives)
        # Check if the player lose
        if lives == 0:
            print(f"You ran out of lives :(( The word is {chosenword}")
            break
        # Check if the player wins
        if ''.join([str(char) for char in guessList]) == chosenword:
            print(f"You win! The word is {chosenword}!")
            break
    # check if want to play again
    playAgain = ''
    while playAgain != 'y' and playAgain != 'n':
        playAgain = str(input("Do you want to play again? (Y, n) ")).lower()
        if playAgain == 'y': main()
        elif playAgain == 'n': break
        else: print('Invalid response!')

if __name__ == '__main__':
    main()



