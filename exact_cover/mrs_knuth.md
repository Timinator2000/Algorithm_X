# A Long-Lost Relative?

It is highly unlikely that Mrs. Knuth is any relation to Donald Knuth, but one never knows. Mrs. Knuth is the school band teacher, and she needs help scheduling her students for lessons during the summer. We haven’t even covered how Algorithm X works, but we are going to use it to help Mrs. Knuth with her scheduling problem and solve the first Mrs. Knuth puzzle:

[Algorithm X – Part I](www.codingame.com)

# Puzzle Overview

Of course, you’ll need to properly organize your input and format your output, but the algorithm for building the schedules is a perfect candidate for Algorithm X. For your convenience, I have copied the most important portion of the goal section here:

_Mrs. Knuth, the school band teacher, has asked you to write an algorithm to generate her weekly private lesson schedule for the summer. Her availability is different from week to week, but she will always teach between 1 and 5 days per week. On each day that she teaches, she will teach between 2 and 8 hours. Because she likes consistency, she will teach the same number of hours on each day she teaches, but the actual time slots during which she is available might be different from day to day._

_Mrs. Knuth is a creature of habit. Her workday starts at 8am every day and ends at 5pm with an hour break for lunch each day from noon to 1pm. Although she is at school 9 total hours every day, she might not be available to teach on some days, she might have partial teaching availability on other days or she might have a day where she teaches every free minute other than during lunch._

_Mrs. Knuth is also a bit odd when it comes to music. To keep her mind fresh, she refuses to teach more than a single hour per day for any particular instrument. If she teaches 3 hours in one day, those lessons must be for 3 different instruments. If she teaches 8 hours in one day, all 8 instruments that day must be different._

_Given Mrs. Knuth’s open availability and each student’s instrument and lesson availability, generate a schedule for Mrs. Knuth that allows her to work with each student one time per week and meets her quirky demands._
