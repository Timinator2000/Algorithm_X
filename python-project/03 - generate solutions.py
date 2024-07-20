# TECH.IO allows me to use this import statement to make my examples concise and easy
# to study. It is highly likely you will need to copy all of the AlgorithmXSolver
# code into your coding environment.

from AlgorithmX import AlgorithmXSolver

class MrsKnuthPartISolver(AlgorithmXSolver):

    def __init__(self):
        requirements = [('requirement 1', ), ('requirement 2', )]
        actions = {
            ('Cover Req 1', ):[('requirement 1', )],
            ('Cover Req 2', ):[('requirement 2', )]
        }

        super().__init__(requirements, actions)


def main_program:

    solver = MrsKnuthPartISolver()
          
    for solution in solver.solve():
        for action in solution:
            print(action)
