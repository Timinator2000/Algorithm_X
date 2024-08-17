# There Is No Spoon - Episode 2 - Setting Up Algorithm X

Let's take another look at the Object-Oriented Design model. Everything Algorithm X needs is right here:

<BR><BR>
![No Spoon 2 - OOD](ClassesWithLists.png)
<BR>

This might be the toughest Algorithm X puzzle on Codingame due to the amount of multiplicity. The requirements are straightforward. Just like Emma needed some number of lessons for Mrs. Knuth – Part III, each Node needs some number of links.

__Step 1:__ Loop through all Nodes and create the appropriate requirements.

Let’s dig a bit deeper into the actions. As mentioned earlier, all actions involve putting some link between two Nodes, but what does that actually look like? Looking at the gameboard, the link must be placed in a specific slot and it needs to be tied to one of the link requirements for each node. Looks like triple multiplicity, doesn’t it!

__Step 2:__ Loop through all Channels and create the appropriate actions, including the lists of requirements covered by each action. Make sure you properly handle all the multiplicity.

What about those pesky Intersections? Putting a link in a Channel might eliminate any possibility of putting links in a crossing Channel. Sounds like textbook mutual exclusivity, right? You’ll need to create optional requirements to handle all the mutual exclusivity.

__Step 3:__ Loop through all Intersections and create the appropriate optional requirements to handle all mutual exclusivity created by Channels that pass through the same Intersection.

__Step 4:__ Make sure all the proper `me_requirements` are added to the lists of requirements covered by the actions that cover them. If you use the code structure recommended in Mrs. Knuth – Part III, make sure you append the `me_requirements` to the rest of the `optional_requirements` before invoking the inherited AlgorithmXSolver constructor.

# Your Goal

Using the techniques covered so far, you can solve most of the test cases for this puzzle, but you cannot solve them all. Test Case 8: Advanced and Test Case 13: Expert are just too big to solve purely with backtracking. In the next section, I will cover problem-space reduction, and I’ll revisit this puzzle with a few more ideas that might help you find the finish line. Before moving on, let’s discuss a few things about the test cases you should be able to solve.

__Test Cases 1 through 7, 9 and 10:__ These can all be solved with Algorithm X by following the processes covered in the Mrs. Knuth puzzles and the guidelines given here.

__Test Cases 11 and 12:__ Algorithm X will generate multiple solutions and you will need to determine which solution has a __single connected group__ of nodes. Just like in Mrs. Knuth – Part III, this is a perfect opportunity to override the AlgorithmXSolver method `_process_solution(self)`. If the solution if valid, you do not need to do anything. The solver will `yield` the solution just as expected. If the solution is not valid, add the following line before exiting the method to tell Algorithm X this solution is not valid and should not be included in the solution generator.

```python
self.solution_is_valid = False
```

In the next section, I’ll discuss how to solve part of a problem with logic so that the task given to Algorithm X is more manageable. Much of There is No Spoon – Episode 2 can be solve with only logic, no backtracking. However, only a combination of logical problem-space reduction and backtracking can solve all test cases and validators.
