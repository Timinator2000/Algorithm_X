# All or None

The [Merriam-Webster Dictionary](https://www.merriam-webster.com/) defines [mutually exclusive](https://www.merriam-webster.com/dictionary/mutually%20exclusive) as:

> : being related such that each excludes or precludes the other
>> _mutually exclusive_ events

Assume I have an exact cover problem and the possible actions are `(A, B, C, D)`. Also assume the solution will consist of two actions, but we know `A` and `C` are mutually exclusive. It's pretty easy to see the possible solutions are `(A, B)`, `(A, D)`, `(B, C)`, `(B, D)` or `(C, D)`. It is not possible for `(A, C)` to be a proper solution since `A` and `C` are mutually exclusive and cannot both be part of the same solution. How can we include this knowledge in the model we build to feed Algorithm X?

# Optional Requirements to the Rescue
