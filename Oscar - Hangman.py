import random
guesses_left = 10
"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item form the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition

"""
Word_Bank = ["You did it", "Avengers", "Jurassic World", "California", "Google", "USA", "Hangman", "Password",
             "PyCharm", "Super Bowl"]

word = random.choice(Word_Bank)

letters_guessed = []

guess = ""
while guess != guesses_left > 0:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    if output == list(word):
        print("You Win!")
        win = True
    guess = input("Guess a letter")
    letters_guessed.append(guess)
    print(letters_guessed)
    if guess not in word:
        guesses_left -= 1
    print("You have %s guess left" % guesses_left)
