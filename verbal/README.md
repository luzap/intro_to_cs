# Verbal Arithmetic

## Introduction

This homework will test your understanding of backtracking by asking
you to write a program to solve "[verbal
arithmetic](https://en.wikipedia.org/wiki/Verbal_arithmetic)"
problems. Verbal arithmetic are words that, when their letters are
substituted with numbers, make a valid equation. The canonical
example is `SEND + MORE = MONEY`. A valid substitution would be:
```
SEND + MORE = MONEY
9567 + 1085 = 10652
```
A few things to note:

1. This assignment only deals with addition problems, subset of
   verbal arithmetic. Further, in all cases, the "right-hand" side of
   the equation will be a single word; so we will never solve
   something as or more complex than

   ```
   a + b + ... + y = z.
   ```
   In general, however, verbal arithmetic can be arbitrarily
   complicated.
2. The solution to an equation in general, and those provided with
   this assignment in particular, may not be unique.
3. Each letter should represent a unique number.
4. The leading digit of any number cannot be zero.

To solve a verbal arithmetic problem, one must deduce the proper
numeric substitutions for the various letters in the sentence. Such
deduction is similar to, and often the basis of, techniques for
solving other logic puzzles such as Sudoku, Hidato, Kakuro, and even
cross word puzzles. In all such instances,
[backtracking](https://en.wikipedia.org/wiki/Backtracking) is a good
technique for finding a solution.

## Basic functionality (50 points)

The components of your implementation are broken down into various
functions. Each function must follow the definition. The set of
functions should be placed in a single Python file called
`valib.py`; a skeleton file has been provided.

### Create the equation (7 points)

```python
def create(eq_file):
    # returns a list
```
Create an "equation" from a given file. Each number in the file
(or, more accurately, *word*) is on a separate line:
```bash
$> cat equations/00.txt
SEND
MORE
MONEY
```
This function should read that file, making each line a separate
element of the list:
```python
>>> eq = create('equations/00.txt')
>>> print(eq)
[ 'SEND', 'MORE', 'MONEY' ]
```

### Print the equation (7 points)

```python
def display(equation)
    # no return value
```

Given an equation -- a list of strings -- prints the formatted equation:
```
>>> display(create('equations/00.txt'))
   SEND
+  MORE
-------
  MONEY
```
Note that each word is right-aligned, an addition sign is placed
before the last left-hand word, and an ASCII equality bar is printed
before the result word. If the equation has more than two left-hand
words, only a single addition sign is required:
```
>>> display(create('equations/01.txt'))
   SEND
      A
    TAD
+  MORE
-------
  MONEY
```
If the equation has been solved, then passing it to display will print
the solution:
```
>>> display(solve(create('equations/00.txt')))
   9567
+  1085
-------
  10652
```
The formatting is the same, but the letters are replaced with numbers.

### Next guess (7 points)
```python
def guess(equation)
    # returns a list
```

Return a list of numbers between zero and nine excluding the numbers
present in equation. If the equation is full -- it contains no
letters -- the function should return an empty list:
```python
>>> guess(['A1B2C3', 'Z9'])
[ 0, 4, 5, 6, 7, 8 ]
```
For grading purposes, the order of the returned list does not matter.

### Replace a character with a number (7 points)
```python
def replace(equation, number)
    # returns a list
```

Replace a letter in the equation with `number`. Which letter to
replace is up to you (see below for a recommendation), but all
instances of that letter should be replaced. The function should
return a new equation -- a list of strings -- containing the
replacement.

Keep in mind that there are string methods provided by Python to help
distinguish a number from a letter:
```python
>>> '1'.isalpha()
False
>>> 'A'.isdigit()
False
```
Play around with different strings to get a feel for the semantics of
these methods.

### Is the equation correct? (7 points)
```python
def accept(equation)
    # returns a Boolean
```

Given an equation, returns whether that equation is valid:

1. In the given equation, a list consisting of n words, words zero
   through n-1 sum to the value of word n.
2. Words in the equation consist entirely of numbers.
3. All numbers begin with a value greater-than zero.

If any of these conditions are not met, the function should return
`False`.

### Are the current substitutions valid? (7 points)
```python
def reject(equation)
    # returns a Boolean
```

Part of what makes backtracking so powerful is its ability to realize
when a certain path will not lead to a solution. In this case, that
means determining whether a partially filled equation will eventually
lead to a solution. That is the purpose of this function. How you make
that determination is up to you, but it must be made.

A naive approach, commonly referred to as "brute force," would be for
this function to always return `False`. In that case, the backtracking
algorithm would try every complete equation possibility until a valid
solution is found. Your implementation should do something smarter.

### Solve the equation (8 points)
```python
def solve(equation)
    # returns a list
```

The function that orchestrates the backtracking: if the equation is
not solved or cannot be declared invalid, keep guessing. On the other
hand, if the equation is solved, return it; otherwise, return an empty
list.

## Running the program

The Python file `run.py` has been provided to facilitate running the
functions you have implemented. Thus, you should put your
implementations in a separate file. To execute `run.py`, it is
important that the file containing your function implementations be
called `valib.py` and be in the same directory as `run.py`. You are
free to alter `run.py` as you see fit, but your final submission
should at least work with the version provided here.

Various equations have been provided for you to test your code. Files
for each can be found in the ZIP archive above. You can test your
implementation against these equations by altering the filename passed
to `create` in `run.py`.

## Backtracking (20 points)

Although your implementation of `solve` might follow the generic
semantics of backtracking, if it is not optimized, it might not
actually be taking advantage of backtracking's benefits. As mentioned
above, for example, if `reject` rejects everything, then you will
potentially present more candidate solutions to `solve` than
necessary.

You are free to implement these functions in ways that you feel are
optimal. We encourage you, in fact, to think creatively about what is
happening and devise "smart" approaches to guessing, replacement, and
reject-determination. One suggestion is as follows:

* Consider a simple equation `['AB', 'CD', 'EF']`. If the letters B,
  D, and F have been replaced with 1, 2, and 4, respectively, then
  there is no point in trying to continue with the current equation:
  there are no replacements of A, C, or E that will make such a
  partial equation valid. If `reject` were to return `False` in this
  case, it would force `solve` to begin again with a different value
  for B, D, or F that is likely closer to a proper solution.

  * During replacement, giving precedence to the "right most"
    characters will likley help with this. Thus, when tasked with
    character replacement, it would therefore be wise to search the
    right-most position in each word and stop when a character is
    found.

To evaluate whether you are doing better than brute force, we will
time your code against a brute force implementation. To get full
credit for your backtracking implementation, you must, on average, do
better than a naive approach.

## Expectations (30 points)

1. The code that you submit should run. Even if you have not
   implemented all parts of the assignment, the subset of parts that
   are implemented should be free of Python errors.

2. There should be comments throughout the program:

   * A few lines at the top of the file specifying (at least) your
     name and net ID.
     
   * If you write a function -- irrespective of whether that function
     is required -- talk about it a hi-level: what it does; what types
     it takes; what types it returns; and what's the point.
     
   * If the block of a loop or a decision structure is longer than six
     or seven lines, a comment at the top outlining the point of the
     block is helpful.

   * If you use a concept that has not been covered in class,
     something you found online perhaps, you should add a comment
     explaining what is going on. Without an explanation, we can only
     assume you have cheated.

## Overtime

If you decide to implement these features, please make two
submissions: one that implements the original specification, and
another that implements the extra features.

## Submission

A single Python file should be submitted via NYU Classes, against the
corresponding homework assignment. There is no need to submit the
verbal arithmetic (text) files.

Any submission after the deadline, including re-submissions, will be
regarded as late and penalized accordingly.
