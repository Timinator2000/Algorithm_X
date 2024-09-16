# Customizing Column Selection

In Step 2 of Algorithm X, a column is chosen from all remaining yet-to-be-covered columns. As is often the case with backtracking, `AlgorithmXSolver`’s default is to choose the column covered by the fewest number of rows. The technique is often referred to as Minimum Remaining Value (MRV). Two situations could prompt you to override this default.

1. You may want to specify how ties are broken when multiple columns are covered by the same number of rows.

1. You may want to specify some non-MRV-based criteria.


To customize the sort criteria, you must override `AlgorithmXSolver`’s `self. _requirement_sort_criteria(self, node)`. Algorithm X loops through the column headers to determine which column to choose next. Because the `node` passed into the method is a column header, it is easy to accesss:

1. `node.size` - the number of rows that cover this column

1. `node.title` - the requirement tuple

In the `AlgorithmXSolver` code below, you can see the default is to return `node.size`.

```
    # In some cases it may be beneficial to have Algorithm X try covering certain requirements
    # before others as it looks for paths through the matrix. The default is to sort the requirements
    # by how many actions cover each requirement, but in some case there might be several 
    # requirements covered by the same number of actions. By overriding this method, the
    # Algorithm X Solver can be directed to break ties a certain way or consider some other way
    # of prioritizing the requirements.
    def _requirement_sort_criteria(self, node):
        return node.size
```

Often, MRV is a very good choice for column selection, so you may find it rare that you consider overriding how columns are sorted. In the next section, I will look at the rows of the matrix.
