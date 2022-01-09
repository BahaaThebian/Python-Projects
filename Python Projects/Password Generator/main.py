#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letterCount=nr_letters
symbolCount=nr_symbols
numbersCount=nr_numbers
result=""
for i in range(0,nr_letters+nr_numbers+nr_symbols):
  if letterCount==0 and symbolCount==0:
    choice=2
  elif letterCount==0 and numbersCount==0:
    choice=1
  elif symbolCount==0 and numbersCount==0:
    choice=0
  elif letterCount==0:
    choice=random.randint(1,2)
  elif symbolCount==0:
    choice=[0,2][random.randint(0,1)]
  elif numbersCount==0:
    choice=random.randint(0,1)
  else:
    choice=random.randint(0,2)
  if choice==0 and letterCount!=0:
    result+=letters[random.randint(0,len(letters)-1)]
    letterCount-=1
  if choice==1 and symbolCount!=0:
    result+=symbols[random.randint(0,len(symbols)-1)]
    symbolCount-=1
  if choice==2 and numbersCount!=0:
    result+=numbers[random.randint(0,len(numbers)-1)]
    numbersCount-=1
print(f"Here is your password: {result}")