# Capturing Requirements

My Algorithm X journey was heavily influenced by [Ali Assaf]( https://www.cs.mcgill.ca/~aassaf9/index.html)’s [Algorithm X in 30 Lines!]( https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html). Toward the bottom is a link to Assaf’s [Sudoku Solver]( https://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt). I found his technique for capturing requirements and actions very helpful in my debugging and I’m going to suggest you also use that format.

For each requirement, a human readable tuple of data clearly identifies the requirement. First, consider that each student must be put on Mrs. Knuth’s schedule. Since there are three students in our initial example, we start with the following 3 requirements:

```text
    ('student scheduled', 'Ayla')
    ('student scheduled', 'Bob')
    ('student scheduled', 'Alex')
```

If we take any one of those requirements, it is very easy to answer “yes” or “no” to the following question: Has this requirement been satisfied yet or not? Ayla has either been placed on the schedule or she has not. There is no in-between. This is a critical feature of requirements, they must be black or white. It must be obvious if the requirement has been satisfied or not.

Next, we’ll add requirements for Mrs. Knuth’s availability. She only teaches at 2, 3 and 4 on Thursday. Each one of those slots must be filled:

```text
    ('slot filled', 'Th', 2)
    ('slot filled', 'Th', 3)
    ('slot filled', 'Th', 4)
```

Two pieces of data uniquely identify each requirement: the day and the time of the slot. Because this initial test case is very minimal and Mrs. Knuth only teaches one day, we could omit the day from the requirement specification, but we would quickly run into problems as soon as Mrs. Knuth teaches on 2 or more days. 

Lastly, we need to add requirements to make sure each instrument is taught on each day. Again, we could omit these requirements for this simple example where Mrs. Knuth only teaches one day, but, just like before, we quickly run into problems as soon as Mrs. Knuth teaches more than one day per week.

Looking at the input, we see the instruments being taught are Trumpet, Drums and Tuba. Each of those instruments must show up on each day Mrs. Knuth teaches. Since she only teaches one day, we only need three more requirements:

```text
    ('instrument on day', 'Th', 'Trumpet')
    ('instrument on day', 'Th', 'Drums')
    ('instrument on day', 'Th', 'Tuba')
```

That’s all we need! A complete list of requirements for this first test case looks like this:

```text
    ('student scheduled', 'Ayla')
    ('student scheduled', 'Bob')
    ('student scheduled', 'Alex')
    ('slot filled', 'Th', 2)
    ('slot filled', 'Th', 3)
    ('slot filled', 'Th', 4)
    ('instrument on day', 'Th', 'Trumpet')
    ('instrument on day', 'Th', 'Drums')
    ('instrument on day', 'Th', 'Tuba')
```

Look through that list again and ask yourself this question: Does each requirement clearly identify something that must happen? Ayla must get scheduled. Bob must get scheduled. Alex must get scheduled. Thursday at 3 on Mrs. Knuth’s schedule must get filled. A Tuba lesson must be scheduled on Thursday. I think you get the idea.

Keep in mind, each of one of these requirements must be satisfied exactly one time by any proposed solution. This is where the term “exact” comes from in exact cover. __All requirements must be covered exactly once by a proper solution. None can be left uncovered and none can be covered multiple times by overlapping actions.__

# Constraining the Realm of Possibility

I have chosen to use the word “requirement”, but you will often see the word “constraint” used with Algorithm X. Each word is powerful in its own way. I want to briefly demonstrate where the word “constraint” really helps us understand the big picture of Algorithm X.

Consider Mrs. Knuth’s desire to avoid teaching more than one lesson per day for any instrument. One approach is to build all possible schedules and then check each schedule to see if any day has a repeated instrument. Because Algorithm X is _less constrained_, it will generate many solutions that eventually get eliminated when the days are checked for duplicate instrument lessons.

How many solutions get eliminated? Because all test cases in Mrs. Knuth - Part I are guaranteed to have a unique solution, we know all possible solutions _except one_ will be eliminated. That doesn’t really make the point I want to make unless we look at how many solutions need to be checked.

Test Cases 1 and 2 only have Mrs. Knuth teaching on a single day, so there is no impact to those test cases. However, starting with Test Case 3, the unconstrained results grow rapidly. Remember, every one of these possible solutions needs to be checked to make sure no two instruments are taught on the same day.

* Test Case 3 - 96 possible solutions

* Test Case 4 - 1,818 possible solutions

* Test Case 5 - 11,414 possible solutions

* Test Case 6 - 130,235 possible solutions

* Test Case 7 – I stopped counting at 53,000,000 possible solutions

There is a point to this exercises. It is best to restrict Algorithm X as much as possible with constraints (requirements). You will not always be able to eliminate the need to further validate potential solutions after Algorithm X finds them, but, by maximizing the knowledge passed to Algorithm X, you will be rewarded with a significantly smaller set of possible solutions, and in many cases, you will be rewarded with the _only_ valid solution.

