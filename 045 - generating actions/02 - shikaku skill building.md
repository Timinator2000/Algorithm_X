# Shikaku Skill Builder

Puzzle: [Shikaku Skill Builder]()

Author: [@Timinator](https://www.codingame.com/profile/2df7157da821f39bbf6b36efae1568142907334)

Published Difficulty: Easy

# Visualizing the Problem

Shikaku is a great place to start because the directions have a decent chance of putting you on a path that might lead to a dead end. According to the Shikaku Solver puzzle specification:

>The objective is to divide the grid into rectangular pieces such that each piece contains exactly one number, and that number represents the area of the rectangle.

That is all true, but “dividing” is not something discussed in terms of visualizing a problem. Let’s look at Shikaku a different way. Consider that you start with an outline of the grid with some numbers penciled in. You also have a large pile of rectangular tiles, each one having a certain width and height, from which you can calculate the area of the tile. Your job is to place tiles on the grid one-by-one, appropriately covering the penciled-in numbers, until the entire grid is covered with tiles.

Algorithm X doesn’t know how to “divide” things up. Algorithm X is very good at finding a subset of a “large pile” of options and it is critical that we give Algorithm X a __complete__ set of “tiles” from which it can pick and choose to build valid solutions.

# Skill Building

In the Shikaku Sill Building puzzle, the grids start very small and even the largest grid is just the smallest test case from the Shikaku Solver. The goal of the puzzle is to practice enumerating all the possible actions. Let’s do a couple of examples.

?[Given the following grid, how many way can you place a tile with area 9 on the grid such that the 9 is covered?
    0 0 0
    0 9 0
    0 0 0]
- [ ] I have no idea. 
- [ ] 9
- [ ] 2 
- [x] 1






?[You have a 3x3 grid with all spaces empty, except a 9 in the middle square. How many different ways can you put a tile with area 9 on the grid so that the 9 in the middle square is covered by the tile?]
- [ ] I have no idea. 
- [ ] 9
- [ ] 2 
- [x] 1


?[How many solutions did Algorithm X find?]
- [ ] None - I was too lazy to click “run”.
- [ ] 2 – Exactly what I expected!
- [x] 4 – Is Algorithm X broken?
- [ ] 37 – Ella just stopped by and bumped her request to 5 lessons per week.


