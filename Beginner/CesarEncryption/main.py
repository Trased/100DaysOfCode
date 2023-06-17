alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(text,shift,direction):
  if direction == "decode":
    shift = -shift
  modified_text = ""
  for letter in text:
    if letter not in alphabet:
      modified_text += letter
    else:
      position = alphabet.index(letter)
      modified_text+= alphabet[(position+shift)%len(alphabet)]
  print(modified_text)

redo = True
while redo:
  good = False
  while not good:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
      good = True
      cesar(text,shift,direction)
    else:
      print("Not a good selection")
  
  good = False
  while not good:
    check = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if(check == "no"):
      redo = False
      good = True
    elif(check == "yes"):
      redo = True
      good = True
    else:
      print("Not a good selection")
      
