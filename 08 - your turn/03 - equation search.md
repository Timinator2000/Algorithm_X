# Equation Search

__Puzzle:__ [Equation Search](https://www.codingame.com) LINK NEEDED

__Author:__ [@Timinator](https://www.codingame.com/profile/2df7157da821f39bbf6b36efae1568142907334)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Specifically Designed to Test What You Have Learned So Far

# Strategy

The most important part to creating an Algorithm X solution for Equation Search is coming up with a gameboard/tiles analogy. What does the gameboard look like? There could be a temptation to make every operand and every operator a tile. The gameboard would be made up of several equations, each equation having 3 spots for 2 operands and 1 operator. Given right sides of 5, 7 and 10, the gameboard might look like:

{gameboard 1}

As tiles are put on the gameboard, some sort of validation would need to be done to see if there is some way to put the operands and the operator together to come up with the right-side value. This feels a bit like making tiles in Winamax correspond to every cell in the grid. With Winamax, it ultimately was better to build routes and consider each possible route a tile that could be placed on the gameboard. A similar approach will work better here.

Let’s make gameboard nothing more than a list of right-side value. Using the strategy we know worked for Winamax, we can make each tile here a full equation, including the right-side value. The goal becomes to place the equation tiles on the matching right-side values found on the gameboard.

?[How many requirements are satisfied every time you put an equation on the gameboard?]
[]-1
[]-2
[x]-3
[]-4

The correct answer is 3. Putting a single equation tile on the gameboard covers one of the right-side numbers and it covers one of the necessary occurrences for each operand. Of course, if the operands are the same, it covers two of the necessary occurrences for that operand. Let’s look at an example. 

Assume the operand counts include one 2 and three 5s. 

?[How many different ways are there to create an equation that equals 10?]
[]-4
[x]-6
[]-8
[]-13

The correct answer is 6! Remember, because of the multiplicity, you can use the first 5, the second 5 or the third 5. The possible equations look like this:

{Ways to make 10}

There is a fair amount of multiplicity in this puzzle and to solve the bigger test cases, you will need to properly use AlgorithmXSolver’s memory. What is it you will want Algorithm X to remember?
