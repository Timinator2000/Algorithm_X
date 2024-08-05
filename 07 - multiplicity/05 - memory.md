# Making Algorithm X Smarter About Duplicates




# How Important is This?

What if Ella wanted 3 lesons? What if each of the students wanted 2 lessons? The more multplicity in the problem, the more crazy things can get. In Mrs. Knuth - Part III, all valid solutions need to be found and scored to determine the best schedule for Mrs. Knuth. The following table shows you how many distinct solutions need to be scored for each test case and how many solutions are generate by Algorithm X if multiplicity is _not_ properly handled. I have only included the test cases where multiplicity creates a problem.

<BR>

| Test Case | Distinct Solutions     | Solutions Found if Multiplicity Not Handled     |
|:--|:----:|:------------------------------------------------------------------:|
| 1 - 2 Lessons Per Week for Ella|2|4|
| 2 - 3 Lessons Per Week for Ella|2|12|
| 3 - 4 Lessons Per Week for Ella|2|48|
| 4 - Mornings are Better|8|192|
| 10 - Meh|66|792|
| 11 - Almost Perfect Schedule|863|3,452|
| 12 - Emma, We Need to Chat|413|9,912|
| 13 - 4-Day Weekends!|3,425|41,100|
| 14 - 3-Day Weekends!|2,755|88,160|
| 15 - Let's Rethink This Ivy|2,601|124,848|
| 16 - 5 Days of Drums…Ugh|1,546|148,416|
| 17 - Monday at 8am…Really?|1,862|178,752|
| 18 - So Many Options|12,561|200,976|
| 19 - Here Comes the Weekend|2,517|241,632|
| 20 - Hump Day!|8,297|265,504|
