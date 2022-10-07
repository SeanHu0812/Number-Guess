import random
print("Rounds to play")
round = int(input())
answer = random.randint(0,10)
print("The number is between 0 and 10");
for i in range(round):
  print("Enter your guess")
  guess = int(input())
  if guess == answer:
    print("Congradulation you guessed the right answer!")
    break
  print("Not correct! Guess again")
print("Ahh bad luck!")
