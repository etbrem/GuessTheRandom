# Guess The Random

The game is played between two players.

### Before the game starts, the first player chooses a random number which they keep a secret. The `secret_number` stays constant throughout the game.

`secret_number = get_random_number()`

## Each turn:

### On the start of each turn the first player generates a new temporary random number.

`temporary_number = get_random_number()`

### They add the `temporary_number` to their `secret_number` and tell the second player the result as a `hint`.

`hint = secret_number + temporary_number`

### After hearing the `hint`, the second player tries to guess the first players's `secret_number` and the turn ends.

`guess = int(input("Enter guess: "), 0)`

### The game ends once the second player guesses the `secret_number` correctly. 

All numbers are assumed to be in the range of `-limit` to `limit`, where `limit` can be infinite.


[A strategy for the second player](SOLUTION.md)

[Code which simulates the game and (usually) ends with the second player correctly guessing the `secret number`](guess_the_random.py)
