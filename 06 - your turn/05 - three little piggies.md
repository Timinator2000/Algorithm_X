# Three Little Piggies

__Puzzle:__ [Three Little Piggies](https://www.codingame.com/training/hard/three-little-piggies)

__Author:__ [@nicola](https://www.codingame.com/profile/21bf42f790de293c3aef398f18cd2627479878)

__Published Difficulty:__ Hard

__Algorithm X Complexity:__ Pigs In Houses? Day? Night? Lot's of Options Create Complexity

# Strategy

Where do I so often start? How should we visualize placing tiles on a gameboard? The easy answer is the gameboard is what is given in the input and the tiles are the 3 houses. Seems easy, but I opted for another route.

Once again, I chose to consider the gameboard a mostly blank canvas. Some locations have pencil marks indicating where pigs need to be, where the wolf needs to be if it is night and where the trees need to be. Rather than just placing houses on the gameboard, I prefer having to place all the elements on the gameboard – the trees, the pigs, the wolf __and__ the houses.

# Requirements

This puzzle is interesting because the requirements are different depending on day or night. At night, the wolf must be placed on the board. During the day pigs must be placed on the board. At night, pig locations must be properly covered by houses. During the day, trees must be placed on the board.

Do the _requirements_ actually change from day to night? Let’s look at this another way. Maybe the requirements do not change as much as we think. Maybe it is the list of possible actions where most change takes place. For instance, all pig locations must be covered. This is the same for day and night. However, during the day, those locations are covered by pig “tiles”, while at night those locations are covered by house “tiles”.

Remember, the tiles are the action steps I can take to build a solution. At night I have a wolf tile. During the day, I do not. During the day, I have 2 or 3 pig tiles. At night, I don’t have any pig tiles. During the day, I also requirements that force 
