# Winamax Sponsored Contest

Puzzle: [Winamax Sponsored Contest](https://www.codingame.com/training/hard/winamax-sponsored-contest)

Difficulty: Hard

Algorithm X Complexity: Requirements are Straightforward, Actions are Complex (You May Need Aspirin)

# Big Payoff

__250 XP!!!__ Need I say more? Puzzles on Codingame that offer unusually high XP are always popular. This puzzle is so creative, I am not sure it even needs the high XP.

# Visualizing the Problem

Let’s start with a quote from the problem statement:

> In this puzzle, you are given a grid representing a golf course. On each course is a certain amount of balls and an equal amount of holes. The objective is to find the route for each ball to a different hole without their paths ever crossing.

Using the analogy of laying tiles on a grid, it seems pretty obvious the grid is the map of the golf course given in the input. Per the statement above, the grid will indicate where the holes are and where the balls are. Later in the problem statement, we are told the grid also identifies water hazards and open fairway spaces.

What are the tiles we can lay down on the grid? It might be tempting to consider each individual ball movement a tile, but that would be similar to considering each square in a Shikaku rectangle a separate tile. In Shikaku, Algorithm X needed a full list of possible rectangles and each one of those rectangles, possibly covering many grid cells, is a tile that can be placed on the grid. Let’s again look to the problem statement for a hint:

>The objective is to find the route for each ball to a different hole without their paths ever crossing.

Each possible route from a ball to a hole is a tile that could be placed on the grid. Given 5 balls and 5 holes and a bunch of possible routes from the balls to the holes, Algorithm X will find a set of routes where each ball goes “to a different hole without their paths ever crossing”.

# Enumerating the Actions

I have recommended that you use human readable tuples when identifying actions for an exact cover problem and the information in those tuples need to uniquely distinguish each action from all other actions. What information is needed to uniquely identify a route? Since a route can zig and zag in all kinds of directions, the only way to uniquely identify a route is with a full set of grid coordinates that make up the route. What about short routes vs long routes? This seems like it could be challenging, and there is an easy solution.

Let’s say you have 100 possible routes from balls to holes. Give every route a unique integer ID between 1 and 100 and use that unique ID as your action in terms of Algorithm X, possible something like ('select route', bx, by, route option) where bx and by are the ball location . Remember, the mapping from actions to covered requirements is the important information. The 1s in the matrix are the powerful knowledge elements that fuel Algorithm X.

Going back to the tiles on a board analogy, each tile now has a ball location, (bx, by), and a route number on it, but what does that tile look like? Since we had to generate all the routes and we know all grid coordinates that make up each route, you can visualize each tile in the zigzagging route determined by its coordinates. Algorithm X is going to get a pile of crazy shaped zigzagging tiles to be placed on the grid, each tile representing one possible route.

Of course, you will need a data structure where you store all the cells for each route. When Algorithm X tells you route 15 the ball at (3, 4) is part of the solution, you will need to know how to display that route in your output.

To be honest, generating an exhaustive list of routes is harder than setting up Algorithm X.

# Identifying Requirements

The Winamax problem statement is very well written. From the problem statement segment above we know all ball locations must be covered and all hole locations must be covered. What about the requirement that paths never cross? Since any tow paths would cross at a single point on the grid, it sounds like any point on the grid that is not a ball or a hole does not need to be covered by any route, but if it is, it can only be covered by a single route. That appears to be a pretty straitforward optional requirement.

What about the requirement that a "ball [...] cannot stop in a water hazard."? Is that something Algorithm X needs to know about? No, it is not. This requirement is part of your algorithm that generates all possible routes from balls to holes. A route is not legitimate if any section of that route lands in a water hazard. By the time these routes get to Algorithm X, they need to be propre routes.

# Putting It All Together

Winamax is a great fit for Algorithm X. Once you separate the process of identifying routes and the process of finding a set of routs that exactly matches up the balls to holes, the problem becomes much more manageable than it might have seemed at first.

