import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
userChoice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpuChoice=random.randint(0,2)
drawings=[rock,paper,scissors]
decisionList=[["draw","lose","win"],["win","draw","lose"],["lose","win","draw"]]
decision=decisionList[userChoice][cpuChoice]
print(drawings[userChoice])
print(f"Computer chose:\n{drawings[cpuChoice]}")
print(f"You {decision}")