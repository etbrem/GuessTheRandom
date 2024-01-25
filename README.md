# Guess The Random

The game is played between two players.

Before the game starts, the first player chooses a random number which he keeps a secret. The `secret number` stays constant throughout the game.

On the start of each turn the first player generates a new temporary random number. He adds the `temporary number` to his `secret number` and tells the second player the result as a `hint`.

After hearing the `hint`, the second player tries to guess the first players's `secret number` and the turn ends.

The game ends once the second player guesses the `secret number` correctly. 

All numbers are assumed to be in the range of `-limit` to `limit`, where `limit` can be infinite.


[A strategy for the second player](SOLUTION.md)

[Code which simulates the game and (usually) ends with the second player correctly guessing the `secret number`](guess_the_random.py)
