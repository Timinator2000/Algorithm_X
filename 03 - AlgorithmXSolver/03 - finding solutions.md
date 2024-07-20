# Finding Solutions

```python runnable
#  This solution uses Knuth's Algorithm X and his Dancing Links (DLX):
#  (DLX Based Algorithm X Solver Last Revised 06/02/2024)
// { autofold
#
#   https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
#
#  June 02, 2024 - history added to allow subclasses to make adaptations for multiplicity.
#                - giving this Solver similar functionality to Knuth's Algorithm M.
#

#  To study the implementation of Algorithm X, I originally used the following write-up
#  by Ali Assaf (ali.assaf.mail@gmail.com) titled "Algorithm X in 30 Lines!" 
#
#    https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html
#
#  Assaf's Algorithm X implementation is not DLX based, but it was extremely helpful in my
#  journey that resulted in the DLX based solver below.
#
#  For a detailed discussion of my non-DLX solver, see my solutions for:
#
#       Dominoes Solver          : https://www.codingame.com/training/hard/dominoes-solver
#       Sudoku Solver            : https://www.codingame.com/training/medium/sudoku-solver
#

#  To understand this DLX based solver will require what I consider mind-bending study
#  of Knuth's Dancing Links. I believe I was only able to become proficient with DLX
#  because I was able to study @RoboStac's solution to Constrained Latin Squares on
#  www.codingame.com.
#
#  https://www.codingame.com/training/medium/constrained-latin-squares
#
#
#  Ultimately, I have used @RoboStac's DLXCell class which represents a single cell in
#  Algorithm X's Matrix A and provides all the "dancing" functionality. In a much less
#  significant effort, I took @Robostac's Algorithm X logic and reworked it to fit the
#  Algorithm X logic laid out above by Assaf. In the end, I created what I believe to 
#  be an extremly reusable DLX based Algorithm X solver with significant options for
#  customization.
#
#  If you are interested in Algorithm X and Dancing Links, I invite you to copy this code
#  and try to solve all the puzzles on @5DN1L's Algorithm X list below. You should be able
#  to do every puzzle without making a single change to my DLX based AlgorithmXSolver class.
#  Simply create a subclass Solver and add the puzzle specific details...which many times is
#  a very challenging task itself!
#
#  @5DN1L's Puzles Solvable with Algorithm X:
#
#  https://www.codingame.com/forum/t/puzzles-solvable-by-algorithm-x-dancing-links/196871
#
// }

# @RoboStac's DLX Cell Class Definition
// { autofold

# DLXCell is one cell in Matrix A. This implementation was mostly copied 
# from @RoboStac's solution to Constrained Latin Squares on Codingame.com.
#
# https://www.codingame.com/training/medium/constrained-latin-squares
#
class DLXCell:
    def __init__(self, title=None):
        self.prev_x = self
        self.next_x = self
        self.prev_y = self
        self.next_y = self

        self.col_header = None
        self.row_header = None

        # Only used for column and row headers.
        self.title = title

        # Size quickly identifies how many rows are in any particular column.
        self.size = 0

    def remove_x(self):
        self.prev_x.next_x = self.next_x
        self.next_x.prev_x = self.prev_x

    def remove_y(self):
        self.prev_y.next_y = self.next_y
        self.next_y.prev_y = self.prev_y

    def restore_x(self):
        self.prev_x.next_x = self
        self.next_x.prev_x = self

    def restore_y(self):
        self.prev_y.next_y = self
        self.next_y.prev_y = self

    def attach_horiz(self, other):
        n = self.prev_x
        other.prev_x = n
        n.next_x = other
        self.prev_x = other
        other.next_x = self

    def attach_vert(self, other):
        n = self.prev_y
        other.prev_y = n
        n.next_y = other
        self.prev_y = other
        other.next_y = self

    def remove_column(self):
        self.remove_x()
        node = self.next_y
        while node != self:
            node.remove_row()
            node = node.next_y

    def restore_column(self):
        node = self.prev_y
        while node != self:
            node.restore_row()
            node = node.prev_y
        self.restore_x()

    def remove_row(self):
        node = self.next_x
        while node != self:
            node.col_header.size -= 1
            node.remove_y()
            node = node.next_x

    def restore_row(self):
        node = self.prev_x
        while node != self:
            node.col_header.size += 1
            node.restore_y()
            node = node.prev_x

    def select(self):
        node = self
        while 1:
            node.remove_y()
            node.col_header.remove_column()
            node = node.next_x
            if node == self:
                break

    def unselect(self):
        node = self.prev_x
        while node != self:
            node.col_header.restore_column()
            node.restore_y()
            node = node.prev_x
        node.col_header.restore_column()
        node.restore_y()
// }

# AlgorithmXSolver Class Definition
// { autofold

class AlgorithmXSolver():
    # R - a list of requirements.  The __init__() method converts R to a dictionary, but R must
    #     originally be passed in as a simple list of requirements. Each requirement is a tuple
    #     of values that uniquely identify that requirement from all other requirements.
    #
    # A - must be passed in as a dictionary - keys are actions, values are lists of covered requirements
    #
    # O - list of optional requirements.  They can be covered, but they never cause failure.
    #     Optional requirements are important because if they get covered, no other action can 
    #     also cover that same requirement. Also referred to as "at most one time contraints".
    #
    def __init__(self, R: list, A: dict, O: list = []):
        self.A  = A
        self.R  = R + O
        self.O  = O

        # The list of actions (rows) that produce the current path through Matrix A.
        self.solution = []
        
        # A history can be added to a subclass to allow Algorithm X to handle "multiplicity".
        # In the basic Solver, nothing is ever put into the history. A subclass can override
        # the _process_row_selection() method to add history in cases of multiplicity. 
        self.history = [set()]

        # For the basic Algorithm X Solver, all solutions are always valid.  However, a subclass
        # can add functionality to check solutions as they are being built to steer away from
        # invalid solutions.  The basic Algorithm X Solver never modifies this attribue in any way.
        self.solution_is_valid = True

        # Create a column in Matrix A for every requirement.
        self.matrix_a_root = DLXCell()
        self.matrix_a_root.size = 10000000
        self.matrix_a_root.title = 'root'
        
        self.col_headers = [DLXCell(requirement) for requirement in self.R]
        self.row_headers = {action:DLXCell(action) for action in self.A}

        self.R = {requirement:self.col_headers[i] for i, requirement in enumerate(self.R)}

        for i in range(len(self.col_headers)):
            self.matrix_a_root.attach_horiz(self.col_headers[i])

        # Create a row in Matrix A for every action.
        for action in self.A:
            current_row_header = self.row_headers[action]
            
            previous_cell = None
            for requirement in A[action]:
                next_cell = DLXCell()
                current_col_header   = self.R[requirement]
                next_cell.col_header = current_col_header
                next_cell.row_header = current_row_header
                current_col_header.attach_vert(next_cell)
                next_cell.col_header.size += 1
                
#                 THIS WOULD BE MORE APPROPRIATE, BUT I WOULD NEED TO FIX A FEW OTHER THINGS
#                 current_col_header.attach_horiz(next_cell)
                
                if previous_cell:
                    previous_cell.attach_horiz(next_cell)
                else:
                    previous_cell = next_cell


    def solve(self):
        
        # Algorithm X Step 1:
        #
        # Choose the column (requirement) with the best value for "sort criteria". For
        # the basic implementation of sort criteria, Algorithm X always chooses the column
        # covered by thew fewest number of actions. Optional requirements are not eligible 
        # for this step.
        best_column = self.matrix_a_root
        best_value  = 'root'
        
        node = self.matrix_a_root.next_x
        while node != self.matrix_a_root:
            
            # Optional requirements (at most one time constraints) are never chosen as best.
            if node.title not in self.O:
                
                # Get the sort criteria for this requirement (column).
                value = self._requirement_sort_criteria(node)
                if best_column == self.matrix_a_root or value < best_value:
                    best_column = node
                    best_value  = value
            node = node.next_x
            
        if best_column == self.matrix_a_root:
            self._process_solution()
            yield self.solution
        else:

            # Build a list of all actions (rows) that cover the chosen requirement (column).
            actions = []
            node = best_column.next_y
            while node != best_column:
                actions.append(node)
                node = node.next_y

            # The next step is to loop through all possible actions. To prepare for this,
            # a new level of history is created. The history for this new level starts out
            # as a complete copy of the most recent history.
            self.history.append(self.history[-1].copy())    
                
            # Loop through the possible actions sorted by the given sort criteria. A basic
            # Algorithm X implementation does not provide sort criteria. Actions are tried
            # in the order they happen to occur in Matrix A.
            for node in sorted(actions, key=lambda a:self._action_sort_criteria(a)):
                self.select(node=node)
                if self.solution_is_valid:
                    for s in self.solve():
                        yield s
                self.deselect(node=node)

            self.history.pop()

    # Algorithm X Step 4 - Details:
    #
    # The select method updates Matrix A when a row is selected as part of a solution path.
    # Other rows that satisfy overlapping requirements need to be deleted and in the end,
    # all columns satisfied by the selected row get removed from Matrix A.
    def select(self, node=None, title=None):

        if node:
            node.select()
            self.solution.append(node.row_header.title)
            self._process_row_selection(node.row_header.title)

        # This is currently never used. I have some thoughts about what might be possible
        # if a row could be selected by title as compared to being selected by none.
        if title:
            pass


    # Algorithm X Step 4 - Clean Up:
    #
    # The select() method selects a row as part of the solution being explored.  Eventually that
    # exploration ends and it is time to move on to the next row (action).  Before moving on,
    # Matrix A and the partial solution need to be restored to its prior state.
    def deselect(self, node=None, title=None):

        if node:
            node.unselect()
            self.solution.pop()
            self._process_row_deselection(node.row_header.title)

        # This is currently never used. I have some thoughts about what might be possible
        # if a row could be selected by title as compared to being selected by none.
        if title:
            pass
        
        
    #  In some cases it may be beneficial to have Algorithm X try certain paths through Matrix A.
    #  This can be the case when there is reason to believe certain actions have a better chance than
    #  other actions at producing complete paths through Matrix A.  The method included here does
    #  nothing, but can be overridden in the case a subclass wishes to influence the order in which
    #  Algorithm X tries rows (actions) that cover some particular column.
    def _action_sort_criteria(self, node):
        return 0
    

    #  In some cases it may be beneficial to have Algorithm X try covering certain requirements
    #  before others as it looks for paths through Matrix A.  The default is to sort the requirements
    #  by how many actions cover each requirement, but in some case there might be several 
    #  requirements covered by the same number of actions.  By overriding this method, the
    #  Algorithm X Solver can be directed to break ties a certain way or consider some other way
    #  of prioritizing the requirements.
    def _requirement_sort_criteria(self, node):
        return node.size
    
    
// }
    #  The following method can be overridden by a subclass to add logic to perform more detailed solution
    #  checking if invalid paths are possible through Matrix A.  Some problems have requirements that
    #  cannot be captured in the basic requirements list passed into the __init__() method.  For instance,
    #  a solution might only be valid if it fits certain parameters that can only be checked at intermediate
    #  steps.  In a case like that, this method can be overridden to add the functionality necessary to 
    #  check the solution.
    #
    #  If the subclass logic results in an invalid solution, the 'solution_is_valid' attribute should be set
    #  to False instructing the Algorithm X to stop progressing down this path in Matrix A.
    def _process_row_selection(self, row):
        pass


    #  This method can be overridden by a subclass to add logic to perform more detailed solution
    #  checking if invalid paths are possible through Matrix A.  This method goes hand-in-hand with the
    #  _process_row_selection() method above.
    #
    #  If the subclass logic results in an invalid solution, the 'solution_is_valid' attribute should be
    #  set to False instructing Algorithm X to stop progressing down this path in Matrix A.  When the
    #  Algorithm X backtracking comes back to deselect this row, the 'solution_is_valid' attribute must 
    #  be reset to True. That should be done here.
    def _process_row_deselection(self, row):
        pass


    #  This method can be overridden to instruct Algorithm X to do something every time a solution is found.
    #  For example, this method could be updated to simply count the number of solutions. It's also possible 
    #  that not all full paths through Matrix A are truly valid, but maybe that cannot be determined until 
    #  the very end. In that case, logic could be added here to perform some checking on a solution Algorithm X 
    #  considers valid, but ultimate validity requires the solution passing some last bit of logic.
    def _process_solution(self):
        pass


#------------------------------------------------------------------------------------------------------
#
# Everything above this point could easily be put into a package and reused on any exact cover problem.
#
# Below here is the only code specific to the { some puzzle name } puzzle.
#
#------------------------------------------------------------------------------------------------------



class MrsKnuthPartISolver(AlgorithmXSolver):

  def __init__(self, teacher_availability, students):
    print("Let's Go!")

solver = MrsKnuthPartISolver(None, None)

for solution in solver.solve():
  pass

print('Finished!')
```
