# Einstein's Riddle Solver

__Puzzle:__ [Einstein's Riddle Solver](https://www.codingame.com/training/hard/einsteins-riddle-solver)

__Author:__ [@OroshiX](https://www.codingame.com/profile/045d3b89723c9acafb728c9fd1d8cb297970931)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ A Subtle Shift In Perspective Can Make Life a Lot Easier

# Strategy

Einstein’s Riddle Solver lends itself perfectly to the tiles on a gameboard analogy. Even the problem statement directs you to…

>solve the riddle and print it as a grid, separated by space and newline, with each person in their own column and each characteristic category on its own line.

And what are the tiles? They are the characteristics, of course. Your job is to place all the tiles on the grid. I’ll bet that sounds familiar.

In Sudoku, some cells are prefilled and I suggested handling that by limiting the actions available for those cell to a single action, putting the correct number tile on that prefilled grid position. This puzzle has essentially prefilled the entire first row:

>The characteristics in the first line will be ordered alphabetically…

You can choose to put any characteristic in any column, as long as you obey the rules. The examples given in the problem statement are:

1)	Georges & Salad which means Georges eats Salad
2)	Georges ! Salad which means Georges doesn't eat Salad.

#1 is very clear. You cannot put salad in the same column as George! Sounds like mutual exclusivity, right? But what about #2. How can we handle mutual inclusivity, actions that __must__ happen together?

Assume I have a set of items: `{a, b, c, d, e}` and it is given that `a` and `c` are mutually inclusive. I have to choose two items from the set, but if I choose `a`, I must also choose `c` or if I first choose `c`, I must also choose `a`. Any combination of `b`, `d` and `e` would be fine. In this playground, we have only covered mutual exclusivity, never inclusivity. Is there a way we can handle this situation with what we already know? There sure is!

If `a` and `c` must be chose together, I could restate that as `a` must not be chosen with `b`, `a` must not be chosen with `d` and `a` must not be chosen with `d`. The only options left are to choose both `a` and `c` or to choose some combination of  `b`, `d` and `e`.

If Georges must have Salad, you can accomplish that by making sure Georges cannot have any of the other food options. Later in the playground, I’ll discuss another way to handle mutual inclusivity, but changing the mutually inclusive requirement to a set of mutually exclusive requirements is an easy and often effective solution.
