# A Sudoku Data Structure

A few pages ago, I intentionally drew the original sudoku grid as 81 disconnected cells to create the perception of each cell being a standalone entity, or object. Since each cell is a standalone object, I can put a pointer to that cell into each group it belongs to. I will demonstrate how to do this with Sudoku, and later I will give an overview of how this same general structure can be used on several other puzzles.

First, a class for an individual cell:

```
UNKNOWN = '.'

class SudokuCell():

    def __init__(self, value: str, all_possible_values: str):
        self.value = value
        self.candidates = set(all_possible_values) if value == UNKNOWN else {value}

    def reduce_(self, unavailable_values: set):
        # your code goes here – make sure all unavailable_values are removed from the candidates
```

Second, a class for a Sudoku group:

```
class SudokuGroup():

    def __init__(self):
        self.cells = []

    def reduce_(self):
        # your reducing code goes here
```

Next, in the constructor of my SudokuSolver class, I will use a dictionary comprehension to create an instance of a `SudokuCell` for each location in the grid. Using the `(row, col)` tuple as the dictionary key makes it easy to get a pointer to a cell as the groups are built.

```
class SudokuSolver(AlgorithmXSolver):

    def __init__(self, grid: List[List[str]], values: str):

        # Calculate size and box size so that one 
        # class works for different size Sudokus.
        size = len(grid)
        box_size = int(size ** 0.5)

        self.grid = {(row, col): SudokuCell(grid[row][col], values) for row in range(size) for col in range(size)}

```
It would have been just as easy to create a two-dimensional array of `SudokuCell` instances. I chose to use a dictionary to hold the cells to intentionally blur the visual of a Sudoku grid. It can be beneficial to think in terms of rows, columns and boxs as compared to hanging on to the visual of a two-dimensional grid.

Continuing in the constructor, I create a list of `SudokuGroup`s for the rows, another for the columns and a third for the boxes.

```
        rows = [SudokuGroup() for _ in range(size)]
        cols = [SudokuGroup() for _ in range(size)]
        boxes = [SudokuGroup() for _ in range(size)]
```

The last step is to put all the cells into the groups to which they belong. The values of `self.grid` are all pointers to an instance of a `SudokuCell`. After the following code executes, what remains is 27 groups and each group has a list of pointers to the cells that make up that group. A change to one cell is seen by all groups to which that cell belongs.

```
        for row in range(size):
            for col in range(size):
                box = row // box_size * box_size + col // box_size
                rows[row].cells.append(self.grid[(row, col)])
                cols[col].cells.append(self.grid[(row, col)])
                boxes[box].cells.append(self.grid[(row, col)])

```

# A Short Algorithm to Fascilate Problem-Space Reduction

All that is left now is to loop over all 27 groups, one at a time, reducing the problem space where possible.

```
        need_to_reduce = True
        while need_to_reduce:
            need_to_reduce = False
            for group in rows + cols + boxes:
                if group.reduce_():
                    need_to_reduce = True
```

The `while` loop will continue as long as at least one group is able to reduce the problem space in some way. Only after all 27 groups indicate no reduction is possible does the code exit the `while` loop and I’m sure you know what comes next, building the requirements and actions for Algorithm X.

# Reducing a Sudoku

This framework cwill get you going in a good direction, but there is still a lot of code to write. You may have already completed all the Sudoku puzzles using Algorithm X, but there is a lot to be learned if you take on the challenge of solving those puzzles again using only logic. On the next page, I'll give you a few hints as to what is possible on all the Sudoku puzzles using only logical, problem-space reduction. Later in the playground, I'll explore a few puzzles that need a combination of both to fully complete.
