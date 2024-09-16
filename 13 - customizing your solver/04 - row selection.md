# Customizing Row Selection

By default, rows of the matrix are sorted simply by the order in which they are encountered. When a column is selected, Algorithm X navigates down the column and builds a list of all rows that cover that column. These rows are tried, one-by-one, in the order Algorithm X found them.

Customizing the order in which Algorithm X tries rows is a bit more interesting than the columns, since MRV already provides a fairly powerful strategy for column selection.  With no strategy override, row order is based on the algorithm you used to build your actions dictionary. In the `AlgorithmXSolver` code, you can see the default is to return `0` for all nodes, providing no guidance at all to Algorithm X.

```python
    # In some cases it may be beneficial to have Algorithm X try certain paths through the matrix.
    # This can be the case when there is reason to believe certain actions have a better chance than
    # other actions at producing complete paths through the matrix. The method included here does
    # nothing, but can be overridden in the case a subclass wishes to influence the order in which
    # Algorithm X tries rows (actions) that cover some particular column.
    def _action_sort_criteria(self, node):
        return 0
```

To demonstrate an override situation, let’s again look at Sudoku where every action probably took the following form:

```python
action = ('place value', row, col, val)
```

The `node`s passed into `self._action_sort_criteria(self, node)` are nodes from the matrix. To get access to the row title, it is necessary to first follow the pointer to the row header. The following override will make sure integers for a Sudoku cell are always tried in ascending order:

```python
    def _action_sort_criteria(self, node):
        _, _, _, val = node.row_header.title
        return val
```

The following override will make sure integers for a Sudoku cell are always tried in descending order:

```python
    def _action_sort_criteria(self, node):
        _, _, _, val = node.row_header.title
        return -val
```

The following override will make sure integers are again tried in descending order, but this time all even numbers are chosen before odd numbers:

```python
    def _action_sort_criteria(self, node):
        _, _, _, val = node.row_header.title
        return (val % 2, -val)
```

With these new tools in place, let's take a look at the [Assorted Rectangular Pieces Puzzle](https://www.codewars.com/kata/5a8f42da5084d7dca2000255) found on [CodeWars](https://www.codewars.com).
