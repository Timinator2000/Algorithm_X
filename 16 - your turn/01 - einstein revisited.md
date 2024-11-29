# Einstein's Riddle Solver (Revisited)

__Puzzle:__ [Einstein's Riddle Solver](https://www.codingame.com/training/hard/einsteins-riddle-solver)

__Author:__ [@OroshiX](https://www.codingame.com/profile/045d3b89723c9acafb728c9fd1d8cb297970931)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ No More Perspective Shift Needed

# Memory Refresh

Einstein’s Riddle Solver is unique because some characteristics _must_ be the same and other characteristics _must not_ me the same. In the [original discussion](einsteins-riddle-solver), I suggested converting all characteristics that must be the same into a group of characteristics that must be different. In that way, all characteristic relationships could be handled with option requirements used to implement [mutual exclusivity]( mutual-exclusivity). Let’s now consider solutions for Einstein’s Riddle Solver that use [coloring]( all-or-none-with-colors) or [complex actions](complex-actions) to enforce sameness.

Einstein’s Riddle Solver is extremely similar to [scavenger hunt](all-or-none-sets-of-events) presented in the previous section, with one key difference. The scavenger hunt did not have any mutual exclusivity. The scavenger hunt can be thought of as a grid, just like the gameboard and tiles analogy proposed in the original Einstein discussion. In the scavenger hunt, each child already has a grade level, but must be assigned a team color. In the Einstein puzzle, each characteristic already has a row and must be assigned a column.

# All-Or-None Sets of Characteristics

Because every characteristic must be accounted for, start with a list of sets where each set contains exactly one characteristic. Then, add another set to the list for each group of 2 characteristics that must be the same. The last step is to combine the all-or-none sets that overlap, per the skills practice on the [previous page](test-your-skills). In the end, you will have some sets with multiple characteristics that must be the same and several sets that still only contain a single characteristic, meaning that characteristic is not required to be the same column as any other characteristic.

# Enforcing Sameness with Colors

To build a solution using colors, you will follow the same steps used to build a solution for the scavenger hunt to add the coloring mechanisms. Other than that, handling the mutually exclusive characteristics does not change from the original discussion.

# Enforcing Sameness with Complex Actions

Again, building Einstein’s complex actions is almost the exact same process as described in the scavenger hunt. With complex actions, tremendous care must be taken when identifying the requirements covered by each complex action. Don not overlook the `me requirements` for each simple action that is part of the complex action.

# Comparison

The following table compares my solvers using each of the three techniques discussed here. It is important to remember my solution with coloring is an Algorithm X solution, _adapted_ for coloring. It is not an implementation of Donald Knuth’s Algorithm C.

| Sameness Enforce With | Actions | me_requirements | Execution Time |
|:------|:------:|:------:|:------:|
| Test Case 1 |  |  |  |
| Mutual Exclusivity | 0 | 0 | 0 |
| Colors | 0 | 0 | 0 |
| Complex Actions | 0 | 0 | 0 |
| Test Case 1 |  |  |  |
| Mutual Exclusivity | 0 | 0 | 0 |
| Colors | 0 | 0 | 0 |
| Complex Actions | 0 | 0 | 0 |
