# Solving Mrs. Knuth Part III

You already have everything you need to instruct Algorithm X to find scheduling options for Mrs. Knuth. The last thing to cover is the process of evaluating the options and determining which one is best. I’m going to leave all the score calculations to you, but I do want to show you how to make your AlgorithmXSolver subclass handle some of the details for you.

Your code will need to evaluate a bunch of scheduling options and score each option. In order to keep track of the current best score and the current best option, let’s create a couple of new attributes in your subclass constructor.

```
class MrsKnuthPartIIISolver(AlgorithmXSolver):

    def __init__(self, teacher_availability, students, troublesome_pairs):
        
        self.best_solution = []         # a copy of the best solution found so far
        self.best_score = 0             # the full score of the best solution found so far

        requirements = []
        optional_requirements = []
        actions = dict()

        # Code to set up the rows and columns for Algorithm X goes here.

        super().__init__(requirements, actions, optional_requirements)

    def _process_solution(self):
        # need to override this AlgorithmXSolver method
```

What is that second method definition? Each time Algorithm X finds a potential solution, the method `_process_solution(self)` is called before the `yield` statement sends that solution to the code looping through solutions. (You will have to look through the AlgorithmXSolver code if you want to see where solutions are generated.) If you would like to use this built in functionality, you simply override this method and add your specific scoring logic. Your code should look something like this:


```
    def _process_solution(self):
        if self.handle_multiplicity:

            score = 0

            # Your code to score the current solution goes here. The actions that make up the
            # current solution are stored by your solver subclass in the attribute self.solution.
            # You can loop through this list of actions, just like we have already done in
            # Mrs. Knuth - Parts I and II.

            # If the current score is better than the best score, update the best score
            # and save a copy of the solution as the new best_solution.

            if score > self.best_score:
                self.best_score = score
                self.best_solution = self.solution.copy()
```

Hopefully, that is enough to get you going in the right direction. There is still plenty of work to be done on your scoring algorithm, generating a visual of the best schedule and printing the scoring intermediate steps. You've got this!
