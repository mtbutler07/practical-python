# Practical Python Walkthrough

Notes for working through the exercises in the [Practical Python course](https://dabeaz-course.github.io/practical-python/).

## Statements

A python program is a sequence of statements:

```python
a = 3 + 4
```

Each statement is terminated by a newline.
Statements are executed one after the other until control reaches the end of the file.

## Types

Python is dynamically typed.
The perceived type of a variable might change as a program executes depending on the current value assigned to it.

```python
whole_num = 4         # perceived as a int
float_num = 3.14      # perceived as a float
name = "Marcus"       # perceived as a str
```

## Numbers

Python has 4 different types of numbers

- Booleans
- Integers
- Floating point
- Complex (Imaginary numbers)

### Booleans (bool)

Booleans have two values: `True`, `False`
Booleans can also be evaluated as integers with values `1`, `0`

```python
c = 4 + True # 5
d = False
if d == 0:
    print('d is False')
```

### Integers (int)

Signed values of arbitrary size and base

```python
pos_int = 42
neg_int = -42
hexadecimal = 0x7fa8
octal = 0o253
binary = 0b10001111
```

Integer Operations:

```text
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide (produces a float)
x // y     Floor Divide (produces an integer)
x % y      Modulo (remainder)
x ** y     Power
x << n     Bit shift left
x >> n     Bit shift right
x & y      Bit-wise AND
x | y      Bit-wise OR
x ^ y      Bit-wise XOR
~x         Bit-wise NOT
abs(x)     Absolute value
```

### Floating Point (float)

Uses a decimal or exponential notation and represented as double precision (17 digits / exponent -308 - 308) using IEEE 754.

```python
float_a = 3.1415
float_exp = 4e5
all_float_on = -3.1415e-10
```

Floating Point Operations:

```text
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide
x // y     Floor Divide
x % y      Modulo
x ** y     Power
abs(x)     Absolute Value

math.sqrt(x)
math.sin(x)
math.cos(x)
math.tan(x)
math.log(x)
```

## Printing

Python uses the built in function `print()` for printing to the console.
The full list of built-in types is available [here](https://docs.python.org/3/library/functions.html#built-in-functions).

```python
print("Hello World")
```

Variables can also be passed to the `print()` function.

```python
sentence = "Hello Marcus"
print(sentence) #
```

Multiple variables can also be passed in when separated by a comma.

```python
x = "Hello"
y = "Marcus"
print(x, y) # Prints Hello Marcus
```

`print()` will add a single whitespace between the variables and also places a newline at the end.

The new line can be suppressed using the `end` parameter when calling the `print()` function.

```python
print('Hello', end=' ')
print('My name is', 'Marcus')
```

## User Input

To read input from a users keyboard, using the built-in `input()` function.

```python
name = input('Type your name: ') # This is prompt that will be presented to the user
print('Your name is', name)
```

The print statement will not be executed util the user presses the enter key.

## Indention

Indention is used to denote groupings of statements.
Python's only requirements is that indention within the same block be consistent on the number of spaces or tabs.

Best practices are:

1. Use spaces instead of tabs (Or have the IDE convert tabs to spaces)
2. Use 4 spaces for each indention level

## Strings

Strings are sequences of characters.

Individual characters within a string can be accessed by their index

```python
name = "Marcus"
print(name[0]) # prints M
```

Substrings can be accessed using a range of indices with `:`

```python
name = "Marcus"
print(name[0:3]) # prints Mar
print(name[0:]) # prints Marcus
print(name[3:]) # prints cus
```

String Methods

`rstrip()` will remove trailing (right) whitespace

```python
fname = "Marcus    "
lname = "Butler"
print(fname.rstrip(), lname) # prints Marcus Butler
```

`lstrip()` will remove leading (left) whitespace

```python
fname = "Marcus"
lname = "       Butler"
print(fname, lname.lstrip()) # prints Marcus Butler
```

`strip()` will remove both leading and trailing whitespace

```python
fname = "  Marcus      "
lname = "       Butler     "
print(fname.strip(), lname.strip()) # prints Marcus Butler
```

`upper())` will convert characters to upper case

```python
fname = "marcus"
print(fname.upper()) # prints MARCUS
```

`lower())` will convert characters to lower case

```python
fname = "MARCUS"
print(fname.lower()) # prints marcus
```

`replace(old, new))` will replace old character(s) with new character(s)

```python
name = "marcus_butler"
print(name.replace('_', ' ')) # prints marcus butler
```

Values can be converted to string using the `str()` function.

```python
num = 42
print(str(num)) # prints '42'
```

f-strings - A string with formatted expression substitution.

```python
symbol = 'IBM'
shares = 100
price = 91.1

fmt_str = f"{symbol:>10s} {shares:10d} {price:10.2f}"

print(fmt_str) # prints        IBM        100      91.10
```

Format Modifiers

```text
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```

Full documentation for codes is [available here](https://docs.python.org/3/library/string.html#format-specification-mini-language).

## Tuples

A tuple is a collection of values.
They are typically used to represent a simple record or structure.
Generally they are a single object containing multiples parts of data.

The contents of a tuples are ordered and can be accessed like an array.

```python
data = ('FDX', 100, 232.79)
print(data[0])  # prints FDX
```

The parenthesis are optional, but encouraged

```python
data = 'FDX', 100, 232.79
```

Tuples are immutable, meaning that their contents cannot be modified once created.

```python
data = 'FDX', 100, 232.79
data[2] = 500
```

```console
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Tuples can be unpacked into multiple variables in one line.

```python
data = 'FDX', 100, 232.79
symbol, shares, price = data

print(shares) # prints 100
```

## Dictionaries

A dictionary is a mapping of keys to values. In other programming languages, they are called hash tables or associative arrays. The key serves as indices for accessing values.

```python
stock = {
    'symbol': 'FDX',
    'shares': 100,
    'price': 232.79
}

print(stock['price']) # prints 232.79
```

To add or modify values, assign them using the key name.

```python
stock = {}
stock['symbol'] = 'FDX'
stock['shares'] = 100
stock['price'] = 232.79
```

## Sets

Sets are collections of unordered unique items.

```python
# Defining a set
stonks = {'FDX', 'AAPL', 'MSFT'}

# Alternative syntax
stonks = set(['FDX', 'AAPL', 'MSFT'])
```

Sets are useful for eliminating duplicate elements

```python

stonks = ['FDX', 'AAPL', 'MSFT', 'AAPL']

unique = set(stonks)

print(unique) # prints {'MSFT', 'AAPL', 'FDX'}
```

Set Operations

```text
s1 | s2                 # Set union
s1 & s2                 # Set intersection
s1 - s2                 # Set difference
```

## Conditionals

The `if` keywords is used to execute a conditional.
The `else` keyword is optional.

```python
if 4 > 3:
    print("Made it here!")
else:
    print("If you see this, something very wrong has happened :(")
```

Multiple conditions can be evaluated by using the `elif` keyword

```python
if 3 > 4:
    print("Not executed")
elif 10 > 7:
    print("Made it here!")
else:
    print("Not executed either")
```

## Looping

The `while` keyword executes a loop.
The statements within the while block will execute until some condition is met.

```python
index = 0
stop = 10

while index < stop:
    index += 1
    print(index)
```

# File IO

Opening and reading a text file

```python
f = open('filename.txt', mode='r')
data = f.read()
f.close()
print(data)
```

Opening and writing to a text file

```python
f = open('filename.txt', mode='w')
f.write('Hello World!')
f.close()
```

Using a context manager to open and close the file.
The file is opened as soon as control enters the indented code block and
closed upon leaving.

```python
with open('filename.txt', mode='r') as f:
    data = f.read()
print(data)
```
