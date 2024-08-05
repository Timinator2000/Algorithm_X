# Multiplicity

Mrs. Knuth is moving up the ladder at school and she is once again requesting changes. All the details are found here:

[Mrs. Knuth - Part III](https://www.codingame.com/contribute/view/959460130d2f9792d933f75838edb639a6dae)

There seems to be a lot of new information in the puzzle, but only this key paragraph affects our Algorithm X approach:

_Mrs. Knuth has received some wonderful news! This summer, she will only be working with a handful of honor students. Although she'll have fewer students, each student is now allowed to request multiple hours of instruction per week. This creates a situation where many potential schedules exist. Based on her preferences, Mrs. Knuth needs you to find the best schedule possible._

Let's jump right into the example:

```
M 8 Tu 8 W 8 Th 8 F 8 9 10 11 1
3
Drew Trombone 1 M Tu W Th F 10 11
Ella Flute 2 M 8 Tu 8 W Th F 11
Lola Drums 1 M Tu W Th F 11 1
1
Drew Ella
```

Ella wants two lessons! How can such a little change make such an impact on our existing algorithms? In each of the previous two Mrs. Knuth puzzles, we would have identified the following three requirements:

```text
('student scheduled', 'Drew')
('student scheduled', 'Ella')
('student scheduled', 'Lola')
```

Until now, requirements needed to be covered exactly once, but now the Emma requirement needs to be covered twice and in future test cases, students are request even more than 2 hours of instruction. Houston, we have a problem.

In his book, [The Art of Computer Programming](https://www-cs-faculty.stanford.edu/~knuth/taocp.html), Donald Knuth discusses Algorithm M for handling problems with requirements/constraints that might need to be covered multiple time and I suggest you add learning about Algorithm M to your to-do list. However, this playground is an Algorithm X tutorial and an overarching goal of mine is to explore how much we can accomplish with one, out-of-the-box AlgorithmXSolver!
