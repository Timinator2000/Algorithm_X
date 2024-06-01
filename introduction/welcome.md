# Welcome!

A quick Google search will surely bring you to countless implementations of Algorithm X, usually solving a 9x9 Sudoku grid using the famous Dancing Links (DLX) technique proposed by the brilliant Donald Knuth. This playground is NOT just another Sudoku demonstration. Rather, the goal here is to go deeper and explore using Algorithm X to teach both reusable problem solving techniques and reusable software architectures. By the time you're finished working your way through the material, you should feel confident solving any exact cover problem you run across!


__What to Expect__

This tutorial is broken into the following topics:

__Try to Add a Project__

@[Luke, how many stars are there in these galaxies?]({"stubs": ["universe.py"], "command": "python3 test_universe.py"})


__Understanding Algorithm X__

Part I - need to address MRV vs MRV for column selection and point out that MRV is the default for my AlgorithmX Solver.

Part II - Two ways to implement secondary constraints. Adjust the algorithm so that secondary constraints are never selected and they never cause failure. Or, add a row to the matrix for each secondary constraint where the only column covered is that specific constraint. It essentially says, "If no other action covers this row, select this action that only covers this one single constraint."

From conversation with Lisa:

Exact Cover refers to types of problems/puzzles that can be modeled as a system of constraints and options. I prefer the words requirements and actions. If you can build a model of requirements and actions, Donald Knuth’s Algorithm X will find the solution(s). Still, what does that mean? Let’s look at Mrs. Knuth’s scheduling problem.

Requirements - what are the requirements that must be satisfied by a solution to the problem? For Mrs. Knuth’s schedule, there are 3 distinct types of requirements.

* Each slot in the schedule must be filled.
* Each student must be put somewhere on the schedule.
* Each day must have one and only one student for each instrument type.
* How many total requirements are there in the example problem? Mrs. Knuth is only teaching 3 total hours and all those hours are on the same day. There are 3 slots that must be filled. There are 3 students that must be placed on the schedule and there are 3 instruments types that must show up somewhere on the day she is teaching. There are 9 total requirements for the example problem. (In my playground, I will discuss how to properly construct a requirement and I will provide the details of exactly how I suggest defining all 9 requirements.)

What are the actions that can be taken to try to solve the problem. There are only 5 possible actions. Ayla could be scheduled Thursday at 2pm. Bob could be schedule Thursday at 2pm or at 3pm. Alex could be scheduled at 2pm or 4pm.

Each of those 5 actions will satisfy some of the requirements, but no single action will satisfy all of the requirements of course. Given a list of requirements, a list of actions and the mapping that identifies which requirements are satisfied by each action, Donald Knuth’s Algorithm X will quickly and efficiently determine all sets of actions that “exactly cover” the requirements.

What does it mean to “exactly cover”? It means that all requirements must be satisfied by one and only one of the actions. No two actions in the solution are allowed to satisfy the same requirement. Going back to Mrs. Knuth, Algorithm X ensures that scheduling Bob on Thursday at 2pm and scheduling Alex on Thursday at 2pm never show up together in the same solution. They both satisfy the same requirement of scheduling somebody during the 2pm Thursday slot.

That was a long answer to your short question, but I will now copy everything I just wrote into my playground. Let me know how it hits you.

My goal is to teach the processes of distinguishing requirements and actions. I will provide a complete black box Algorithm X Solver. The user will be able to feed the requirements and actions into the solver and the solver will return a list of actions that produce a solution. I truly believe I can make some pretty tough Codingame puzzles very doable for anybody that wants to give it a try.

Everything on the Internet about Exact Cover and Algorithm X is primarily focused on writing the code to implement Donald Knuth’s Dancing Links (DLX). In the real world, we only need one genius to code up the algorithm while we need hundreds or thousands of ordinary engineers to build models of problems and feed those models into the algorithm.

By the way…I am not the “genius” that coded up the algorithm. I copied the main engine from some code written by RoboStac. I made it into a reusable black box and hopefully built a wrapper to make it easy to use, but I am just one of the 100s or 1000s of ordinary engineers. I just happen to love building models.

For a more mathematical discussion of Exact Cover and Algorithm X, I suggest Wikipedia. (fyi - the formal math makes my head hurt, but I do like the example with the matrix):

Wikipedia - Exact Cover 1

__Using Algorithm X__

Text here.

__Building a Black Box Algorithm X Solver__

Text here.

__18 Different Exact Cover Problems__

__Music Schedules Part I__

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

__Music Schedules Part II__

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

__Music Schedules Part III__

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


__Example of Runnable Text Block__
```python runnable
print('Hello World')
```

