from replit import clear
import random
import hangman_word_list as hg
import hangman_art as art
print(art.logo)
chosen_word = random.choice(hg.word_list)
display = []
lives = 6
for i in range(len(chosen_word)):
  display.append("_")

print(f"{' '.join(display)}")

missing_letters = True
alive = True
guessed = []
while missing_letters and alive:
  print(art.stages[lives])
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in guessed:
    print(f"You already guessed the letter {guess}")
  else:
    guessed += guess
    
  correct = False
  iter = 0
  for letter in chosen_word:
    if guess == letter:
      display[iter] = letter
      correct = True
    iter = iter + 1
  
  print(f"{' '.join(display)}")
  if not correct:
    print("Wrong!")
    lives -= 1

  if not lives:
    print(art.stages[lives])
    print("You lost!")
    alive = False

  if "_" not in display:
    missing_letters = False
    print("Wow! You guessed the word correctly !")

  print(f"You guessed: {' '.join(guessed)}")

