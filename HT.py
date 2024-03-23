from random import choice

chosen = choice(["Rock", "Paper", "Scissors"])
your_choice = input("Write your choice: ")
print(chosen)

if (chosen == "Rock" and your_choice == "Paper") or \
   (chosen == "Paper" and your_choice == "Scissors") or \
   (chosen == "Scissors" and your_choice == "Rock"):
    print("You won")
elif (your_choice == "Rock" and chosen == "Paper") or \
     (your_choice == "Paper" and chosen == "Scissors") or \
     (your_choice == "Scissors" and chosen == "Rock"):
    print("Computer won")
else:
    print("Draw")
