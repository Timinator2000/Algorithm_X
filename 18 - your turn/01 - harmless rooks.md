# Harmless Rooks

__Puzzle:__ [Harmless Rooks](https://www.codingame.com/training/hard/harmless-rooks)

__Author:__ [@Niako](https://www.codingame.com/profile/eb89cbdf69d07106c84edf1d191caaf33289651)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Algorithm X is the Easy Part

# Problem Statement

Harmless Rooks is a hard puzzle, but a very short Algorithm X setup can easily solve the first two test cases and get you moving in a powerful direction. Although the Algorithm X setup is not terribly complex, some background is helpful. For convenience, I have copied the entire goal statement here:

> The __rook__ is a chess piece that can move along its current line (horizontally) or column (vertically) through any number of free (unoccupied) squares.
>
>In this problem, we consider an N × N generalized chess board where the squares are either free (. in the input) or already occupied (X in the input) and hence cannot be crossed by the rooks.
>
>Compute the __maximum number of rooks__ that can be placed on __free squares__ in such a way that __no two rooks threaten each other__ (hence two rooks on the same line/column must be separated by at least one occupied square).

# A Perfect World

Rooks move along horizontal and vertical lines. On a standard 8 x 8 chessboard, there are 16 total attack lines, 8 rows and 8 columns. A rook placed on location `(r, c)` _threatens_ all locations in row  `r` and all location in column `c`. Because there is no functional difference between a row and a column, I will refer to all rows and all columns as `AttackLine`s, an uninterrupted group of 1 or more cells that, together, make a horizontal or vertical line. A rook placed on any location in the `AttackLine` threatens all other locations in the `AttackLine`.

Placing a single rook on a standard 8 x 8 chessboard covers two `AttackLine`s, one horizontal and one vertical. On any `N x N` chessboard, consisting of all free squares, a maximum of `N`rooks can be placed. Each rook occupies one row and one column. Using this unobstructed chessboard, the following problem could be considered:

>Given an `N x N` chessboard with all free squares, how many different ways can `N` rooks be placed on the board, such that no rook threatens any other rook?

How could Algorithm X be set up to solve this problem? What are the requirements? Every one of the `N * N` `AttackLine`s must be covered by a rook. What are the actions? Each action is simply placing a rook at location `(r, c)` and each action coves two requirements, one for each `AttackLine` coved by the rook placement.

Asking Algorithm X to find the number of possible configurations for values of `N` between 2 and 10 results in the following:

| N | Valid Configurations |
|:-----:|:---------:|
|2|2|
|3|6|
|4|24|
|5|120|
|6|720|
|7|5040|
|8|40320|
|9|362880|
|10|3628800|

It is not difficult to show that for any `N x N` chessboard, there are `N` factorial ways to arrange the rooks. However, I chose to illustrate how Algorithm X could produce these results to lay the groundwork for an Algorithm X approach to the oddly configured boards found in Harmless Rooks.

# Handling Occupied Spaces

Harmless Rooks has some large boards with many spaces already occupied. Since rooks cannot cross occupied squares, each occupied square either shortens an `AttackLine` or divides an `AttackLine` into two separate lines. Even a single location, bordered on all sides by occupied spaces forms two `AttackLine`s, one horizontal and one vertical. Placing a rook on that isolated space occupies both `AttackLine`s.

On a board with no occupied spaces, the maximum number of rooks is always `N`. Each rook placed covers one column and one row. Said another way, each rook covers exactly two `AttackLine`s and __all__ `AttackLine`s are covered. As soon as occupied spaces show up on a board, it can get much more difficult to cover every `AttackLine`. Consider the following 5 x 5 board with a single occupied space.

{5 x 5 board with one occupied space}

The board now has 11 `AttackLine`s. Each rook placed covers exactly 2 `AttackLine`s, making it is impossible to cover every `AttackLine`. However, we might consider asking Algorithm X to attempt the following:

>Try to cover every `AttackLine` by placing rooks on open squares. If no solution exists that covers all AttackLine`s, identify the partial solution that gets the closest.

# Customizing Algorithm X To Be Inefficient

Algorithm X is designed to be efficient, and it is extremely efficient at identifying when paths are dead ends. As soon as Algorithm X determines that a path will eventually be a dead end, paths forward are no longer explored and backtracking happens. Without any customization, Algorithm X can quickly determine if __all__ `AttackLine`s can be covered, but it is not designed to tell us how close it can get to a proper solution when no full solution is possible.

How does Algorithm X know when a path is a dead end? The matrix has at least one requirement that no longer has any rows that cover it. Since it is impossible for one of the (mandatory) requirements to be satisfied, Algorithm X backtracks. `AlgorithmXSolver` implements this process by sorting requirements by the number of rows remaining that cover each requirement, often referred to as Minimum Remaining Value (MRV). Columns that are not covered by any rows are sifted to the front of the line and Algorithm X immediately knows it is time to backtrack. The default behavior happens in the `AlgorithmXSolver` method `_requirement_sort_criteria(self, col_header: DLXCell)` as shown below. 


```
    def _requirement_sort_criteria(self, col_header: DLXCell):
        return col_header.size
```

The `size` attribute keeps track of the number of rows that still cover the requirement. `AlgorithmXSolver` will sort all remaining requirements by the number of rows covering each requirement and then pick the requirement with the _minimum remaining value (number of rows)_.

For this puzzle, I know that occupied cells will most likely create a squares where I cannot cover ever `AttackLine`, so I don’t want Algorithm X to backtrack just because it finds one `AttackLine` cannot be covered. Instead, I want Algorithm X to keep placing rooks until none of the remaining `AttackLine`s can be coved. This is easily accomplish simply be reversing the sort order to push requirements that cannot be covered to the end of the line. To implement this in your solver, override the `_requirement_sort_criteria()` method as follows:

```
    def _requirement_sort_criteria(self, col_header: DLXCell):
        return -col_header.size
```

A single `-` sign is all that is needed. As long as a rook can be placed, Algorithm X will continue exploring, looking for a solution that covers all `AttackLine`s. Backtracking will __only__ happen when the matrix shows that none of the remaining `AttackLine`s can be covered by any rook placement. 

# Counting Rooks

Just a few lines of code can customize your solver to keep track of the maximum number of rooks placed. First add two attributes in your solver’s constructor:

```python
self.rooks_placed = 0
self.most_rooks_placed = 0
```

Then, override the `_process_row_selection()` and `_process_row_deselection()` as follows:

```
    def _process_row_selection(self, row):
        self.rooks_placed += 1
        self.max_rooks_placed = max(self.rooks_placed, self.max_rooks_placed)

def _process_row_deselection(self, row):
        self.rooks_placed -= 1
```

You now have a fully functional solver that can finish test cases 1 and 2, but you will probably have timeout issues after that. To solve the remaining test cases, you will need to find ways to reduce the problem space by placing rooks logically. 
