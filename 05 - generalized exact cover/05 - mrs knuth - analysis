# Constraining the Realm of Possibility

I have chosen to use the word “requirement”, but you will often see the word “constraint” used with Algorithm X. Each word is powerful in its own way. I want to briefly demonstrate where the word “constraint” really helps us understand the big picture of Algorithm X.

Consider Mrs. Knuth’s desire to avoid teaching more than one lesson per day for any instrument. An alternate approach to what was discussed above might be to build all possible schedules and then check each schedule to see if any day has a repeated instrument. Because Algorithm X is _less constrained_, it will generate many solutions that eventually get eliminated when the days are checked for duplicate instrument lessons.

How many solutions get eliminated? Because all test cases in Mrs. Knuth - Part I are guaranteed to have a unique solution, we know all possible solutions _except one_ will be eliminated. That doesn’t really make the point I want to make unless we look at how many solutions need to be checked.

Test Cases 1 and 2 only have Mrs. Knuth teaching on a single day, so there is no impact to those test cases. However, starting with Test Case 3, the unconstrained results grow rapidly. Remember, every one of these possible solutions would need to be checked to make sure no instrument is taught more than once on the same day!

* Test Case 3 - 96 possible solutions

* Test Case 4 - 1,818 possible solutions

* Test Case 5 - 11,414 possible solutions

* Test Case 6 - 130,235 possible solutions

* Test Case 7 – 241,460,379 possible solutions

There is a moral to this story. It is best to restrict Algorithm X as much as possible with constraints (requirements). You will not always be able to eliminate the need to further validate potential solutions after Algorithm X finds them, but, by maximizing the knowledge passed to Algorithm X, you will probably be rewarded with a significantly smaller set of possible solutions, and in many cases, you will be rewarded with the _only_ valid solution.
