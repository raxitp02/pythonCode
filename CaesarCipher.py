def init_fun(): # Initializes the program
  startup = input("Encode or decode with key or decode without key? (ed/dwok)\n> ").lower()
  if startup == "dwok": # "dwok" means decode without key.
    caesarCipher_hiddenkey_decode()
  elif startup == "ed": # "ed" means encode/decode.
    caesarCipher()
  else:
    print("It looks like you didn't input ed or dwok. Try again please.")
    startup_()

def isInt_fun(x):
  try:
    int(x)
    return True
  except ValueError:
    return False

def caesarCipher(): # Encodes or decodes with a key
  text = input("\nInput your message.\n> ")
  key = int(input("\nInput your integer key.\n> "))
  mode = input("\nEncode or decode?\n> ")
  alphabet = "abcdefghijlmnopqrstuvwxyz"
  newText = "" # text = list(text) is unnecessary here
  if mode == "decode": # Reverses the direction of the inputted shift
    key = -ke
    print("\nDecoding...\n")
  else:
    print("\nEncoding...\n")
    
  for char in range(len(text)):
    if text[char].isupper():
      alphabet = alphabet.upper()
    elif text[char].islower():
      alphabet = alphabet.lower()
    if text[char].isalpha() == False: # Exception for non-letters
      if isInt_fun(text[char]):
        newLetter = str((int(text[char]) + key)%10)
      else:
        newLetter = text[char]
    else:
      newLetter = alphabet[((alphabet.index(text[char])+key)%25)]
    newText += newLetter
  print("Result:", newText)

def caesarCipher_hiddenkey_decode(): # Decodes one step at a time with user input
  text = input("\nInput your message to decode.\n> ")
  alphabet = "abcdefghijlmnopqrstuvwxyz"
  key = 1
  not_done = ""
  while not_done == "":
    newText = ""
    print("\nDecoding...\n")
    for char in range(len(text)):
      if text[char].isupper():
        alphabet = alphabet.upper()
      elif text[char].islower():
        alphabet = alphabet.lower()
      if text[char].isalpha() == False:
        if isInt_fun(text[char]):
          newLetter = str((int(text[char]) - key)%10)
        else:
          newLetter = text[char]
      else:
        newLetter = alphabet[((alphabet.index(text[char])-key)%25)]
      newText += newLetter
    key += 1 # Iterate through all possible key values one step at a time.
    print("Result: " + newText)
    not_done = input("\nInput something if done.\n> ") # User can tell the script when to stop cycling.
  print("\nDone!\n\nThe final result is: " + newText)



init_fun() # Begins the script
