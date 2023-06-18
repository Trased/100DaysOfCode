import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
computer = random.randint(1,100)
pick = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if pick == "easy":
  attempts = 10
else:
  attempts = 5
  
while attempts > 1:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > computer:
    print("Too high.\nGuess again.")
    attempts -= 1
  elif guess < computer:
    print("Too low.\nGuess again.")
    attempts -= 1
  else:
    print(f"You got it! The answer was {computer}")
    break
if attempts == 0:
  print(f"You've run out of guesses, you lost! The number was {computer}")
