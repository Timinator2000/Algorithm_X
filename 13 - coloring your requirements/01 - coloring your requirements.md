# Coloring Your Requirements

In his book, Donald Knuth identifies a category of problems where it is not only important to know which requirements have been covered, but also to know “how” those requirements have been covered. He proposes that sometimes requirements can be covered with a “color”, and if the color remains the same, certain requirements can be covered any number of times.

Going back to the analogy of tiles on a gameboard, the concept of coloring allows tiles to overlap. However, it is critical that the tiles be identical at the point of overlap. In his book, Knuth uses an example of building a word search puzzle. Given a list of words and a grid, put all the words on the grid, including horizontal words, vertical words, diagonal words and certain amount of overlap.

# Constructing a Word Search

Constructing a word search is a great fit for Algorithm X, until we get to the overlapping locations. What are the mandatory requirements? Each word must be placed somewhere on the grid. Are there any optional requirements? Each square of the grid may be covered by a letter, or it may be left empty, later to be filled with a letter that is not part of the solution. What about actions? Each action is simply putting a word on the grid at a specified location and in a specified direction.

What about the requirements satisfied by each action? A word has been placed on the grid and a certain number of cells have been covered. But what about multiple words that overlap. Two words that overlap were each placed on the board by a separate action and each of those actions covers the cell where the overlap occurs. You might be tempted to see this as an instance of the multiplicity discussed earlier, but there is a slight difference. In this example, each cell could be left uncovered or it could be covered multiple times, as long as it is covered by the same letter each time. For all multiplicity examples discussed previously, certain requirements needed to be covered an exact number of times.

__What does "coloring" mean?__

* __Mandatory Requirements:__ _Must_ be satisfied at least once, but may be satisfied many times as long as it is always satisfied or "colored" the same way.
 
* __Optional Requirement:__ Does _not_ need to be satisfied, but if satisfied, it may be satisfied any number of times as long as it is always satisfied or "colored" the same way.
 
  

The following table summarizes the concept of coloring requirements:

<BR>

| Requirement Type | What Does "Coloring" Mean?   |
|:-----:|:-----------------------|
| Mandatory Requirement | __Must__ be satisfied at least once, but may be satisfied many times as long as it is always satisfied or "colored" the same way. |
| Optional Requirement | Does __not__ need to be satisfied, but if satisfied, it may be satisfied any number of times as long as it is always satisfied or "colored" the same way. |

<BR>

# Algorithm C

Knuth proposes Algorithm C to solve exact cover problems that include the coloring of requirements. I am not going to cover Algorithm C here. This is an Algorithm X playground and on the next page, I will show you how to easily customize `AlgorithmXSolver` to handle requirements that can be colored.
