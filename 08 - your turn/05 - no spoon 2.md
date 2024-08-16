# There Is No Spoon - Episode 2

__Puzzle:__ [There Is No Spoon - Episode 2](https://www.codingame.com/training/hard/there-is-no-spoon-episode-2)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Strap in and hold on tight!

# A Past Contest

[There is No Spoon]( https://www.codingame.com/contests/there-is-no-spoon/leaderboard) was a contest in April 2015 and the winner passed all test cases and validators in less than 90 minutes! The puzzle is based on the logic puzzle, [Hashiwokakero]( https://en.wikipedia.org/wiki/Hashiwokakero), which translates to “build a bridge”. You will find websites that refer to the game as “bridge building”, “bridges” or some other variation. Today, it is easy to find websites that will let you work Hashiwokakero puzzles if you’d like to get a better feel for how the game is played.

[Bridges from Simon Tatham’s Portable Puzzle Collection]( https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/bridges.html)

[Play Hashiwokakero on SilverGames.com]( https://www.silvergames.com/en/hashiwokakero)

__Codingame uses the term _LINK_ instead of the term _bridge_ to identify a connection between two nodes. From here on out, I am going to use the term _LINK_.__

# Visualizing the Problem

I believe using the analogy of tiles on a gameboard is the key to a successful Algorithm X approach to this puzzle. What does the gameboard look like? At first glance, the gameborad appears to be a blank slate with nothing except a bunch of nodes, each with a number indicating how many links need to be connected to the node.

<BR><BR>
![Initial Gameboard](Nodes.png)
<BR>

I contend there is much more to the gameboard that is subtly hidden. I will come back to that, but first we need to investigate the action steps that can be taken to create a solution. It seems straightforward the only action we can take to work toward a solution is to put a link between two nodes, similar to this:

<BR><BR>
![Two Nodes with a Link](TwoNodesOneLink.png)
<BR>

Where do I put the link? Yes, I know the link goes between the two nodes, but where exactly do I place my “link tile” on the gameboard? How does the gameboard indicate to me that I can put one or two links between nodes, but I cannot put three? There is something between the nodes that is not explicit in the description, but it is definitely there. I’m going to call this space between nodes, where a link can be placed, a Channel.

<BR><BR>
![Two Nodes with a Channel](TwoNodesOneChannel.png)
<BR>

I can put 0, 1 or 2 links in any Channel. Let’s add dotted lines to each Channel to represent a slot or a placeholder for a future link. My gameboard is much clearer now. To create a solution, I can put links on the gameboard anywhere I see an open slot (dashed line) inside a channel between nodes.

<BR><BR>
![Two Nodes with a Channel and Slots](TwoNodesOneChannelWithSlots.png)
<BR>

What about the places where channels cross? These seem to be very important locations since links are not allowed to cross each other. Any two channels that cross each other could create future problems. Channels can only cross each other at grid locations that are not Nodes. Let’s call every non-Node grid location an Intersection and build our full gameboard from scratch, starting with just Nodes and Intersections:

<BR><BR>
![Nodes and Intersections](NodesAndIntersections.png)
<BR>

Once I fully understand the layout of my gameboard, the only important Intersections will be the intersections that have crossing channels. Even then, nothing is terribly important about an Intersection until a link is place in one of the slots of a Channel. At that point, the other channel in the Intersection is no longer in play. It needs to be removed from the realm of possibility. No links can an ever be placed in the second Channel.

This next diagram displays the entire gameboard before any links are placed. For just a minute, consider how much more detailed this gameboard is compared to the original gameboard. No actions have been taken. No links have been placed. We have only taken the time to build a more detailed, and possibly more meaningful, understanding of the gameboard.

<BR><BR>
![Full Gameboard](FullGameboard.png)
<BR>

Summarizing the gameboard now, we see the following components:

__Node__ – a location on the gameboard that needs a certain number of links.

__Channel__ – a trench between two nodes, inside of which can be placed some number of links. A channel’s link capacity is determined by several factors discussed below, but it can never be more than 2.

__Intersection__ – a location on the gameboard that knows about any Channel that passes through that location

__Channel Capacity__ – in general, a Channel’s initial link capacity is determined by the following formula: `minimum(2, node1 links needed, node 2 links needed)`. There are two important exceptions to that rule.


<BR><BR>
![Two Power 1 Nodes](TwoPower1Nodes.png)
<BR>

_Exception #1_: In the above diagram, each Node connected by the Channel needs 1 link. If these are the only two Nodes in the puzzle, the Channel capacity is 1. If there are more than two Nodes in the puzzle, the Channel capacity is zero since putting a link between the two nodes would create a connected group that could not be connected to the rest of the puzzle.

<BR><BR>
![Two Power 2 Nodes](TwoPower2Nodes.png)
<BR>

_Exception #2_: In the above diagram, each Node connected by the Channel needs 2 links. If these are the only two Nodes in the puzzle, the Channel capacity is 2. If there are more than two Nodes in the puzzle, the Channel capacity is 1 since putting two links between the two nodes would create a connected group that could not be connected to the rest of the puzzle.

# Object-Oriented Analysis

Object-Oriented Programming is a popular topic in the world of Computer Science, but how did it come about? Thought leaders believe the world we live in is object-oriented and matching our programming style to the world we observe has benefits. I contend we have just finished building an object-oriented understanding of our problem space. Next, I'll show you how to turn that _Object-Oriented Analysis_ into an _Object-Oriented Design_ that makes the job of identifying actions and requirements for Algorithm X significantly easier than it probably seemed at first.








# To Figure Out

This might be the toughest Algorithm X puzzle on Codingame. Using the techniques covered so far, you can solve most of the test cases. However, Test Case 8: Advanced and Test Case 13: Expert are just too big to solve purely with backtracking. A little later in the playground, I will cover problem-space reduction, and I’ll revisit this puzzle with a few more ideas that might help you find the finish line.

Let’s first talk about Test Cases 1 through 7, 9 and 10. They can all be solved with Algorithm X by following the processes covered in the Mrs. Knuth puzzles, but it will not be easy.

Lot’s of challenging multiplicity.


Algorithm X will generate multiple solutions for Test Cases 11 and 12 and you will need to determine which solution has a __single connected group__ of nodes.



Backtracking is guessing. Using only logic, no backtracking at all, you can solve 1 – 8 and 10.

Only a combination of pre-backtracking logic and Algorithm X can solve all the test cases.

