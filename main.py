import random

limit = int(input("Enter the high end of the number range: "))
random_num = random.randint(1, limit)
guess = int(input("What is your guess: "))
print("")
total = 4

while guess != random_num:
  if guess > random_num and total > 0:
    total -= 1
    print(f"Number of guesses left: {total + 1}")
    guess = int(input("Too high, guess again: "))
    print("")
    
  elif guess < random_num and total > 0:
    total -= 1
    print(f"Number of guesses left: {total + 1}")
    guess = int(input("Too low, guess again: "))
    print("")

  elif guess != random_num and total < 1:
    print("better luck next time")
    print(f"The number was: {random_num}")
    break


if guess == random_num:
  print("Correct!")
    