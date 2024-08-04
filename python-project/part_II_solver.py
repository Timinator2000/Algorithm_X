# TECH.IO allows me to use this import statement to make my examples concise and easy
# to study. Unless your coding environment will let you create an AlgorithmX package,
# you will need to copy all of the AlgorithmXSolver code into your code.

from AlgorithmX import AlgorithmXSolver

class MrsKnuthPartIISolver(AlgorithmXSolver):

    LOUD_INSTRUMENTS = ['Trumpet', 'Trombone', 'Drums']

    def __init__(self, teacher_availability, students):
        
        requirements = [('student scheduled', 'Drew'),
                        ('student scheduled', 'Ella'),
                        ('student scheduled', 'Lola')]

        optional_requirements = [('slot filled', 'F', 8),
                                 ('slot filled', 'F', 9),
                                 ('slot filled', 'F', 10),
                                 ('slot filled', 'F', 11),
                                 ('slot filled', 'F', 1),
                                 ('instrument on day', 'F', 'Trombone'),
                                 ('instrument on day', 'F', 'Drums'),
                                 ('instrument on day', 'F', 'Flute'),
                                 (('Ella', 'F', 10), ('Drew', 'F', 11)),
                                 (('loud instrument', 'F', 8), ('loud instrument', 'F', 9)),
                                 (('loud instrument', 'F', 9), ('loud instrument', 'F', 10)),
                                 (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        actions = dict()

        action = ('place student', 'Drew', 'Trombone', 'F', 10)
        actions[action] = [('student scheduled', 'Drew'),
                           ('slot filled', 'F', 10),
                           ('instrument on day', 'F', 'Trombone'),
                           (('loud instrument', 'F', 9), ('loud instrument', 'F', 10)),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        action = ('place student', 'Drew', 'Trombone', 'F', 11)
        actions[action] = [('student scheduled', 'Drew'),
                           ('slot filled', 'F', 11),
                           ('instrument on day', 'F', 'Trombone'),
                           (('Ella', 'F', 10), ('Drew', 'F', 11)),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        action = ('place student', 'Drew', 'Trombone', 'F', 1)
        actions[action] = [('student scheduled', 'Drew'),
                           ('slot filled', 'F', 1),
                           ('instrument on day', 'F', 'Trombone')]

        action = ('place student', 'Ella', 'Flute', 'F', 10)
        actions[action] = [('student scheduled', 'Ella'),
                           ('slot filled', 'F', 10),
                           ('instrument on day', 'F', 'Flute'),
                           (('Ella', 'F', 10), ('Drew', 'F', 11))]

        action = ('place student', 'Ella', 'Flute', 'F', 1)
        actions[action] = [('student scheduled', 'Ella'),
                           ('slot filled', 'F', 1),
                           ('instrument on day', 'F', 'Flute')]

        action = ('place student', 'Lola', 'Drums', 'F', 11)
        actions[action] = [('student scheduled', 'Lola'),
                           ('slot filled', 'F', 11),
                           ('instrument on day', 'F', 'Drums'),
                           (('loud instrument', 'F', 10), ('loud instrument', 'F', 11))]

        action = ('place student', 'Lola', 'Drums', 'F', 1)
        actions[action] = [('student scheduled', 'Lola'),
                           ('slot filled', 'F', 1),
                           ('instrument on day', 'F', 'Drums')]

        


        

        actions[action] = [('student scheduled', 'Ayla'),
                            ('slot filled', 'Th', 2),
                            ('instrument on day', 'Th', 'Trumpet')]
        
        action = ('place student', 'Bob', 'Drums', 'Th', 2)
        
        actions[action] = [('student scheduled', 'Bob'),
                            ('slot filled', 'Th', 2),
                            ('instrument on day', 'Th', 'Drums')]

        action = ('place student', 'Bob', 'Drums', 'Th', 3)
        
        actions[action] = [('student scheduled', 'Bob'),
                            ('slot filled', 'Th', 3),
                            ('instrument on day', 'Th', 'Drums')]

        action = ('place student', 'Alex', 'Tuba', 'Th', 2)
        
        actions[action] = [('student scheduled', 'Alex'),
                            ('slot filled', 'Th', 2),
                            ('instrument on day', 'Th', 'Tuba')]

        action = ('place student', 'Alex', 'Tuba', 'Th', 4)
        
        actions[action] = [('student scheduled', 'Alex'),
                            ('slot filled', 'Th', 4),
                            ('instrument on day', 'Th', 'Tuba')]
        
        super().__init__(requirements, actions, optional_requirements)


def main_program():

    teacher_availability = None
    students = None

    solver = MrsKnuthPartIISolver(teacher_availability, students)
          
    for solution in solver.solve():
        for _, name, instrument, day, hour in solution:
            print(f'Add {name}/{instrument} to Mrs. Knuth\'s schedule on {day} at {hour}.')
