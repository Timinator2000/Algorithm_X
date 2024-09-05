# This Road is a Dead End


```
    def _process_row_selection(self, row):
        _, height, row, col = row
        self.grid[(row, col)].height = height

        if not all(city_view.is_valid() for city_view in self.grid[(row, col)].city_views):
            self.solution_is_valid = False


    def _process_row_deselection(self, row):
        _, _, row, col = row
        self.grid[(row, col)].height = 0
```


Here is diagram 1:

<BR><BR>
![High Rise Buildings Example](HighRise1.png)
<BR>

Here is diagram 2:

<BR><BR>
![City View Example](HighRise2.png)
<BR>

Here is diagram 3:

<BR><BR>
![Multiple City Views](HighRise3.png)
<BR>
