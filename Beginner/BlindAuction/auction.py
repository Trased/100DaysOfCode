from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print (art.logo)
print("Welcome to the secret auction program.")
repeating = True
bidders = {}
while repeating:
  name = input("What is your name?: ")
  bid = int(input("What's your bid? $"))
  bidders[name] = bid
  repeat = input("Are there any other bidders? Type 'yes' or 'no'")
  if repeat == "no":
    repeating = False
  clear()

max_bid = 0
name = ""
for check in bidders:
    if bidders[check] > max_bid:
      name = check
      max_bid = bidders[check]

print(f"The winner is {name} with a bid of ${max_bid}")
