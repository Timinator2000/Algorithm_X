# Generating Solutions for Mrs. Knuth - Part III

Before running Algorithm X, let’s reason our way through the problem statement one more time and determine what we expect to see.

```
M 8 Tu 8 W 8 Th 8 F 8 9 10 11 1
3
Drew Trombone 1 M Tu W Th F 10 11
Ella Flute 2 M 8 Tu 8 W Th F 11
Lola Drums 1 M Tu W Th F 11 1
1
Drew Ella
```

Because Drew and Ella are a troublesome pair and Drew’s only availability is on Friday, there is no way to schedule Ella on Friday. That leaves only Monday at 8 and Tuesday at 8 for Ella. Drew and Lola both play loud instruments, so they cannot be back-to-back. This eliminates the possibility of scheduling Lola on Friday at 11 since Drew’s only remaining availability would be Friday at 10. Lola will have to be scheduled Friday at 1. Finally, Drew could be scheduled on Friday at 10 or 11.

In the following code block, I have hard-coded the setup for the example test case. At this point, the schedule options are not scored. I am simply printing all the options returned by Algorithm X. There should be two possible solutions from which we will need to determine the schedule with the best score. Both solutions will have Ella on Monday at 8 and Tuesday at 8, while Lola will be Friday at 1. The only difference between the two options will be Drew’s location, either Friday at 10 or Friday at 11.

Make sure you scroll to the bottom and click on “run” as there is a quiz afterward.

@[Count the solutions to Mrs. Knuth - Part III Example Problem]({"stubs": ["part_II_solver.py"], "command": "python3 part_II_solver_test.py"})

?[How many solutions did Algorithm X find?]
- [ ] None - I was too lazy to click “run”.
- [ ] 2 – Exactly what I expected!
- [x] 4 – Is Algorithm X broken?
- [  ] 37 – Ella just stopped by and bumped her request to 5 lessons per week.

Did you get the result you expected? Either way, don’t worry. In the next section, we’ll discuss how to teach Algorithm X to do better.
