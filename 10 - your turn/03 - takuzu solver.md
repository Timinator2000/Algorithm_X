# Takuzu Solver

__Puzzle:__ [Takuzu Solver](https://www.codingame.com/training/hard/takuzu-solver)

__Author:__ [@vinc-r](https://www.codingame.com/profile/fb82e6cef7c3f73e81256761a6cac2043494314)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Enjoyably Complex: A Bit of Everything Covered So Far

Unlike many logic puzzles, Takuzu has very limited options. Each cell can be a `0` or a `1`. Solving a Takuzu is still plenty challenging, but the limited cell options might make it a bit easier to focus on problem-space reduction and setting up Algorithm X.

# Problem-Space Setup

Takuzu has a very similar structure to Sudoku. There are cells and those cells are grouped into rows and columns, but because the cells can only contain zeros and ones, I found little code I could reuse, other than the overall structure.

{TakuzuCell and TukuzuGroup }

If you use this structure, setting up the grid, the rows and the columns is extremely similar to setting up a Sudoku.


```
class TakuzuSolver(AlgorithmXSolver):

    def __init__(self, grid: List[List[str]]):

        self.size = len(grid)
        self.grid = {(r, c):TakuzuCell(r, c, val) for r, row in enumerate(grid) for c, val in enumerate(row)}
        self.rows = [TakuzuGroup([self.grid[(r, c)] for c in range(self.size)]) for r in range(self.size)]
        self.cols = [TakuzuGroup([self.grid[(r, c)] for r in range(self.size)]) for c in range(self.size)]
```

I then use an almost identical loop for problem-space reduction.


```
        need_to_reduce = True
        while need_to_reduce:
            need_to_reduce = False
            for group in self.rows + self.cols:
                if group.reduce_():
                    need_to_reduce = True
```

I share this code simply to demonstrate the power of a reusable approach to similar problems. You might come up with a completely different approach and that is perfectly okay. Keep in mind that there are many logic puzzles and a significant number of those puzzles are a grid of cells grouped into rows, cols, boxes, cages, etc. More generally,  _a significant number of those puzzles are a grid of cells organized into groups._ Whatever structure works for you, I invite you to look for opportunities to reuse the work you have already done.

 Unfortunately, this is where the similarities to Sudoku end!

# Reducing the Problem Space

There is a lot of great problem-space reduction possible in Takuzu and the best place to start is with the objectives, straight out of the puzzle description.
>The objective is to fill the grid with 1s and 0s, constraints are :
> - an equal number of 1s and 0s in each row and column
> - no more than two of either number adjacent to each other
> - no identical rows and no identical columns





# What is Possible

No reducing at all - still solve 1, 2 & 3 very fast. Test cases 2 and 3 generate a pretty good handful of solutions before a solution is met that meets the requirements. 30 and 78. ME requirements are critical. Without them, you will probably not pass Test case 3.

To be fast on all test cases requires good reducing + me_requirements.

