# The Reality

Many puzzles have been discussed where it is important to make sure 2 items are not part of the same solution. Optional Requirements were used to enforce [mutual exclusivity](mutual-exclusivity). Specifically, if either `a` __or__ `b` can be part of a solution, but they cannot _both_ be part of the same solution, an additional requirement was added to the optional requirements list to enforce the needed mutual exclusivity.

What if `a` and `b` can only be part of a solution if they are __both__ part of the solution? In this case, `a` and `b` form an _all-or-none_ set of events. The set only contains two items, `a` and `b`, and only two options exist. All items in the set may be part of the solution or none of the items in the set may be part of the solution. Mutual exclusivity allows the enforcement of items that must be different. All-or-none sets of events allow the enforcement of items that must be the same.

# Quiz Time

Consider a slightly more interesting scenario with the following all-or-none sets of events:

1. `a` and `b`
1. `c` and `d`
1. `g` and `h`
1. `x` and `y`
1. `a` and `h`

?[How many all-or-none sets of events are present in this scenario?]
-[] 1 – Please make the next question harder.
-[] 2 – I’m just guessing.
-[x] 3 – I’ve always liked the number 3.
-[] 4 – I’m excluding `x` and `y` as they should only be used in math equations.
-[] 5 – Don’t insult me, I know how to count!

<br>

The correct answer is 3, but why? Any sets that intersect in any way must be joined together. Let’s rewrite the sets from 1, 3 and 5 above:

`b` and `a` . . . . . . `a` and `h` . . . . . . `h` and `g`

Any solution that has `b` must also have `a` and then must also have `h` and then must also have `g`. The same logic applies starting with `a`, `h` or `g`. Since these sets must be combined, the final 3 all-or-none sets of events are:

1. `a` and `b` and `g` and `h`
1. `c` and `d`
1. `x` and `y`

For each of the three sets above, either all members of the set must be part of a solution or none of the members must be part of a solution. For some problems, building these all-or-none sets of events can be challenging, but before we progress down that path, let’s take a look at implementation.