### The second player can win (?)

It may seem counterintuitive, but the second player can end the game and win.

All they need to do is use the average of all of the `hints` they've heard so far as their `guess`. 


### Guessing with the average is all you need (?)

The simplest way to explain why it's a good idea to use the average of all the `hints` as the `guess` is  
that sometimes the `hint` will be above the `secret_number` and sometimes it will be below.

The probability that a `hint` will be above is equal to the probability it will be below (disregarding the limit problem), so loosely speaking it cancels out.



### This is mathematically legit (?)

The more mathematical explanation is that according to [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers) the more turns the game takes,  
the closer the average of the `hints` will get to the [*expected value*](https://en.wikipedia.org/wiki/Expected_value) of a `hint`.

The *expected value* of a hint is calculated as  
$` E(hint) = E(v_0, v_1, v_2, ... v_n, p_0, p_1, p_2, ... p_n)  =  ( sum_{i=0}^{n} p_i * v_i ) / n `$

where $v_i$ are each of the possible values the hint can take  
and $p_i$ the probability that $v_i$ will occur.

Since the probability $p_i$ for each value $v_i$ is equal to any other value $v_j$ (disregarding the limit problem), we can replace $p_i$ with some constant dx giving  
$` E(hint) = ( sum_{i=0}^{n} v_i * dx ) / n =  dx * ( sum_{i=0}^{n} v_i ) / n `$  

Since $v_i$ is the sum of the `secret_number` s and some `temporary_number` t we can replace $v_i$ giving  
$` E(hint) = dx * ( sum_{i=0}^{n} (s+t_i) ) / n `$  

We can seperate the sum into two sums giving  
$` E(hint) = dx * (  sum_{i=0}^{n} s + sum_{i=0}^{n} t_i  ) / n = dx * sum_{i=0}^{n} s / n + dx * sum_{i=0}^{n} t_i / n `$  

Since $t_i$ takes on all values from `-limit` until `limit` the second sum equals 0  
$` E(hint) = dx * sum_{i=0}^{n} s / n + dx * 0 / n = dx * sum_{i=0}^{n} s / n = dx * s `$  




### The limit problem

The closer the `secret_number` gets to the `limit`, the less numbers there are above it
