# Shikaku Skill Builder

Puzzle: [Shikaku Skill Builder]() - LINK NEEDED

Author: [@Timinator](https://www.codingame.com/profile/2df7157da821f39bbf6b36efae1568142907334)

Published Difficulty: Easy

# Visualizing the Problem

Shikaku is a great place to start because the directions have a decent chance of putting you on a path that might lead to a dead end. According to the [Shikaku Solver](https://www.codingame.com/training/medium/shikaku-solver) puzzle specification:

>The objective is to divide the grid into rectangular pieces such that each piece contains exactly one number, and that number represents the area of the rectangle.

That is all true, but “dividing” is not something discussed in terms of visualizing a problem. Let’s look at Shikaku a different way. Consider that you start with an outline of the grid with some numbers penciled in. You also have a large pile of rectangular tiles, each one having a certain width and height, from which you can calculate the area of the tile. Your job is to place tiles on the grid one-by-one, appropriately covering the penciled-in numbers, until the entire grid is covered with tiles.

Algorithm X doesn’t know how to “divide” things up. Algorithm X is very good at finding a subset of a “large pile” of options and it is critical that we give Algorithm X a __complete__ set of “tiles” from which it can pick and choose to build valid solutions.

# Skill Building

In the Shikaku Skill Builder puzzle, the grids start very small and even the largest grid is just the smallest test case from the Shikaku Solver. The goal of the puzzle is to practice enumerating all the possible actions. Let’s test your understanding.

# Start Out Easy

```
          0 0 0
          0 9 0
          0 0 0
```

?[Given the grid above, how many way can you place a tile with area 9 on the grid such that the 9 is covered?]
- [ ] I have no idea. 
- [ ] 4
- [ ] 3 
- [x] 1

# {INSERT SOLUTUION GRAPHIC}

# 2x1 vs 1x2

```
          0 2 0 0
          0 0 4 0
          0 0 0 0
```


?[Given the grid above, how many way can you place a tile with area 2 on the grid such that the 2 is covered? Remember your tile must cover the 2, but it MUST NOT cover any other number]
- [ ] I have no idea. 
- [ ] 4
- [x] 3 
- [ ] 1

# Ractangles Cannot Cover Two Numbers

# {INSERT SOLUTUION GRAPHIC}

```
          0 2 0 0
          0 0 4 0
          0 0 0 0
```

?[Given the grid above, how many way can you place a tile with area 4 on the grid such that the 4 is covered? Remember your tile must cover the 4, but it MUST NOT cover any other number.]
- [ ] I have no idea. 
- [x] 4
- [ ] 2 
- [ ] 1

# {INSERT SOLUTUION GRAPHIC}

# Ready for the Puzzle!

With the Shikaku Skill Builder puzzle, the goal is not to cover the grid. The goal is to identify __every__ rectangle that could be used to build a potential solution. As I said before, Algorithm X is really good at finding a set of actions that make a valid solution, but it cannot do its job unless you give it a full set of possible actions to consider. Hopefull this seems obvious and somewhat easy right now. As the puzzles grow in complexity, this process will get more and more challenging!
