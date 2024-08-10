# Winamax Sponsored Contest

Puzzle: [Winamax Sponsored Contest](https://www.codingame.com/training/hard/winamax-sponsored-contest)

Difficulty: Hard

Algorithm X Complexity: Requirements are Straightforward, Actions are Complex (Are You Prone to Headaches?)

# Big Payoff!

__250 XP!!!__ Need I say more? Puzzles on Codingame that offer unusually high XP are always popular. This puzzle is so creative, I am not sure it even needs the high XP.

# Visualizing the Problem
Let’s start with a quote right from the problem statement:

> In this puzzle, you are given a grid representing a golf course. On each course is a certain amount of balls and an equal amount of holes. The objective is to find the route for each ball to a different hole without their paths ever crossing.

Using the analogy of laying tiles on a grid, it seems pretty obvious the grid is the map of the golf course given in the input. Per the statement above, the grid will indicate where the holes are and where the balls are. Later in the problem statement, we are told the grid also identifies water hazards and open fairway spaces.

What are the tiles we can feed into Algorithm X? What are the tiles we can lay down on the grid? It might be tempting to consider each movement of the ball to be a tile, but that would be similar to considering each square in a rectangle to be a separate tile. In Shikaku, Algorithm X needed a full list of possible rectangles and each one of those rectangles is a tile that can be placed on the grid. Let’s again look to the problem statement for a hint:

>The objective is to find the route for each ball to a different hole without their paths ever crossing.

Each possible route from a ball to a hole is a tile that could be placed on the grid. Given 5 balls and 5 holes and a bunch of possible routes from the balls to the holes, Algorithm X will gracefully find a set of routes where each ball goes “to a different hole without their paths ever crossing”.

# Enumerating the Actions

I have recommended that you use human readable tuples when identifying actions for an exact cover problem and the information in those tuples need to unique distinguish each action from all other actions. What information is needed to uniquely identify a route? Since a route can zig and zag in all kinds of directions, the only way to uniquely identify a route is with a full set of grid coordinates that make up the route. What about routes that are short vs routes that are long. This seems like it could be challenging, there is an easy solution.

Let’s say you have 100 possible routes from balls to holes. Give every route a unique integer ID between 1 and 100 and use that unique ID as your action in terms of Algorithm X. Remember, the mapping from actions to covered requirements is the important information. The 1s in the matrix are the powerful knowledge elements that fuel Algorithm X.

Going back to the tiles on a board analogy, each tile now has route number on it, but what does that tile look like. Since we had to generate all the routes and we know all grid coordinates that make up route, you can now visualize each tile in the zigzagging route determined by its coordinates. Algorithm X is going to get a very big pile of crazy shaped zigzagging tiles to be placed on the grid.

By the way, you’ll need to keep those notes. When Algorithm X tells you route 56 is part of the solution, you will need to know how to incorporate that in your output.

To be honest, generating an exhaustive list of routes is harder than setting up Algorithm X.

# Identifying Requirements
The Winamax problem statement is very well written.

