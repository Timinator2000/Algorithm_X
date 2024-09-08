# Kakuro Solver

__Puzzle:__ [Kakuro Solver](https://www.codingame.com/training/hard/kakuro-solver)

__Author:__ [@Q12](https://www.codingame.com/profile/b683bbb0b3a4c1d61f3ac36f8201d98a6101573)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Algorithm X Setup Is a Subset of Killer Sudoku

# Strategy

To solve Kakuro Solver, you will need to do more problem space reduction that you have done for any puzzle so far. The cell groups must add up to certain numbers, but other than that, you have very little with which to work.

# Tougher Input to Parse

The input for Kakuro Solver is a bit challenging, but I encourage you to make your goal to copy what has been done on every logic puzzle so far. A dictionary is used to store pointers to all the cells of the grid and a list is used to held pointers to all the groups.

This puzzle validates the choice of a dictionary for the grid over any type of 2-dimensional array. Why? The only important cells to put in the dictionary are cells in the Kakuro grid that are either empty or already contain a number. A number of cells in the Kakuro grid are used to tell us how to group cells and what the sum of the cells in the group must be. The information obtained from those cells is used to build the groups, but that information never changes. There is no need to store these cells in the dictionary.

1. Parse the input, creating an instance of a `KakuroCell` in the `self.grid` dictionary. 

1. Parse the input again, this time looking for locations in the Kakuro input that indicate how to group the cells and the sum of each group. Create a new group with a list of pointers to the cells in the group.

# Sum of a Group of Cells?

Unlike many of the puzzles covered so far, the goal statement does not give a name to the groups of cells. The puzzle statement tells us:

>Rules:
>- All empty cells need to be filled in with digits, in such a way that all the given sums are respected.
>- You are not allowed to use the same digit more than once to obtain a given sum.

>- Cell with backslash : the required sum of the corresponding cells.
>- X\ : the vertical sum X of the cells downwards,
>- \X : the horizontal sum X of the cells to the right,
>- X\Y : the vertical sum X of the cells downwards, and the horizontal sum Y of the cells to the right.

Do you see the similarities between these groups and the cages you just explored in [Killer Sudoku Solver]( https://www.codingame.com/training/medium/killer-sudoku-solver)? What are the differences?

One difference is that in Kakuro, the groups are either a horizontal line of cells or a vertical line of cells. Although this is true, is it important. In both puzzles, all that matters is that the cells add up to a certain value and the numbers in the group do not repeat.

Groups in Kakuro are 100% identical to `Cage`s in Killer Sudoku. Hopefully you got a good start on reducing these cages. Regardless of how much cage reducing you already implemented, my guess is you will now need more.

# Suggested Path Forward

The big-picture structure of your code can be exactly the same as what you wrote for [High-Rise Buildings]( https://www.codingame.com/training/expert/high-rise-buildings) and [Killer Sudoku Solver]( https://www.codingame.com/training/medium/killer-sudoku-solver).

* Create a diction of cells.
* Create a list of groups.
* Reduce the groups as much as possible.
*	Run Algorithm X.
  *	Update cells when Algorithm X selects rows.
  *	Validate cages and redirect Algorithm X as necessary.
