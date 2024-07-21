# Create a Solver Instance

So far, all we have is a MrsKnuthPartISolver class. We need to create an instance of that class. You’ll need to get the input data and organize that data so that you can pass it to the constructor.

```python
# Coding the following input is left to you. 
# teacher_availability = 
# students =

solver = MrsKnuthPartISolver(teacher_availability, students)
```

# Ask Solver to Find Solutions

So The last thing we need to do is ask our solver to give us the solutions. Some exact cover problems have multiple solutions and AlgorithmXSolver will always search for __all__ the solutions. Each solution found is returned one-by-one via a generator and each solution is a list of actions that make up that solution. Even if your problem is guaranteed to have a single solution, you should use the following format to get all solutions form your solver.

```python
for solution in solver.solver():
    for action in solution:
        # use the action to build your solution
```

I prefer to "unpack" the action tuple so that I have easy access to the information I need. For Mrs. Knuth Part I, each action is a tuple with 5 pieces of data - a title (that I don't really need right now), name, instrument, day and hour.

```python
schedule = some data structure to manage the answer to the puzzle

for solution in solver.solver():
    for _, name, instrument, day, hour in solution:
        # add name/instrument on day/hour to schedule

print(schedule)    # Don't forget how particular Mrs. Knuth is about her schedule formatting.
```

# Putting it All Together

Let's put this all together now. 

@[Use Algorithm X to find a schedule for Mrs. Knuth Part I]({"stubs": ["part_I_generate_solutions.py"], "command": "python3 part_I_generate_solutions_test.py"})



# Try a Snippet

```python runnable

from AlgorithmXSolver import AlgorithmXSolver

class MrsKnuthPartISolver(AlgorithmXSolver):

  def __init__(self, teacher_availability, students):
    print("Let's Go!")

solver = MrsKnuthPartISolver(None, None)

for solution in solver.solve():
  pass

print('Finished!')
```


