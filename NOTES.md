# Practical Python Walkthrough

Notes for working through the exercises in the [Practical Python course](https://dabeaz-course.github.io/practical-python/).


## Chapter 1

**Statements**

A python program is a sequence of statements:

```python
a = 3 + 4
```

Each statement is terminated by a newline. 
Statements are executed one after the other until control reaches the end of the file.

**Types**
Python is dynamically typed. 
The perceived type of a variable might change as a program executes depending on the current value assigned to it.

```python
whole_num = 4         # perceived as a int
float_num = 3.14      # perceived as a float
name = "Marcus"       # perceived as a str
```

**Printing**
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

**User Input**
To read input from a users keyboard, using the built-in `input()` function.

```python
name = input('Type your name: ') # This is prompt that will be presented to the user
print('Your name is', name)
```

The print statement will not be executed util the user presses the enter key.

**Indention**

Indention is used to denote groupings of statements. 
Python's only requirements is that indention within the same block be consistent on the number of spaces or tabs.

Best practices are:
1. Use spaces instead of tabs (Or have the IDE convert tabs to spaces)
2. Use 4 spaces for each indention level


**Conditionals**

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

**Looping**

The `while` keyword executes a loop. 
The statements within the while block will execute until some condition is met.

```python
index = 0
stop = 10

while index < stop:
    index += 1
    print(index)
```
