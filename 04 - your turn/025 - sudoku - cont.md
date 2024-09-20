# Algorithm X Needs to Be in Charge

The DLX matrix is not meant to handle the selection of improper actions. Every time an action is selected to be part of a solution, DLX removes any impossible actions from the realm of possibility. When Algorithm X is in charge, it is impossible to select an action that cannot possibly be part of the final solution.

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

You and I can easily see there are two 6s in the first row, making it is impossible to ever find a proper solution. This is a toy example, but play along with me.  Assume you want to use Algorithm X to determine if the Sudoku can be solved or not. You first create the requirements and the actions. Then you try to preselect the action that puts a 6 in row 1, col 3 and the action that puts a 6 in row 1, col 7. As soon as you preselect the first action, the DLX matrix is adjusted and there is no longer an option to put the second 6 in row 1, col 7. You tried to preselect an action that is no longer possible. You will either get an error, or your solver might produce many solutions since it is starting with a blank Sudoku with a single 6 preselected in row 1, col 3. 

The solution is simple. The solution is to __leave Algorithm X in charge__. Next, I will discuss options that handle preselected cells, but since Algorithm X is in charge, error situations are more easily avoided.



The following 3 options always leave Algorithm X in charge. Instead of preselecting any cells of the Sudoku, Algorithm X will be instructed to __try__ to put certain values in certain cells. Algorithm X is great at “trying” things. Afterall, that is the general idea of any backtracking technique.

# Option 1: Restrict Possible Actions

Rather than preselecting certain cells, restrict Algorithm X to a single option for certain cells. Algorithm X will immediately select these options because there are no other paths forward. For instance, to restrict the possible actions in a 9x9 Sudoku, loop through all the cells of the grid. If the cell is empty, add 9 possible actions. If the cell already has a value, only add a single action. The pseudocode looks like this:

```text
    for each cell in the grid
        if the cell is empty
            possible values = all possible values
        else
            possible values = cell value

        for each value in possible values
            add an action for placing this value in this cell
```

Algorithm X will immediately select the actions associated with pre-filled cells because they are the only actions that cover the requirements that values be placed in those cells. Notice that the process of restricting the option does not need to be exhaustive. At this time, the goal is to simply force Algorithm X to choose preselected options. The goal is not to perfectly minimize the full list of options available to Algorithm X.

# Option 2: Use Hints

If you search the internet for DLX Sudoku solutions, you will find solutions that use hints to guide Algorithm X. Rather than restricting the options available to Algorithm X, hints are used to force Algorithm X to make certain selections. Each hint is a must-be-covered requirement, and each hint is covered by a single action, giving Algorithm X no choice but to select the actions associated with the hints. The pseudocode looks like this:

```text
    for each cell in the grid
        if the cell is prefilled
            add a new requirement -> (‘hint’, row, col)
        for all possible values
            add an action for placing the value in the cell
            if the value = the value in the cell
                add the new "hint" to the list of satisfied requirements
```

I have never used hints as part of an exact cover solution, but you will run into this technique if you study other Algorithm X solutions found online.

# Option 3: Give Algorithm X a Partial Problem

In some puzzles, a portion of the solution can be determined before Algorithm X begins backtracking and what remains for Algorithm X feels like a puzzle that can stand alone. In these cases, I have chosen to maintain a list of actions that must be part of the final solution, while then giving Algorithm X a smaller version of the problem to solve. The smaller problem feels identical to the larger problem in all ways except size. Later in the playground, I will identify a couple of puzzles with which I used this third technique.
