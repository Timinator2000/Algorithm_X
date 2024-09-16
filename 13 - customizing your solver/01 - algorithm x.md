# Algorithm X

In order to have a conversation about customizing Algorithm X, it is necessary to first understand how Algorithm X works. You are welcome to study a detailed discussion in [Knuth’s The Art of Computer Programming] or a well-done summary on [Wikipedia]( https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X), but I do not see benefit in me trying to repeat that material here.

In the next graphic, I have copied the algorithm provided on Wikipedia. I strongly recommend you work your way through the step-by-step Algorithm X example provided on Wikipedia to gain an understanding of how Algorithm X processes the rows and columns to find solutions. 

<BR><BR>
![Algorithm X](AlgorithmX.png)
<BR>

# The Solver

As I have mentioned a few times already, I took Ali Assaf's Algorithm X code and wrapped it inside an `AlgorithmXSolver` class. In the next code block is the `solve()` method with all comments removed to make the visual concise. 

```python
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

            else:

                # Optional requirements stop the search for the best column.
                node = self.matrix_a_root
            
        if best_column == self.matrix_a_root:
            self._process_solution()
            if self.solution_is_valid:
                self.solution_count += 1
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
            # in the order they happen to occur in the matrix.
            for node in sorted(actions, key=lambda a:self._action_sort_criteria(a)):
                self.select(node=node)
                if self.solution_is_valid:
                    for s in self.solve():
                        yield s
                self.deselect(node=node)

                # All backtracking results in going back to a solution that is valid.
                self.solution_is_valid = True

            self.history.pop()
```


