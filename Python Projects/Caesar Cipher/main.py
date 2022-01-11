def encrypt(plain_text, shift_amount):
  res = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = (position + shift_amount)%len(alphabet)
      res += alphabet[new_position]
    else:
      res+=letter
  print(f"The encoded text is {res}")

def decrypt(txt,shift):
  res=""
  for letter in txt:
    if letter in alphabet:
      res+=alphabet[(alphabet.index(letter)-shift+len(alphabet))%len(alphabet)]
    else:
      res+=letter
  print(f"The decoded text is {res} ")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running=True
while running:
  direction=""
  while direction!="encode"and direction!="decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction=="encode":
    encrypt(text,shift)
  else:
    decrypt(text,shift)
  
  rerun=input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  if rerun=="no":
    running=False
print("Goodbye!")


