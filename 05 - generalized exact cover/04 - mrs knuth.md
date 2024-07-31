# Puzzle Overview - Mrs. Knuth is Back!

How about the good news first? Most of the input and all of the output has not changed for Mrs. Knuth – Part II. Let’s see what changes she has requested…

_Mrs. Knuth's schedule needs to be more flexible than she first thought. She isn't able to always teach the same number of hours on her teaching days. She also doesn't always have enough students to completely fill her `teacherAvailability`. You'll need to adjust your algorithm to handle her `teacherAvailability` possibly containing different numbers of hours for each day she teaches and you'll need to be able to handle hours in her `teacherAvailability` for which there ends up being no student scheduled._

Mrs. Knuth might have more hours of availability than students. In Part I, it was __required__ that each slot in Mrs. Knuth’s availability get filled. It appears now that some slots might not get filled. Of course, she cannot teach two students at the same time, so if a slot is filled, it can only be filled with one student. Hmmm….sounds like an optional requirement.

_You might be impressed with Mrs. Knuth's newfound flexibility, but don't get too relaxed. She still requires that no instrument be taught more than one hour on any one day._

It is important to note that Mrs. Knuth might not teach the same number of hours on each day and becuase of that, it is not guaranteed that she will teach all the same instruments on each day. Still, we must make sure she does not teach a single instrument more than one time per day, but it is also possible certain instruments will not be taught on certain days.

_On top of that, she has struggled with `loudInstrument`s, specifically the __Trumpet__, the __Drums__ and the __Trombone__. In the interest of her long-term hearing, she has asked that you make sure no two `loudInstrument`s are ever scheduled back-to-back. (A lesson at 11am and a lesson at 1pm are not considered back-to-back since there is an hour lunch break between the two.)_

No two loud instruments are ever to be scheduled back-to-back, meaning, if a trumpet is scheduled on Friday at 10, we must not schedule a trombone on Friday at 11. Definitely sounds like mutual exclusivity, doesn’t it?

_For the most part, the kids in school are good kids, but some kids get a bit rowdy when they are with certain friends. To avoid disruptions to her schedule, Mrs. Knuth has given you a list of `troublesomePair`s. It's important the individuals in these pairs never be scheduled back-to-back. There must be at least an hour of time between the two individuals to ensure they don't get each other wound up and start causing trouble._

Here we see another classic example of mutual exclusivity. If Emma and Anna are a troublesome pair, we need to make sure they are not scheduled back-to-back.

_Despite Mrs. Knuth's wacky requests, all students must get a spot on her schedule._

Definitely seems like each student being schedule remains a requirement.

# Example Test Case

Let's take a look at the example test case:

```text
M Tu W Th F 8 9 10 11 1
3
Drew Trombone M Tu W Th F 10 11 1
Ella Flute M Tu W Th F 10 1
Lola Drums M Tu W Th F 11 1
1
Drew Ella
```

Mrs. Knuth is available on Fridays at 8, 9, 10, 11 and 1. Three students need to be scheduled. Drew (trombone) is available on Friday at 10, 11 and 1, Ella (flute) is available on Friday at 10 and 1, and Lola (drums) is available on Friday at 11 and 1. We know all students __must__ be scheduled, so these are standard, must-be-covered-exactly-one-time requirements.

```
Requirements:
    ('student scheduled', 'Drew')
    ('student scheduled', 'Ella')
    ('student scheduled', 'Lola’)
```

What about filling the teacher availability slots? We already know some slots might remain empty and we know that is definitely the case here since there are 3 students and 5 teacher slots. Even though slots don’t need to be filled, any slot that is filled can only be filled once. This perfectly fits the definition of an optional requirement.

```
Optional Requirements:
    ('slot filled', 'Fr', 8)
    ('slot filled', 'Fr', 9)
    ('slot filled', 'Fr', 10)
    ('slot filled', 'Fr', 11)
    ('slot filled', 'Fr', 1)
```

You may have noticed that none of the students are available on Friday before 10, so you could reduce the problem space and eliminate the top two optional requirements. However, I don’t recommend doing that currently. I’ll talk about problem space reduction later in the playground. For now, stick to the process as there is a more-than-reasonable chance that later test cases will be more complex and might not be conducive to the same reductions.

Let’s think ahead a bit about the 'instrument on day' requirements. In this simple example, there are three instruments and there is only one day, but we know from the problem statement that Mrs. Knuth might not teach the same number of hours on every day. During any one day of teaching, an instrument might not be taught or it might be taught one time. It cannot be taught more than one time on the same day. We will add these requirements to our list of optional requirements.

```
Optional Requirements:
    ('slot filled', 'Fr', 8)
    ('slot filled', 'Fr', 9)
    ('slot filled', 'Fr', 10)
    ('slot filled', 'Fr', 11)
    ('slot filled', 'Fr', 1)
    ('instrument on day', 'Fr', 'Trombone')
    ('instrument on day', 'Fr', 'Drums')
    ('instrument on day', 'Fr', 'Flute')
```

What about Drew and Ella being a troublesome pair? We need to look at the availability of Drew and and the availability of Ella and identify where we could have a situation we need to avoid.  

