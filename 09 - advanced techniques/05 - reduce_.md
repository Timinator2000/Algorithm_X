# This Will Be Important Later

You may have already finished all the Sudoku puzzles without any problem-space reduction. I strongly suggest you consider following through with what I'm about to suggest and the reason is because of [Killer Sudoku Solver](https://www.codingame.com/training/medium/killer-sudoku-solver) and [Killer Sudoku Extreme](https://www.codingame.com/training/hard/killer-sudoku-extreme-challenge). 100% of any effort you put forward on this exercise will benefit you when you solve the Killer Sudoku puzzles, which begin with all the same rules as Sudoku and then add a few details you can tackle later.

# Initial Challenge

My initial challenge is for you implement the reduction technique coverd in the previous pages. On the website [Learn-Sudoku.com](https://learn-sudoku.com), this technique is referred to as [Lone Singles](https://learn-sudoku.com/lone-singles.html). For any cell that has been reduced to a single candidate, that value may be removed from the candidate lists of all other cells in the same groups. With just this one reduction technique, you can achieve the following results on each of the [Codingame](https://www.codingame.com/) Sudoku puzzles...without any backtracking.

<BR>

| Puzzle | Results                                |
|:--|:------------------------------------------------------------------|
|[Sudoku Solver](https://www.codingame.com/training/medium/sudoku-solver)|<BR><span style="color:green">✅ Test Case 1: Very Easy</span><BR><span style="color:red">❌ Test Case 2: Easy - Oh, so close!<BR>❌ Test Case 3: Intermediate/Hard - Minimal reduction.<BR>❌ Test Case 4: World's Hardest Sudoku - No reduction at all.<BR><BR></span>|
|[16x16 Sudoku Solver](https://www.codingame.com/training/medium/16x16-sudoku)|<BR><span style="color:green">✅ Test Case 1: Test 1<BR>✅ Test Case 2: Test 2</span><BR><span style="color:red">❌ Test Case 3: Test 3 - Minimal reduction.<BR>❌ Test Case 4: Test 4 - Minimal reduction.<BR>❌ Test Case 5: Test 5 - Minimal reduction.<BR>❌ Test Case 6: Test 6 - Minimal reduction.<BR><BR></span>|
|[25x25 Sudoku Solver](https://www.codingame.com/training/expert/25x25-sudoku)|<BR><span style="color:red">❌ Test Case 1: Test 1<BR>❌ Test Case 2: Test 2<BR>❌ Test Case 3: Test 3 - Minimal reduction.<BR>❌ Test Case 4: Test 4 - Minimal reduction.<BR>❌ Test Case 5: Test 5 - Minimal reduction.<BR><BR><BR></span>|
|[Mini Sudoku Solver](https://www.codingame.com/training/hard/mini-sudoku-solver)|<BR><span style="color:green">✅ Test Case 1: Test 1<BR>✅ Test Case 2: Test 2</span><BR>✅ Test Case 3: Test 3<BR>✅ Test Case 4: Test 4<BR><BR></span>|

<BR>

# If You NEED More
