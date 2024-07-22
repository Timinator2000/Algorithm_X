# Print Your Requirements & Actions

The first troubleshooting step you will want to take is simply printing the requirements, the actions and the requirements satisfied by each action. Hopefully, this can be done on a reasonably small test case. If the test case is big and there are a lot of requirements and actions, sifting through the printed data can be daunting.

If you decide to print the requirements and actions, I suggest doing so right before you invoke the inherited AlgorithmXSolver constructor.

``` python
        for r in requirements:
            print(r)

        for a in actions:
            print(a)
            for r in actions[a]:
                print('   ', r)
        
        super().__init__(requirements, actions)
```

# Study Your Errors

It is critical the tuples you use for requirements and actions always line up with each other so you don’t get `KeyError`s when AlgorithmXSolver is setting up the DLX matrix. For instance, ('slot filled', 'Th', 4) is __not__ the same as ('slot filled', 'Thurs', 4). I’m sure that seems obvious, but when you get a `KeyError`, look for places that you might have requirements specs that are supposed to be the same, but are slightly different.

``` python
Traceback (most recent call last):
  File "/project/target/part_I_generate_solutions_test.py", line 51, in <module>
    main_program()
  File "/project/target/part_I_generate_solutions.py", line 70, in main_program
    solver = MrsKnuthPartISolver(teacher_availability, students)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/project/target/part_I_generate_solutions.py", line 62, in __init__
    super().__init__(requirements, actions)
  File "/project/target/AlgorithmX.py", line 201, in __init__
    current_col_header   = self.R[requirement]
                           ~~~~~~^^^^^^^^^^^^^
KeyError: ('slot filled', 'Thurs', 4)
```

In this playground, you will want to ignore the `Traceback`. It probably won't make sense unless you are familiar with making code exercises on TECH.IO.

# No Solutions Found

Algorithm X not finding any solutions can be the most frustrating of all and it always comes down to some issue with your model. Assuming your problem is guaranteed to have a solution, the only reason Algorithm X will fail to find a solution is that something in your model is not sufficient. __Some requirement is not being covered by any possible combination of actions.__ Something is wrong in your mapping of satisfied requirements for each action.

Although this can be frustrating, you will get better and better at building models with practice. The flip side of this frustration is that after you become proficient at building models you will experience elation when you suprise yourself by solving an exact cover problem much faster than you ever expected!

# Practice Makes Perfect

Down below, I have duplicated full _hard coded_ solution to Mrs. Knuth Part I. Use this code to do the following:

1) Print out all the requirements, actions and the requirements satisfied by each action.

2) Make very minor changes in the requirements to create `KeyError`s.

3) Find a way to make a very minor change that doesn't result in any runtime issues, but Algorithm X fails to find a solution.

@[Try to create the three error situations above.]({"stubs": ["part_I_generate_solutions.py"], "command": "python3 part_I_generate_solutions_test_2.py"})

