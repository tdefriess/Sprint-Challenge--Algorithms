#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
set a equal to zero
loop while a is less than n cubed
    set a equal to a plus n squared

This function will have O(n) runtime complexity because it is performing n ^ 3 as
repeated addition of n ^ 2. In order for a to become greater than n ^ 3, it will need to add 
n ^ 2 to itself n times.


b)
Initialized accumulator variable sum as 0. Loop through using iterator i to do the following:
(Re)initialize j as 1, then while j is less than n, double the value of j and record one time through the loop
in sum.

This function is going to be O(n log n), because as n becomes very large, it will take longer for each for loop to execute, while each while loop takes longer, but decreasingly so, time to complete.

c)
Recursion. Base case is if bunnies has reached 0, return 0, otherwise add two to the stack's count and subtract
bunnies by 1.

This function is going to be O(n/2) because as n increases, the number of recursions that must be completed increase proportional to one half of n.

## Exercise II


Initialize variables lowest_broken, highest_unbroken to None
While lowest_broken - highest_unbroken > 1:
    Select halfway through the building, and drop an egg.
        If egg breaks,
            record lowest_broken and minimize search area to the bottom remaining half.

        Else,
            record highest_unbroken and minimize search area to the top remaining half.

return lowest_broken

This function mimics a binary search but instead of a target, it is moving through the data structure until it satisfies the necessary condition. This algorithm will have a runtime complexity of O(log n).