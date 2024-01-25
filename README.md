# Guess The Random

Guess The Random (GTR from now on) is a single player game where you can enjoy hours of gameplay against the computer.

## At the start of each game the computer chooses a random number which it keeps a secret. The `secret_number` stays constant throughout the game.

`secret_number = get_random_number()`

## Each turn:

### On the start of each turn the computer generates a new temporary random number.

`temporary_number = get_random_number()`

### It adds the `temporary_number` to the `secret_number` and gives the player the result as a `hint`.

`hint = secret_number + temporary_number`

### After getting the `hint`, the player tries to guess the computer's `secret_number` and the turn ends.

`guess = int(input(f"Hint: {hint}\nEnter guess: "))`

### The game ends and the player wins once they guess the `secret_number` correctly. 

All numbers are assumed to be in the range of `-limit` to `limit`, where `limit` can be infinite.

```python
import time
import random

LIMIT = 10**9
get_random_number = lambda limit=LIMIT: random.randint(-limit, limit)

start_time = time.time()
secret_number = get_random_number()

while True:
  temporary_number = get_random_number()
  hint = secret_number + temporary_number

  guess = int(input(f"Hint: {hint}\nEnter guess: "))

  if guess == secret_number:
    print(f"Congrats! You guessed the secret number in only {time.time() - start_time} seconds!")
    break
```

[A strategy to win](SOLUTION.md)

[POC for correctly guessing the `secret number`](guess_the_random.py)
