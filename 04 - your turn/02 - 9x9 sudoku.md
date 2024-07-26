# Puzzle Details

Puzzle: [Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver)

Author: [@AllTheKingsMen](https://www.codingame.com/profile/571927d715f15c3dec7693f461e2a63c6671233)

Difficulty: Medium

# Strategy

Sudoku is a great place to start because a Sudoku always comes with a partial solution already in place. Some portion of the grid has already been filled in. Some number of actions have already been taken and are required to be a part of any complete solution.
Many exact cover problems will start with a partial solution and there are a couple of ways to handle that. Let’s take a look at how the known cells are address in [Assaf's Sudoku]( https://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt) code.

__Assaf’s technique will NOT currently work with my provided AlgorithmXSolver. It is on my to-do list to add the necessary functionality, but it is not currently available.__ After going through Assaf's code, I will demonstrate how to handle partial solutions with my AlgorithmXSolver.

# Pre-Select Known Actions – à la Ali Assaf

Assaf first builds a list of requirements (`X`).

```python
    R, C = size
    N = R * C
    X = ([("rc", rc) for rc in product(range(N), range(N))] +
         [("rn", rn) for rn in product(range(N), range(1, N + 1))] +
         [("cn", cn) for cn in product(range(N), range(1, N + 1))] +
         [("bn", bn) for bn in product(range(N), range(1, N + 1))])
```

Assaf then builds a dictionary of actions (`Y`). Notice that __all__ possible actions are included in the dictionary. Assaf does not limit the actions for cells that already contain a value.

```python 
    Y = dict()
    for r, c, n in product(range(N), range(N), range(1, N + 1)):
        b = (r // R) * R + (c // C) # Box number
        Y[(r, c, n)] = [
            ("rc", (r, c)),
            ("rn", (r, n)),
            ("cn", (c, n)),
            ("bn", (b, n))]
```

In this next line, Assaf makes a call to `exact cover` which converts his `X` list to a dictionary necessary for his implementation of Algorithm X.

```python
    X, Y = exact_cover(X, Y)
```

Now that the matrix is built and ready to go, Assaf uses the following code to add actions to the solution before asking Algorithm X to use backtracking to find the remaining actions that solve the entire Sudoku. He loops through all cells in the Sudoku grid and `if` there is a number (`n`) in the cell, Assaf makes a call to `select` to add the appropriate action to the solution and make the necessary adjustments to the matrix.

```python
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n:
                select(X, Y, (i, j, n))
```

Finally, Assaf builds a solved Sudoku grid with code that should look somewhat familiar. For the most part, my initial AlgorithmXSolver was simply the Assaf code you see right here, organizing inside an AlgorithmXSolver class.


```python
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid
```

# Restrict Possible Actions – à la [@Timinator](https://www.codingame.com/profile/2df7157da821f39bbf6b36efae1568142907334)

I used Assaf’s technique for quite a while, but I eventually started restricting my possible actions when building my dictionary of actions. For 9x9 Sudoku, I loop through all the cells of the grid. If the cell is empty, I add 9 possible actions. If the cell already has a value, I only add a single action. The pseudocode looks like this:

```python
    for each cell in the grid:
        if the cell is empty
            possible values = all possible values
        else
            possible values = cell value

        for each value in possible values
            add a possible action for placing this value in this cell
```

Algorithm X will immediately select the action associated with pre-filled cells because they are the only actions that cover the requirement that a value be placed in that cell.

__NOTE: If you choose to use my provided Algorithm X solver, it is currently imperative that you restrict the possible actions to truly possible actions, rather than following Assaf’s example of “selecting” certain actions after setting up the problem but before performing the backtracking.__
