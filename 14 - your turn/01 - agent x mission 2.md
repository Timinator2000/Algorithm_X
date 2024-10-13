# Agent X, Mission 2 — Mysterious Cryptogram

__Puzzle:__ [Agent X, Mission 2 — Mysterious Cryptogram](https://www.codingame.com/training/medium/agent-x-mission-2mysterious-cryptogram)

__Author:__ [@Jnath](https://www.codingame.com/profile/4289b96dddd132fde4a14cf6f9c10bf22718561)

__Published Difficulty:__ Medium

__Algorithm X Complexity:__ Very Hard or Not Too Bad, Your Choice

# Strategy

Let’s begin with an excerpt from the puzzle statement:

>Your objective is to use a register of N words and a message (ciphertext), encrypted with a substitution table that you don't know, to find the decrypted message (plaintext) and part of the substitution table.
>Not every word in the register is in the message, but all words in the message are in the register.

For clarity, let’s assume the ciphertext has been parsed into a set of unique cipher words, leaving us with a list of cipher words and list of register words. Secondly, let’s assume sets of occurring letters have been compiled giving us a set of all cipher letters and a set of all register letters. I am using the term “letters” instead of “characters” because the problem states “substituted characters are only letters”.

The following are easily pulled from the above statements:

•	Requirements: Every cipher word must be mapped to exactly one register word.

•	Optional Requirements: Each register word might remain unused or it might be mapped to exactly one cipher word.

Ultimately, mapping the register words to the cipher words results in a substitution matrix that maps cipher letters to register letters. It is tempting to say:

•	Requirements: Every cipher letter must be mapped to exactly one register letter.

•	Optional Requirements: Each register letter might remain unused or it might be mapped to exactly one cipher letter.

# Avoid The Temptation Above!

Although both statements are accurate, taking a step back and looking at the tiles and the gameboard is helpful here. The gameboard is nothing more than a list of cipher words. The tiles are the register words. One-by-one, tiles are placed on the gameboard, but each tile covers several of the “letter requirements” depending on  the number of letters in the word. When you consider how many tiles a single letter might appear on, it becomes clear that the letter requirements above are candidates for coloring.

In the end, both statements above end up perfectly true, but during the process of placing tiles on the gameboard, each letter requirement could be covered many times. To find a proper solution, all the colorings across every covering must be consistent.

# Setting Up Your Solver


More to come...
