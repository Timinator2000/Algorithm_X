# Welcome!

A quick Google search will surely bring you to countless implementations of Algorithm X, usually solving a 9x9 Sudoku grid using the famous Dancing Links (DLX) technique proposed by the brilliant Donald Knuth. This playground is NOT just another Sudoku demonstration. Rather, the goal here is to go deeper and explore using Algorithm X to teach both reusable problem solving techniques and reusable software architectures. By the time you're finished working your way through the material, you should feel confident solving any exact cover problem you run across!


__What to Expect__

This tutorial is broken into the following topics:

__Try to Add a Project__

@[Luke, how many stars are there in these galaxies?]({"stubs": ["universe.py"], "command": "python3 test_universe.py"})


__Understanding Algorithm X__

Part I - need to address MRV vs MRV for column selection and point out that MRV is the default for my AlgorithmX Solver.

Part II - Two ways to implement secondary constraints. Adjust the algorithm so that secondary constraints are never selected and they never cause failure. Or, add a row to the matrix for each secondary constraint where the only column covered is that specific constraint. It essentially says, "If no other action covers this row, select this action that only covers this one single constraint."

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

