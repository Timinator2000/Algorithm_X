# Sudoku Solver (cont.)

The following 3 options always leave Algorithm X in charge. Instead of preselecting any cells of the Sudoku, Algorithm X will be instructed to __try__ to put certain values in certain cells. Algorithm X is great at “trying” things. Afterall, that is the general idea of any backtracking technique.

# Option 2: Restrict Possible Actions

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

# Option 3: Use Hints

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

I have never used Option 3 as part of an exact cover solution, but you will run into this technique if you study other Algorithm X solutions found online.

# Option 4: Give Algorithm X a Partial Problem

