Does this work as long as the hint is a linear function?  
If the `hint = secret_number + temporary_number ^ 2`:   
Calculating the expected value of a random variable X^2 gives twice the sum of squares until the `limit`.  
But if `hint = secret_number + temporary_number ^ 3` we again get the expectation value of hint is secret.    
This shows that this works even when the hint is non-linear.  

As long as the _values_ of the hint have a symmetric distribution the expected value will be 0,  
otherwise it should approach some constant which depends on `limit`.  



Any given turn gives us little to no information, but the collection of turns gives us almost complete information.

It's interesting to note that this implies that the mean of random numbers zigzags narrowly around 0 (somewhat approaches 0), but the sum of those numbers zigzags widely around 0.  
This is because the calculation for the mean includes a division by the amount of numbers which always grows,  
while the calculation for the sum may vary widely between iterations.  
Whenever the sum is 0 the mean must also be.  

The limit can be said to be behavioural/statistical rather than being mathematically assured, since we can't assert that we'll be done by any given turn.  


Think of randomly generating text from the alphabet "-+0123456789" and evaluating it as a mathematical expression.  



