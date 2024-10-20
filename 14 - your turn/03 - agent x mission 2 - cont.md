# Agent X, Mission 2 — Mysterious Cryptogram (cont.)

# THIS PAGE IS UNDER CONSTRUCTION

# I Thought There Was a Choice To Be Made

On the previous page, I indicated the Algorithm X setup could be “Very Hard or Not Too Bad, Your Choice”. In this section, I will cover the harder option. 

Coloring is a great fit for Agent X, Mission 2. You could use coloring on just about any puzzle you wish to, but I don’t recommend that. This is an Algorithm X playground and my goal is to demonstrate the tremendous power of Algorithm X and the many different types of problems it can solve. Every now and then, coloring is a better option.

The first puzzle covered in this section was building a word search. I have a few ideas in regard to how that puzzle could be approached purely with Algorithm X, but each of those ideas feels like climbing an enormous mountain. This Agent X, Mission 2 puzzle is a different story. Although the climb is strenuous, there is much to be learned by solving this puzzle with and without coloring.

# Solving Agent X, Mission 2 Without Coloring

This puzzle can be solved without any coloring at all. I found this approach challenging, in a very fun way of course.

Coloring allows us to easily model and implement things that must be the same or situations where consistency is crucial. How else can we model things that must be the same? Based on what must be the same, we can identify everything that must be different. This technique was used multiple times in the section on Generalized Exact Cover, more specifically on puzzles that featured [mutual exclusivity](mutual-exclusivity).

Let’s consider how this puzzle can be solved without coloring. Since we will strictly use the requirements, optional requirements and actions of Algorithm X, actions cannot involve placing one register word on one cipher word. Instead, we must be more granular and make all actions assigning one register letter to one cipher letter. Cipher letters are either covered, or they are not. Register letters are either used, or they are not. All cipher letters __must__ be covered. All register letters __may__ be used. Everything is binary and suitable for Algorithm X.

Mutual Exclusivity allows Algorithm X to easily ensure certain situation do not happen. In order to determine what must __not__ happen in this puzzle, it is necessary to first identify what could happen. Once again, consider the Example Test Case. Go through each combination of words and build a matrix of _what is possible_. On the previous page, the gameboard shows the register word `PART` being mapped to the cipher word `TIFS`. This is a legitimate possibility. Because it is possible to map these two words to each other, what do we know is possible about the cipher letters and the register letters?

* If register letter `P` is mapped to cipher letter `T`, the following are also possible:
  * Register letter `A` could be mapped to cipher letter `I`.
  * Register letter `R` could be mapped to cipher letter `F`.
  * Register letter `T` could be mapped to cipher letter `S`.
* If register letter `A` is mapped to cipher letter `I`, the following are also possible:
  * Register letter `P` could be mapped to cipher letter `T`.
  * Register letter `R` could be mapped to cipher letter `F`.
  * Register letter `T` could be mapped to cipher letter `S`.
* If register letter `R` is mapped to cipher letter `F`, the following are also possible:
  * Register letter `P` could be mapped to cipher letter `T`.
  * Register letter `A` could be mapped to cipher letter `I`.
  * Register letter `T` could be mapped to cipher letter `S`.
* If register letter `T` is mapped to cipher letter `S`, the following are also possible:
  * Register letter `P` could be mapped to cipher letter `T`.
  * Register letter `A` could be mapped to cipher letter `I`.
  * Register letter `R` could be mapped to cipher letter `F`.

<BR>

All that for just one possible mapping of a register word to a cipher word??? After considering all legitimate combinations of register words and cipher words, what is left is a comprehensive matrix of __what is possible__. Because the sets of letters are finite, a comprehensive matrix of __what is NOT possible__ can be determined and how do we tell Algorithm X what is not possible? We build a list of optional requirements (`me_requirements`) to handle [mutual exclusivity](mutual-exclusivity).

To make this process just a bit more concrete, each `me_requirement` takes the form:

```python
((register_letter_1, cipher_letter_1), (register_letter_2, cipher_letter_2))
```

In other words, `register_letter_1` can be assinged to `cipher_letter_1` __OR__ `register_letter_2` can be assinged to `cipher_letter_2`, but both __MUST NOT__ happen in the same solution.

# Are You Kidding Me?

I optimized my code by only considering register words that truly could be mapped to certain cipher words. Of course, the words must be of the same length, but some pattern matching can also limit legitimate pairs. The next table displays how many requirements I constructed to handle mutual exclusivity for each test case.

<BR>

| Test Case | Number of me_requirements |
|:----|:---------------------:|
| 1 - First Contact | 1,412 |
| 2 - Longer Message with More Words | 28,236 |
| 3 - A Lot More Words | 47,211 |
| 4 - Final Test | 35,491 |

<BR>

There is good news and bad news about the size of these numbers. The good news is Algorithm X and DLX chewed through the matrix data like a hot knife through butter; no significant issues at all. The bad news is setting up the actions to feed to Algorithm X required a bit of optimization. After all, the more often you filter a list of 10s of thousands of `me_requirements`, the better chance that filtering takes an unreasonable amount of time.

# Conclusion

[Converting Mutual Inclusivity to Mutual Exclusivity](einsteins-riddle-solver)

9 3 2<BR>
205 18 10<BR>
652 116 40<BR>
303 318 100<BR>
