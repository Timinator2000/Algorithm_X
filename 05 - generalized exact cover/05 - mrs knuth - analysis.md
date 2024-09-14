# Constraining the Realm of Possibility

Could you use the solver you wrote for Mrs. Knuth – Part I to solve this new Part II? You sure could, but your Part I solver doesn’t know anything about Troublesome Pairs and Loud Instruments. If you used that original solver, solutions found by Algorithm X would simply need to be checked after they were generated. The puzzle guarantees that every test case has a unique solution, so you could stop checking solutions as soon as you found the proper one, but, in the worst-case scenario, here are the numbers of solutions you have to check in order to find the proper solution.

| Test Case | Solutions To Test if Not Handling Mutual Exclusivity |
|:--|:------------------------------------------------------------------:|
| 1 - |3|
| 2 - |10|
| 3 - |27|
| 4 - |94|
| 5 - |290|
| 6 - |362|
| 7 - |5,578|
| 8 - |114|
| 9 - |7,738|
| 10 - |25,281|
| 11 - |65,887|


Test Case 1 - 3

Test Case 2 - 10

Test Case 3 - 27

Test Case 4 - 94

Test Case 5 - 290

Test Case 6 - 362

Test Case 7 - 5578

Test Case 8 - 114

Test Case 9 - 7738

Test Case 10 - 25281

Test Case 11 – 65887

The execution times required to find and count all these solutions are significantly higher than the time it takes Algorithm X to completely process the matrix and find the unique solution. When I say “completely process the matrix”, I mean that I am __not__ using a `break` statement to stop Algorithm X after if finds the first solution. To compare total processing time, Algorithm X continues searching for a second solution until it has exhausted all options.

My analysis simply counts the solutions that need to be tested. None of the time required to check those solutions has been included. Even the most efficient checking code would need to be executed up to 65,887 times to find the correct solution for Test Case 11.

Just like in Mrs. Knuth – Part I, we see there is tremendous power in providing as much knowledge as possible to Algorithm X. Later in this playground, we will work with situations that require additional processing outside of the standard Algorithm X backtracking. For now, I want to emphasize, Algorithm X and DLX are specifically designed to efficiently handle the backtracking and maximizing the knowledge passed to Algorithm X will maximize the backtracking efficiency and, most likely, the overall problem efficiency.

Next, we will take a look at the actions, the relationship between the requirements and the actions, and the matrix.

