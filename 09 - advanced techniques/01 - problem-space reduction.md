# Problem Space Reduction

At some point in your Algorithm X jouney, you will encounter problems that are too big for backtracking alone. The problem space that must be explored to find all solutions requires an unacceptable amount of time. In these cases, the solution is to use logic to reduct the problem space before starting the backtracking. As has already been demonstrated, backtracking via Algorithm X can solve plenty of problems without any problem-space reduction. We will soon see that logical, problem-space reduction can also solve some problems with no need for any backtracking. In the end, most medium and hard puzzles eventually present test cases that require a combination of both.

If simply solving the puzzle is your goal, a small amount of problem-space reduction before the backtracking will probably get there. However, if you really want to harvest as much eduction as possible out of these puzzles, I suggest you do the following:

1 Solve as many test cases as possible with backtracking alone.
2 Solve as many test cases as possible with problem-space reduction alone.
3 Only after you have exhausted all options for 1 and 2, use a combination of both.

There are many ways to approach problem-space reduction. You will need or choose various data structures and build an algorithm to mimick what you would do if you were trying to solve the puzzle with a pencil on paper. In the rest of this section, I will lay out a structue and a process I have used over and over that has worked well for me.

# One More Round of Sudoku

Consider __Test Case 1: Very Easy__ from [Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver) on [Codingame](https://www.codingame.com). In the test cases, a '0' represents an unknown cell. For the visual effect, the following diagram leaves the unknown cells empty.

{BasicSudoku}

From the problem statement:

>A sudoku is a Latin Square which has the numbers 1-9 in each row, column, and 3x3 square.

In the following diagram, I have assigned numbers to each row, col and box (sub-grid square). Because Python is 0-indexed, I have started numbering at zero.

{SudokuRowsColsBoxes}

We are ready to use logic to try to find more numbers in the Sudoku before starting any backtracking.
