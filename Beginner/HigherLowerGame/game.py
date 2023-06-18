from game_data import data
from replit import clear
import art
import random


score = 0
A = random.choice(data)
B = random.choice(data)
repeat = True
while repeat:
  clear()
  print(art.logo)
  while A == B:
    B = random.choice(data)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} ")
  print(art.vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']} ")
  pick = input("Who has more followers? Type 'A' or 'B': ")
  correct_pick = A['follower_count'] > B['follower_count']
  if (pick == "A" and correct_pick == 1) or (pick == "B" and correct_pick == 0):
    score += 1
    if correct_pick == 1:
      B = random.choice(data)
    else:
      A = B
      A = random.choice(data)
      
  else:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong! Final score: {score}")
    repeat = False


