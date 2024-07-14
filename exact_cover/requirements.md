# Capturing Requirements

My Algorithm X journey was heavily influenced by [Ali Assaf]( https://www.cs.mcgill.ca/~aassaf9/index.html)’s [Algorithm X in 30 Lines!]( https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html). Toward the bottom is a link to Assaf’s [Sudoku Solver]( https://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt). I found his technique for capturing requirements and actions very helpful in my debugging and I’m going to suggest you also use that format.

For each requirement, a human readable tuple of data clearly identifies the requirement. First, consider that each student must be put on Mrs. Knuth’s schedule. Since there are three students in our initial example, we start with the following 3 requirements:

```text
    (‘student scheduled’, 'Ayla')
    (‘student scheduled’, 'Bob')
    (‘student scheduled’, 'Alex')
```

If we take any one of those requirements, it is very easy to answer “yes” or “no” to the following question: Has this requirement been satisfied yet or not? Ayla has either been placed on the schedule or she has not. There is no in-between. This is a critical feature of requirements, they must be black or white. It must be obvious if the requirement has been satisfied or not.

Next, we’ll add requirements for Mrs. Knuth’s availability. She only teaches at 2, 3 and 4 on Thursday. Each one of those slots must be filled:

```text
    (‘slot filled’, ‘Th’, 2)
    (‘slot filled’, ‘Th’, 3)
    (‘slot filled’, ‘Th’, 4)
```

Two pieces of data uniquely identify each requirement: the day and the time of the slot. Because this initial test case is very minimal and Mrs. Knuth only teaches one day, we could omit the day from the requirement specification, but we would quickly run into problems as soon as Mrs. Knuth teaches on 2 or more days. 

Lastly, we need to add requirements to make sure each instrument is taught on each day. Again, we could omit these requirements for this simple example where Mrs. Knuth only teaches one day, but, just like before, we quickly run into problems as soon as Mrs. Knuth teaches more than one day per week.

Looking at the input, we see the instruments being taught are Trumpet, Drums and Tuba. Each of those instruments must show up on each day Mrs. Knuth teaches. Since she only teaches one day, we only need three more requirements:

```text
    (‘instrument on day’, ‘Th’, ‘Trumpet’)
    (‘instrument on day’, ‘Th’, ‘Drums’)
    (‘instrument on day’, ‘Th’, ‘Tuba’)
```

That’s all we need! A complete list of requirements for this first test case looks like this:

```text
    (‘student scheduled’, ‘Ayla’)
    (‘student scheduled’, ‘Bob’)
    (‘student scheduled’, ‘Alex’)
    (‘slot filled’, ‘Th’, 2)
    (‘slot filled’, ‘Th’, 3)
    (‘slot filled’, ‘Th’, 4)
    (‘instrument on day’, ‘Th’, ‘Trumpet’)
    (‘instrument on day’, ‘Th’, ‘Drums’)
    (‘instrument on day’, ‘Th’, ‘Tuba’)
```

Look through that list again and ask yourself this question: Does each requirement clearly identify something that must happen? Ayla must get scheduled. Bob must get scheduled. Alex must get scheduled. Thursday at 3 on Mrs. Knuth’s schedule must get filled. A Tuba lesson must be scheduled on Thursday. I think you get the idea.

Keep in mind, each of one of these requirements must be satisfied exactly one time by any proposed solution. This is where the term “exact” comes from in exact cover. All requirements must be covered exactly once by a proper solution. None can be left uncovered and none can be covered multiple times by overlapping actions.
