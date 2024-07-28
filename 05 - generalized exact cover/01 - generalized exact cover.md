# Generalized Exact Cover



<BR>

| Playground Term | Equivalent Terms |
|:---|:---------------|
| requirements| constraints, columns, primary constraints, primary columns |
| actions | options, rows |

<BR>
This is the first time I’ve used the terms “primary constraint” and “primary column”, and there is a good reason for that. _Generalized Exact Cover_ adds the concept of “secondary constraints”, often referred to as “secondary columns” when referenced in terms of a matrix. I want you to know these terms, but in this playground, I’m going to use the term “Optional Requirement”.

What is the difference between a requirement (primary constraint/column) and an optional requirement (secondary constraint/column)? A requirement must be satisfied exactly once by a proper solution. It may not be left uncovered and it may not be covered more than once. On the other hand, an optional requirement is just what it says. It is optional. It does not need to be covered, but if it is covered, it can only be covered once.

I’m going to add one last equivalent term to the table above: At Most One-Time Constraint. The requirement may be covered at most one time, restricting the options to being covered zero times or exactly one time.

There is a reason the term “optional requirement” works for me. There is only one difference between a requirement and an optional requirement. With an optional requirement, not being covered never causes failure. As Algorithm X is looking for solutions, having no ability to cover a remaining requirement causes a failure condition causing Algorithm X to backtrack. That is not the case with optional requirements. Algorithm X doesn’t care if these optional requirements get covered at all, but Algorithm X does care that these optional requirements never get covered more than once.

<BR>

| Playground Term | Equivalent Terms | Definition |
|:----|:----|:-----------------|
| requirements| constraints, columns, primary constraints, primary columns | __Must__ be satisfied exactly once. |
| optional requirements| secondary constraints, secondary columns, at most one-time constraints | __May__ be satisfied, but if so, one time only. |
| actions | options, rows | The steps that can be taken to find a solution. |
