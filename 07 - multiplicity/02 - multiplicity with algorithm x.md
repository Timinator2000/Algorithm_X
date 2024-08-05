# Requirements Need More Precision

Let's take another look at the example problem:

```
M 8 Tu 8 W 8 Th 8 F 8 9 10 11 1
3
Drew Trombone 1 M Tu W Th F 10 11
Ella Flute 2 M 8 Tu 8 W Th F 11
Lola Drums 1 M Tu W Th F 11 1
1
Drew Ella
```

Requirements must be binary in Algorithm X. They have either been covered or they have not been covered. It is important to make sure there is no middle ground, such as Emma is half-way scheduled because 1 of her 2 lessons has been scheduled and the other still needs to be scheduled.
As problems get more complex, it is often helpful to quickly identify the steps that need to be taken to solve a simply or “toy” version of the problem and the example test case works perfectly. What needs to happen to build a solution?

1 Drew’s one lesson must be scheduled.
1 Lola’s one lesson must be scheduled.
1 Emma’s first lesson must be scheduled.
1 Emma’s second lesson must be scheduled.

Hopefully you see that 4 requirements are now needed to make sure these 3 students are properly scheduled. More precisely, a requirement specification now needs more than just a name. It also needs to identify which lesson has been scheduled. Is it the student’s first lesson? Second lesson? Third lesson? Let’s add lesson number to each requirement specification.

```text
('student scheduled', 'Drew', 1)
('student scheduled', 'Lola', 1)
('student scheduled', 'Ella', 1)
('student scheduled', 'Ella', 2)
```

Now we have a much more complete set of requirements. 4 requirements must be covered, resulting in 4 lessons being scheduled, one for Drew, one for Lola and two for Ella.

# Actions Need More Precision

