from random_words import RandomWords

rw = RandomWords()
word = rw.random_word()  # Creating a random word


print("Welcome to hangman! The current word is " + str(
    len(word)) + " letters long! You will have six guesses to get it right!")
guesses = 0
win = False
solved_letters = ""
correct_letters = []
for letter in word:  # Creating a list that is the same length as the random word but filled with _ spaces to show correct guessed letter
    correct_letters.append("_")


def play_game():
    global guesses
    already_guessed = ""
    initiate_game = input("Would you like to play? y/n ")
    if initiate_game == "y".casefold():
        display_board()
        while guesses < 6:
            if win:
                break
            guess = input("Please guess a letter: ")
            if len(guess) > 1:  # Making sure the user can only guess one letter at a time
                print("You can only guess one letter!")
            elif guess not in word and guess not in already_guessed:  # Checking if user incorrectly guesses a letter not yet guessed and adding one to the counter
                guesses += 1
                already_guessed = already_guessed + guess  # Storing all the previously guessed letters
                display_board()
                print("Here is what you already guessed: " + already_guessed)
                print("".join(correct_letters))
            elif guess in already_guessed:  # If user guesses a letter that they have already guessed
                print("You already guessed that!")
            elif guess in word:  # If the user correctly guesses a letter in the hidden word
                display_board()
                for i in range(len(word)):  # To display all the letters they have guessed correctly
                    if word[i] == guess:
                        correct_letters[i] = guess
                print("".join(correct_letters))

            game_win()

        else:  # Game loss if no more turns
            display_board()
            print("You lose! The word was " + word)



def display_board():  # Print out board corresponding to how many wrong guesses
    if guesses == 0:
        print("+-------+")
        print("|")
        print("|")
        print("|")
        print("|")
        print("=======")
    elif guesses == 1:
        print("+-------+")
        print("|       O")
        print("|")
        print("|")
        print("|")
        print("=======")
    elif guesses == 2:
        print("+-------+")
        print("|       O")
        print("|       |")
        print("|")
        print("|")
        print("=======")
    elif guesses == 3:
        print("+-------+")
        print("|       O")
        print("|       |")
        print("|      /")
        print("|")
        print("=======")
    elif guesses == 4:
        print("+-------+")
        print("|       O")
        print("|       |")
        print("|      / \\")
        print("|")
        print("=======")
    elif guesses == 5:
        print("+-------+")
        print("|      \O")
        print("|       |")
        print("|      / \\")
        print("|")
        print("=======")
    elif guesses == 6:
        print("+-------+")
        print("|      \O/")
        print("|       |")
        print("|      / \\")
        print("|")
        print("=======")


def game_win():  # Check if game won by seeing if there are no more _ in the correct letters list
    global win
    if "_" not in correct_letters:
        win = True
        print("You got it! The word was " + word)


play_game()
