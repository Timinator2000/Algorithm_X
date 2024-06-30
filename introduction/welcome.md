# Welcome!

A quick Google search will surely bring you to countless implementations of Algorithm X, usually solving a 9x9 Sudoku grid using the famous Dancing Links (DLX) technique proposed by the brilliant Donald Knuth. This playground is NOT just another Sudoku demonstration. Rather, the goal here is to go deeper and explore using Algorithm X to teach both reusable problem solving techniques and reusable software architectures. By the time you're finished working your way through the material, you should feel confident solving any exact cover problem you run across!

## What to Expect

This tutorial is broken into the following topics:

## Try to Add a Project

@[Luke, how many stars are there in these galaxies?]({"stubs": ["universe.py"], "command": "python3 test_universe.py"})

## Regarding MRV vs non-MRV

* My AlgorithmXSolver uses MRV by default.
* I recommend always trying MRV first.
* My AlgorithmXSolver makes it very easy to customize the order in which columns are chosen.

## Understanding Algorithm X

Part I - need to address MRV vs MRV for column selection and point out that MRV is the default for my AlgorithmX Solver.

Part II - Two ways to implement secondary constraints. Adjust the algorithm so that secondary constraints are never selected and they never cause failure. Or, add a row to the matrix for each secondary constraint where the only column covered is that specific constraint. It essentially says, "If no other action covers this row, select this action that only covers this one single constraint."

From conversation with Lisa:

Exact Cover refers to types of problems/puzzles that can be modeled as a system of constraints and options. I prefer the words requirements and actions. If you can build a model of requirements and actions, Donald Knuth’s Algorithm X will find the solution(s). Still, what does that mean? Let’s look at Mrs. Knuth’s scheduling problem.

Requirements - what are the requirements that must be satisfied by a solution to the problem? For Mrs. Knuth’s schedule, there are 3 distinct types of requirements.

* Each slot in the schedule must be filled.
* Each student must be put somewhere on the schedule.
* Each day must have one and only one student for each instrument type.

How many total requirements are there in the example problem? Mrs. Knuth is only teaching 3 total hours and all those hours are on the same day. There are 3 slots that must be filled. There are 3 students that must be placed on the schedule and there are 3 instruments types that must show up somewhere on the day she is teaching. There are 9 total requirements for the example problem. (In my playground, I will discuss how to properly construct a requirement and I will provide the details of exactly how I suggest defining all 9 requirements.)

What are the actions that can be taken to try to solve the problem. There are only 5 possible actions. Ayla could be scheduled Thursday at 2pm. Bob could be schedule Thursday at 2pm or at 3pm. Alex could be scheduled at 2pm or 4pm.

Each of those 5 actions will satisfy some of the requirements, but no single action will satisfy all of the requirements of course. Given a list of requirements, a list of actions and the mapping that identifies which requirements are satisfied by each action, Donald Knuth’s Algorithm X will quickly and efficiently determine all sets of actions that “exactly cover” the requirements.

What does it mean to “exactly cover”? It means that all requirements must be satisfied by one and only one of the actions. No two actions in the solution are allowed to satisfy the same requirement. Going back to Mrs. Knuth, Algorithm X ensures that scheduling Bob on Thursday at 2pm and scheduling Alex on Thursday at 2pm never show up together in the same solution. They both satisfy the same requirement of scheduling somebody during the 2pm Thursday slot.

That was a long answer to your short question, but I will now copy everything I just wrote into my playground. Let me know how it hits you.

My goal is to teach the processes of distinguishing requirements and actions. I will provide a complete black box Algorithm X Solver. The user will be able to feed the requirements and actions into the solver and the solver will return a list of actions that produce a solution. I truly believe I can make some pretty tough Codingame puzzles very doable for anybody that wants to give it a try.

Everything on the Internet about Exact Cover and Algorithm X is primarily focused on writing the code to implement Donald Knuth’s Dancing Links (DLX). In the real world, we only need one genius to code up the algorithm while we need hundreds or thousands of ordinary engineers to build models of problems and feed those models into the algorithm.

By the way…I am not the “genius” that coded up the algorithm. I copied the main engine from some code written by RoboStac. I made it into a reusable black box and hopefully built a wrapper to make it easy to use, but I am just one of the 100s or 1000s of ordinary engineers. I just happen to love building models.

For a more mathematical discussion of Exact Cover and Algorithm X, I suggest Wikipedia. (fyi - the formal math makes my head hurt, but I do like the example with the matrix):

Wikipedia - Exact Cover 1

## Using Algorithm X

Text here.

## Building a Black Box Algorithm X Solver__

Text here.

## 18 Different Exact Cover Problems

[Constrained Latin Squares]( https://www.codingame.com/training/medium/constrained-latin-squares) (+50 XP)
<BR>[Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver) (+50 XP)
<BR>[16x16 Sudoku]( https://www.codingame.com/training/medium/16x16-sudoku) (+50 XP)
<BR>[Futoshiki Solver](https://www.codingame.com/training/medium/futoshiki-solver) (+50 XP)
<BR>[Shikaku Solver](https://www.codingame.com/training/medium/shikaku-solver) (+50 XP)
<BR>[Dumbbells Solver](https://www.codingame.com/training/hard/dumbbells-solver) (+50 XP)
<BR>[Dominoes Solver](https://www.codingame.com/training/hard/dominoes-solver) (+50 XP)
<BR>[Mini Sudoku Solver]( https://www.codingame.com/training/hard/mini-sudoku-solver) (+50 XP)
<BR>[Winamax]( https://www.codingame.com/training/hard/winamax-sponsored-contest) (+250 XP)
<BR>[Three Little Piggies]( https://www.codingame.com/training/hard/three-little-piggies) (+50 XP)
<BR>[Takuzu Solver]( https://www.codingame.com/training/hard/takuzu-solver) (+50 XP)
<BR>[Hitori Solver]( https://www.codingame.com/training/hard/hitori-solver) (+50 XP)
<BR>[Kakuro Solver]( https://www.codingame.com/training/hard/kakuro-solver) (+50 XP)
<BR>[n Queens]( https://www.codingame.com/training/hard/n-queens) (+50 XP)
<BR>[There Is No Spoon – Episode 2]( https://www.codingame.com/training/hard/there-is-no-spoon-episode-2) (+250 XP)
<BR>[Einstein’s Riddle Solver]( https://www.codingame.com/training/hard/einsteins-riddle-solver) (+50 XP)
<BR>[Breaking Bifid]( https://www.codingame.com/training/hard/breaking-bifid) (+50 XP)
<BR>[High-Rise Buildings](https://www.codingame.com/training/expert/high-rise-buildings) (+50 XP)

[25x25 Sudoku](https://www.codingame.com/training/expert/25x25-sudoku) (+50 XP)
<BR>[Killer Sudoku Solver](https://www.codingame.com/training/medium/killer-sudoku-solver) (+50 XP)
<BR>[Killer Sudoku Extreme Challenge](https://www.codingame.com/training/hard/killer-sudoku-extreme-challenge) (+50 XP)
<BR>[Tetris Floor](https://www.codingame.com/training/hard/tetris-floor) (+50 XP)






## Music Schedules Part I

Number of Iterations without using Day-Instrument Constraint:

Test Case 5 - 96

Test Case 6 - 63

Test Case 7 - 1818

Test Case 8 - 1387

Test Case 9 - 11414

Test Case 10 - 10691

Test Case 11 - 130235

Test Case 12 - 83620

Test Case 13 - stopped counting at 500k

Test Case 14 - stopped counting at 500k

## Music Schedules Part II

Number of Iterations without using checking Troublesome Pairs and Loud Instruments:

Test Case 1 - 3

Test Case 2 - 4

Test Case 3 - 10

Test Case 4 - 4

Test Case 5 - 27

Test Case 6 - 18

Test Case 7 - 94

Test Case 8 - 78

Test Case 9 - 290

Test Case 10 - 321

Test Case 11 - 362

Test Case 12 - 140

Test Case 13 - 5578

Test Case 14 - 2205

Test Case 15 - 114

Test Case 16 - 98

Test Case 17 - 7738

Test Case 18 - 4882

Test Case 19 - 25281

Test Case 20 - 20433

Test Case 21 - 65887

Test Case 22 - 53101

## Music Schedules Part III

Number of possibilities without multiplicity adaptation:

Test Case 1 - 

Test Case 2 - 

Test Case 3 - 

Test Case 4 - 

Test Case 5 - 

Test Case 6 - 

Test Case 7 - 

Test Case 8 - 

Test Case 9 - 

Test Case 10 - 

Test Case 11 - 

Test Case 12 - 

Test Case 13 - 

Test Case 14 - 

Test Case 15 - 

Test Case 16 - 

Test Case 17 - 

Test Case 18 - 

Test Case 19 - 

Test Case 20 - 

Test Case 21 - 

Test Case 22 - 


## Example of Runnable Text Block
```python runnable
print('Hello World')
```


## Overview of Puzzles

___Part I:___ Goal is to introduce requirements and actions (columns and rows)
- primary constraints only
- slots = students
- unique instrument count per day == slots per day

___Part II:___ Goal is to introduce at ost one-time constraints and mutually exclusive actions
- optional constraints
- more slots than students
- troublesome pairs
- loud instruments cannot be back-to-back

___Part III:___ Goal is to introduce multiplicity and evaluating all solutions to find the best
- still more slots than students
- possible multiple hours per student
- need to find the best of all solutions

___Part IV:___ Goal is to introduce mutually inclusive actions and redirection of Algorithm X path finding
- sibling pairs - mutually inclusive actions
- mornings/afternoons must be one of ... {BGBG, GBGBG, BGGB} since boys tend to require more energy than girls at this age.

___Other Ideas___
- find the best schedule if not all students need to be scheduled and not all slots need to be filled