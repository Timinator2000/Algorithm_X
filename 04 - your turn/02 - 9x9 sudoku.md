# Sudoku Solver

__Puzzle:__ [Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver)

__Author:__ [@AllTheKingsMen](https://www.codingame.com/profile/571927d715f15c3dec7693f461e2a63c6671233)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ If Only They Were All This Straightforward

# Strategy

Sudoku is a great place to start because a basic Sudoku always comes with a partial solution already in place. Some portion of the grid has already been prefilled. Some number of actions have already been taken and are required to be a part of any complete solution.

Many exact cover problems will start with a partial solution and there are several ways to handle that. Let’s first take a look at how the known cells are addressed in [Assaf's Sudoku]( https://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt) code.

# Option 1: Preselect Known Actions – à la Ali Assaf

Assaf first builds a list of requirements (`X`).

Note: In Assaf's code, `R` and `C` are the numbers of rows and columns in a Sudoku box or subgrid. A 9x9 Sudoku grid has 9 boxes and each box is 3x3. For a traditional 9x9 Sudoku, `N` = 9 in Assaf's code, but `R` and `C` are both 3.

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

Finally, Assaf builds a solved Sudoku grid with code that should look somewhat familiar. For the most part, my initial AlgorithmXSolver was simply the Assaf code we just covered, organized inside an AlgorithmXSolver class.


```python
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid
```

# Option 1:  Preselect Known Actions - à la [@Timinator](https://www.codingame.com/profile/2df7157da821f39bbf6b36efae1568142907334)
You can preselect known actions with my AlgorithmXSolver, just like was done in Assaf’s code, but the syntax is slightly different. To preselect an action, you will call the AlgorithmXSolver `select()` method and pass in the appropriate action as a keyword argument. For a 9x9 Sudoku, the following code will preselect all cells that already have a number penciled in.

```
        # preselecting cells for a Sudoku should be done right after calling the inherited __init__()

        requirements = []
        actions = dict()

        super().__init__(requirements, actions)

        # assume all actions are a tuple formatted as (‘place value’, row , col, value) 
        for row in range(9):
            for col in range(9):
                if grid[row][col] has a number penciled in:
                    self.select(action=('place value', row, col, grid[row][col]))

```
# Option 1 Will Not Always Work

Assaf’s technique is simple and straightforward, but it will not always work. It will only work when the actions you are preselecting are proper actions. The DLX matrix is not meant to handle the selection of improper actions. Every time an action is selected to be part of a solution, DLX removes any impossible actions from the realm of possibility. When Algorithm X is in charge, it is impossible to select an action that cannot possibly be part of the final solution.

Consider the following example. Do solutions exist for the Sudoku board below?

```
0 0 6 0 0 0 6 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

You and I can easily see there are two 6s in the first row, making it is impossible to ever find a proper solution. Obviously, this is a toy example, but play along with me.  Assume you want to use Algorithm X to determine if the Sudoku can be solved or not. You first create the requirements and the actions. Then you try to preselect the action that puts a 6 in row 1, col 3 and the action that puts a 6 in row 1, col 7. As soon as you preselect the first action, the DLX matrix is adjusted and there is no longer an option to put the second 6 in row 1, col 7. You tried to preselect an action that is no longer possible. My AlgorithmXSolver will tell you it cannot comply with your request and it __will not put a 6 in row 1, col 7__. If you then ask Algorithm X to look for solutions, it will find many proper solutions since it is starting with a blank Sudoku with a single 6 preselect in row 1, col 3. 

The solution is simple. The solution is to leave Algorithm X in charge. I'm not saying you should never use Assaf's technique, but you need to recognize when other options are required. Let’s look at 3 more options, all of which leave Algorithm X completely in charge of managing the DLX matrix, but still accomplish the same preselection process.

