# Puzzle Details

Puzzle: [25x25 Sudoku](https://www.codingame.com/training/expert/25x25-sudoku)

Author: [@yoch](https://www.codingame.com/profile/14a6f9fb972f723d06789c969370ff2e7411725)

Difficulty: Very Hard

# Strategy

Everything you need to know about this puzzle has already been covered in the section on 9x9 Sudoku. However, I do want to add a few comments. Please note, my comments are strictly related to my experience solving this puzzle with Python.

I found this puzzle to be more than just an Exact Cover problem. Algorithm X is a backtracking technique and DLX is a backtracking implementation. Any backtracking problem has many paths that need to be explored and the order in which you choose to explore those paths makes a difference. 

In the world of Algorithm X, the ordering of the columns and the rows in the matrix has an impact on the order in which paths are explored. For now, just know that in order to finish this puzzle within the time limit, I had to find the same matrix organization that the author used. The organizational difference between my original implementation and the author’s implementation was very small, but it was enough to slow me down enough so that I couldn’t finish in time.

Because I only ran into this situation on this one puzzle, my AlgorithmXSolver now defaults to the necessary organizational structure needed by this puzzle and you might not have any problems. However, if you run into timeout issues trying to solve this puzzle, please reach out to me in the [Codingame Forum]( https://www.codingame.com/forum). I will do what I can to help you determine if your issue just comes down to matrix organization or if there is something else slowing you down.
