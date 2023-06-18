import art
from replit import clear
import random

def deal_card():
  return random.choice(cards)

def calculate_score(list):
  score = 0
  for i in list:
    if(i == 11):
      if (score + i) > 21:
        index = list.index(11)
        list.remove(11)
        list.insert(index,1)
        score += 1
      else:
        score += i
    else:
      score += i     
  return score

def compare(user, calculator):
  if user > calculator :
    print("You won!")
  elif user == calculator:
    print("It's a draw!")
  else:
    print("You lost.")
    
def begin():   
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())
  user_cards.append(deal_card())
  user_cards.append(deal_card())

def user_playing(user):
  repeat = True
  while repeat:
    print(f"\tYour cards: {user_cards}, current score: {user}")
    print(f"\tComputer's first card: {computer_cards[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
      user_cards.append(deal_card())
      user = calculate_score(user_cards)
      if user > 21:
        return False
    else:
      repeat = False
      return True

def computer_playing(computer):
  repeat = True
  while repeat:
    if computer < 17:
      computer_cards.append(deal_card())
      computer = calculate_score(computer_cards)
      if computer > 21:
        return False
    else:
      repeat = False
      return True


if __name__ == "__main__":
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  computer_cards = []
  redo = True
  while redo:
    print(art.logo)
    begin()
    user = calculate_score(user_cards)
    computer = calculate_score(computer_cards)
    if user_playing(user):
      if computer_playing(computer):
        print(f"\tYour cards: {user_cards}, final score: {user}")
        print(f"\tComputer's final hand: {computer_cards}, final score:  {computer}")
        compare(user, computer)
      else:
        print("Opponent went over. You won!")
    else:
      print("You went over. You lost.")
    
    pick = input("Do you want to play another Blackjack game? type 'y' or 'n'")
    if(pick == 'n'):
      redo = False
    else:
      clear()
      user_cards = []
      computer_cards = []
