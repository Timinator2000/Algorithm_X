# Optimized Coloring

__Puzzle:__ [Optimized Coloring](https://www.codingame.com/training/medium/optimized-coloring)

__Author:__ [@Oflopy78](https://www.codingame.com/profile/78597a36a97776323b29c41b0e314f1c8444555)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ If At First You Don't Succeed, Try Again!

# Identifying Zones

Before putting any thought into an Algorithm X approach to this puzzle, the cells of the picture must be organized into zones. From the problem statement:

>Having an empty sheet of paper divided into some zones

>A zone is made of "space" characters.

I will move forward assuming you have created a list of zones where each zone is a list of row, col `(r, c)` `tuple`s. Each `(r, c)` `tuple` identifies one “space” character found in the zone. Again from the problem statement:

>two adjacent zones must be filled with two different colors.

Let’s call “two adjacent zones” a set of neighbors and let’s rephrase the statement above as:

>two neighbors must never be filled with the same color

Algorithm X needs to know every set of neighbor zones so it can make sure no neighbors are ever assigned the same color. And, how do we ensure something doesn’t happen? Correct! Mutual exclusivity.

<details>
<summary>Spoiler Alert: Python suggestions for finding neighbor zones.</summary>
<br>

You need to look at every combination of 2 zones and determine if those two zones are neighbors. This is a great opportunity to use `itertools.combinations`.

```python
# assumed data structure
# zones : List[List[tuple]] – each zone in zones is a list if (r, c) tuples

from itertools import combinations

neighbors = []
for zone_1, zone_2 in combinations(zones, 2):
    for (r1, c1) in zone_1:
        for (r2, c2) in zone_2:
            if the two cells indicate the zones are neighbors:
                add (zone_1, zone_2) to the list of neighbors
                stop checking and move on to the next combination of zones
```

If you really want to make your code “Pythonic”, try this:

```python
# assumed data structure
# zones : List[List[tuple]] – each zone in zones is a list if (r, c) tuples

from itertools import combinations

neighbors = []
for zone_1, zone_2 in combinations(zones, 2):
    if any((r1, c1, r2, c2 indicate zones are neighbors) for (r1, c1) in zone_1 for (r2, c2) in zone_2):
        add (zone_1, zone_2) to the list of neighbors
```

The code is still very readable, but the use of `any` has shortened the code and eliminated the need to do further checking to break out of the nested `for` loops.
</details>

In the Python code above, I have intentionally left out the details needed to replace `(r1, c1, r2, c2 indicate zones are neighbors)` with code. Several CodinGamers have asked for clarification on how to determine when two zones are neighbors and when they are not neighbors. Almost every puzzle on CodinGame has a discussion tab and if you need more help determining neighbors, click [here]( https://www.codingame.com/training/medium/optimized-coloring/discuss) to open this puzzle’s discussion tab.

# Algorithm X Setup


