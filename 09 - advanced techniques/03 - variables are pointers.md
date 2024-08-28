# Python Variables

Understanding how variables truly work in Python is a learning experience every Python programmer goes through. With a bare minimal understanding of C and C++ pointers, I was thoroughly confused the first time I created a function in python with a list as an argument. I thought a copy of the list would be made and my original list would stay intact. Not the case!

Once you understand that all variables in Python are pointers to objects, your Python life becomes much more clear. If this is a new concept to you, do not worry that we are travelling down a path of C pointers and pointers to pointers, etc. As most things are in Python, it is much easier than you might expect.

On the website [Python Morsels](https://www.pythonmorsels.com/variables-are-pointers/), Trey Hunter does a nice job explaining how variables work in Python.

https://www.youtube.com/watch?v=g-iNz91YyGw

For even more detail, check out this write-up on [LaunchSchool.com](https://launchschool.com/books/python/read/variables_pointers).

# Why Is This Important?

In the next section, I am going to suggest making every cell in your Sudoku grid an object. Each grouping of cells (rows, columns and boxes) then becomes a list of pointers to a group of 9 cell objects. Let's take a closer look.
