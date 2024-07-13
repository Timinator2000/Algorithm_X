# Background

In August, 2022, I attempted to solve [Constrained Latin Squares]( https://www.codingame.com/training/medium/constrained-latin-squares), a recently published puzzle by [@darkhorse64]( https://www.codingame.com/profile/c9ebe76a83b33730956eda0534d6cad86053292) on [Codingame](www.codingame.com). I noticed [@5DN1L]( https://www.codingame.com/profile/bbb8f47ea4601179303c20acdbf5fb6c1904782) had, a week earlier, posted a link to [Puzzles solvable by Algorithm X / Dancing Links](https://www.codingame.com/forum/t/puzzles-solvable-by-algorithm-x-dancing-links/196871), a post where he had compiled a list of puzzles on [Codingame](www.codingame.com) he had solved with [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X). I love processes that are repeatable and the idea of using a single algorithm to solve a long list of medium/hard puzzles intrigued me.

For the next 18 months, I worked on [@5DN1L]( https://www.codingame.com/profile/bbb8f47ea4601179303c20acdbf5fb6c1904782)’s list, reaching out to him over and over again with questions and ideas. I saw tremendous opportunity for not only a reusable software architecture, but also a repeatable engineering process for solving [Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover) problems. Eventually, he suggested I build an [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) playground, and here we are!

I can’t thank [@5DN1L]( https://www.codingame.com/profile/bbb8f47ea4601179303c20acdbf5fb6c1904782) enough for all of his guidance, support, ideas, encouragement, questions, answers, poking, prodding, reviewing, etc. This playground is his creation every bit as much as it is mine. His influence has made a permanent mark on who I am and how I approach problems. I am forever grateful.

# What is Algorithm X?

[Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) is a promise. If you can build a proper model to a particular problem space, [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) promises to find all solutions to that problem space. Papers have been written and projects have been done to demonstrate “how” [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) works. That is not the goal here. Instead, the focus of this exercise is to build expertise in the realm of modeling. The goal is to build models that [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) easily digests and returns solutions. Only a cursory understanding of [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) is required, and the implementation details will barely be covered. Instead, you will be asked to build models of problems and you will have the opportunity to see how well you modeled each problem simply by seeing how easily [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) converted your models into solutions.

# What’s In It for You?

A quick Google search will surely bring you to countless implementations of [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X), usually solving a 9x9 Sudoku grid using the famous [Dancing Links (DLX)]( https://en.wikipedia.org/wiki/Dancing_Links) technique proposed by the brilliant [Donald Knuth]( https://www-cs-faculty.stanford.edu/~knuth/). This playground is NOT just another Sudoku demonstration. By the time you're finished working your way through this material, you should feel confident solving any [Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover) problem you run across, including…

[Algorithm X – Part I]( https://www.codingame.com) -  Mrs. Knuth Tutorial (+50 XP)
<BR>[Algorithm X – Part II]( https://www.codingame.com) -  Mrs. Knuth Tutorial (+50 XP)
<BR>[Algorithm X – Part III]( https://www.codingame.com) - Mrs. Knuth Tutorial (+50 XP)
<BR>[Equation Finder]( https://www.codingame.com) - Algorithm X – Part III Bonus Exercise (+50 XP)

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

# My Promise to You

I wholeheartedly believe that working through this playground and the accompanying puzzles will be a great experience on multiple levels. How can I say this? All these things happened for me as I studied [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) and applied it to as many puzzles as possible. I promise…

* You will become proficient with a powerful and repeatable problem solving technique known as [Algorithm X]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X).
* You will experience the compelling nature of reusable software architectures.
* You will find every puzzle listed above significantly easier than it would have been otherwise. I’m not saying they’ll all be easy, but they will indeed be easier.
* You will have a lot of fun.
* You will earn up to 1700 [Codingame](www.codingame.com) XP!
