# There Is No Spoon - Episode 2

Puzzle: [There Is No Spoon - Episode 2](https://www.codingame.com/training/hard/there-is-no-spoon-episode-2)

Published Difficulty: Hard

Algorithm X Complexity: Strap in and hold on tight!

# A Past Contest

Did you know [There is No Spoon]( https://www.codingame.com/contests/there-is-no-spoon/leaderboard) was a contest back in April 2015? The winner passed all test cases and validators in less than 90 minutes! The puzzle is based off the logic puzzle, [Hashiwokakero]( https://en.wikipedia.org/wiki/Hashiwokakero), which translates to “build a bridge”. You will find websites that refer to the game as “bridge building”, “bridges” or some other variation. Today, it is easy to find websites that will let you work Hashiwokakero puzzles if you’d like to get a better feel for how the game is played.

[Bridges from Simon Tatham’s Portable Puzzle Collection]( https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/bridges.html)

[Play Hashiwokakero on SilverGames.com]( https://www.silvergames.com/en/hashiwokakero)

__Codingame uses the term _LINK_ instead of the term _bridge_ to identify a connection between two nodes. From here on out, I am going to use the term _LINK_.__

# Visualizing the Problem

I believe using the analogy of tiles on a gameboard is the key to a successful Algorithm X approach to this puzzle. What does the gameboard look like? At first glance, the gameborad appears to be a blank slate with nothing except a bunch of nodes, each with a number indicating how many links need to be connected to the node.

__INITIAL GRAPHIC__

I contend there is much more to the gameboard that is subtly hidden. I will come back to that, but first we need to investigate the action steps that can be taken to create a solution. It seems straightforward the only action that we can take to work toward a solution is to put a link between two nodes, similar to this:

__LINK BETWEEN NODES__

Where do I put think? Yes, I know the link goes between two nodes, but where exactly do I place my “link tile” on the gameboard? How does the gameboard indicate to me that I can put one or two links between nodes, but I can’t put three? There is something between the nodes that isn’t explicit in the description, but it is definitely there. I’m going to call that a Channel. If I add channels to my gameboard, it now looks like this:

<BR><BR>
![Two Nodes with a Channel](TwoNodesOneChannel.png)
<BR>

I can put 0, 1 or 2 links in any Channel. Let’s add dotted lines to each Channel to represent a slot or a placeholder for a future link. My gameboard is much clearer now. To create a solution, I can put links on the board anywhere I see an open slot (dashed line) inside a channel between nodes.

__NODES WITH CHANNELS__

What about the places where channels cross? These seem to be very important locations since links are not allowed to cross each other. Any two channels that cross each other could create future problems. Channels can only cross each other at grid locations that are not Nodes. Let’s call every non-Node grid location an Intersection. Once I fully understand the layout of my gameboard, the only important Intersections will be the intersections that have crossing channels. Even then, nothing is terribly important about an Intersection until a link is place in one of the slots of a Channel. At that point, the other channel in the Intersection is no longer in play. It needs to be removed from the realm of possibility. No links an ever be placed in that second Channel.

Summarizing the gameboard now, we see:

Nodes – a location on the gameboard that needs a certain number of links.

Channels – a trench between two nodes, inside of which can be placed some number of links. A channel’s link capacity is determined by several factors discussed below, but it can never be more than 2.

Intersection – a location on the gameboard that knows about any Channel that passes through that location

Channel Capacity – in general, a Channel’s initial link capacity is determined by the following formula: `minimum(2, node1 links needed, node 2 links needed)`. There are two important exceptions to that rule.

Exception #1: In the above diagram, each Node connected by the Channel needs 1 link. If these are the only two Nodes in the puzzle, the Channel capacity is 1. If there are more than two Nodes in the puzzle, the Channel capacity is zero since putting a link between the two nodes would create a connected group that could not be connected to the rest of the puzzle.

Exception #2: In the above diagram, each Node connected by the Channel needs 2 links. If these are the only two Nodes in the puzzle, the Channel capacity is 2. If there are more than two Nodes in the puzzle, the Channel capacity is 1 since putting two links between the two nodes would create a connected group that could not be connected to the rest of the puzzle.

What does our gameboard look like now?

__FINAL GAMEBOARD__








# To Figure Out

This might be the toughest Algorithm X puzzle on Codingame. Using the techniques covered so far, you can solve most of the test cases. However, Test Case 8: Advanced and Test Case 13: Expert are just too big to solve purely with backtracking. A little later in the playground, I will cover problem-space reduction, and I’ll revisit this puzzle with a few more ideas that might help you find the finish line.

Let’s first talk about Test Cases 1 through 7, 9 and 10. They can all be solved with Algorithm X by following the processes covered in the Mrs. Knuth puzzles, but it will not be easy.

Lot’s of challenging multiplicity.


Algorithm X will generate multiple solutions for Test Cases 11 and 12 and you will need to determine which solution has a __single connected group__ of nodes.



Backtracking is guessing. Using only logic, no backtracking at all, you can solve 1 – 8 and 10.

Only a combination of pre-backtracking logic and Algorithm X can solve all the test cases.

