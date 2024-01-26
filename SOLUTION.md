### The player can win (?)

It may seem counterintuitive, but the player can win and end the game.

All they need to do is use the average of all of the `hints` they've gotten so far as their `guess`. 


### Guessing with the average is all you need (?)

The simplest way to explain why it's a good idea to use the average of all the `hints` as the `guess` is  
that sometimes the `hint` will be above the `secret_number` and sometimes it will be below.

The probability that a `hint` will be above is equal to the probability it will be below (disregarding the limit problem), so loosely speaking it cancels out.



### This is mathematically legit (?)

The more mathematical explanation is that according to [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers) the more turns the game takes,  
the closer the average of the `hints` will get to the [*expected value*](https://en.wikipedia.org/wiki/Expected_value) of a `hint`.

The *expected value* of a random variable $X$ is 

$` E(X) = sum_{i=0}^{N} ( x_i * p(x_i) ) = x_0 * p(x_0) + x_1 * p(x_1) + ... + x_N + p(x_N) `$  

where $x_i$ is each of the possible values the variable $X$ can take  
and $p(x_i)$ is the probability of $x_i$ occuring.


The *expected value* is linear in addition so  

$` E(hint) = E(secret\_number + temporary\_number) = E(secret\_number) + E(temporary\_number) `$  


The `secret_number` is constant so it's *expected value* is `secret_number`  

$` E(secret\_number) = secret\_number `$

The *expected value* of a `temporary_number` (a random variable in the range `-limit` to `limit`) is calculated as  

$` E(temporary\_number) = sum_{i=0}^{2*limit+1} (v_i * p_i) `$ 

where $v_i$ is each of the possible values the `temporary_number` can take  
and $p_i$ is the probability that $v_i$ occurs. 

Since the probability $p_i$ of any $v_i$ occuring is equal to the probability $p_j$ of any $v_j$ occuring  

$` p_i = p_j = dx `$  

where dx is some constant.  

Since all probabilities are equal and constant  

$` E(temporary\_number) = sum_{i=0}^{2*limit+1} (v_i * dx)  = dx * sum_{i=0}^{2*limit+1} v_i `$  

But since $v_i$ takes on all the values from `-limit` to `limit`  

$` E(temporary\_number) = dx * sum_{i=0}^{2*limit+1} v_i = dx * (-limit + -(limit-1) + -(limit-2) + ... + 0 + ... + (limit-2) + (limit-1) + limit ) = 0`$  

Finally we see that the *expectation value* of a `hint` is  

$` E(hint) = E(secret\_number) + E(temporary\_number) = secret\_number + 0 = secret\_number`$

So according to the Law of large numbers the average of all the hints will approach the `secret_number` the more turns the game takes.

### The limit problem

The closer the `secret_number` gets to the `limit`, the less numbers there are above it
