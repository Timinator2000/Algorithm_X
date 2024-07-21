# Background

[Ali Assaf]( https://www.cs.mcgill.ca/~aassaf9/index.html)’s [Algorithm X in 30 Lines!]( https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html) played a huge part in my initial attempt to build a reusable AlgorithmXSolver. I wrapped Assaf's code inside of an AlgorithmXSolver class that I could initialize with a list of requirements and a dictionary of actions. Each action (key) in the dictionary had a list of requirements covered by that action. Although I had good success with that solver, I knew I eventually wanted to implement Donald Knuth's [Dancing Links (DLX)]( https://en.wikipedia.org/wiki/Dancing_Links).

I have learned a ton these past several years looking at other Codingamers' solutions after I submit a solution to a puzzle. I noticed @RoboStac had implemented DLX for Constrained Latin Squares. I eventually took that code and, essentially, swapped out the engine of my AlgorithmXSolver. The interfaces remained the same, but I now had better horsepower under the hood!

Here's the best news of all. You are welcome to study DLX and implement it yourself, but you don't need to do that to solve all the puzzles on @5DN1L's list. I'm going to give you my AlgorithmXSolver. Would it be beneficial to study DLX and implement it yourself. Absolutely! However, this playground is not about coding up DLX. This playground is about building models that Algorithm X can easily digest and solve. In the big picture of life, DLX only needs to be implemented one time, while the number of problems that might need to be modeled and solved is endless.

# Using the AlgorithmXSolver Class

If you use my AlgorithmXSolver, you will need to copy the code into your coding environment. In this playground, I am able to simplify things by using the following import statement.

```python
from AlgorithmX import AlgorithmXSolver
```

__This import statement will not work in your coding environment. You will need to copy all of the following code into your source file.__

```python
#  This solution uses Knuth's Algorithm X and his Dancing Links (DLX):
#  (DLX Based Algorithm X Solver Last Revised 06/02/2024)
#
#   https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
#
#  June 02, 2024 - history added to allow subclasses to make adaptations for multiplicity.
#                - giving this Solver similar functionality to Knuth's Algorithm M.
#
```
