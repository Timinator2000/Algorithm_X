# 25x25 Sudoku

__Puzzle:__ [25x25 Sudoku](https://www.codingame.com/training/expert/25x25-sudoku)

__Author:__ [@yoch](https://www.codingame.com/profile/14a6f9fb972f723d06789c969370ff2e7411725)

__Published Difficulty:__ Very Hard

__Algorithm X Complexity:__ Should Be Straightforward, but Can Be Challenging (see below)

# Strategy

You can successfully finish 25x25 Sudoku just with what you have learned so far, but you might run into timing issues. These large Sudoku grids translate into large Algorithm X matrices that take time to process. You might find that running your code multiple times produces very different run times and there is a reason for that. To understand why that happens, it is important to identify how many rows make up the matrix for each test case.

Using the basic strategy laid out for 9x9 Sudoku, each known cell only adds one row to the matrix, while each unknown cell adds 25 rows to the matrix. Looking at each test case results in the following:

<BR>

| | Unknown Cells (U)          | Known Cells (K)              | Rows in the Matrix (25 * U + K)|
|:--|:----:|:-------------------:|:----:|
| Test Case 1: Test 1|276|349|7249|
| Test Case 2: Test 2|331|294|8569|
| Test Case 3: Test 3|324|301|8401|
| Test Case 4: Test 4|321|304|8329|
| Test Case 5: Test 5|326|299|8449|

<BR>
