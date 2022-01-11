import random
import hangman_art 
import hangman_words

word_list=hangman_words.word_list
stages=hangman_art.stages
logo=hangman_art.logo
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
usedChars=""
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in usedChars and guess in chosen_word:
      print(f"You already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        if guess in usedChars:
          print(f"The word does not contain this letter, you already guessed {guess}")
        else:
          print("The word does not contain this letter.")
          lives -= 1
          if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    if guess not in usedChars:
      usedChars+=guess