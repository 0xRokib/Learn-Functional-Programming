# First Class Function in Python

In Python, **First Class Functions** treat functions as first-class citizens, meaning functions can be assigned to variables, passed as arguments, and returned from other functions.

## What is First Class Function?

A **First Class Function** is a function that is treated as a value, just like strings, numbers, or lists.

### Example:

```python
def greet(name):
    return f"Hello, {name}"

# Assigning function to a variable
greeting = greet

print(greeting("Rokib"))
# Output: Hello, Rokib
```

## Functions as Arguments

Functions can be passed as arguments to other functions.

### Example:

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func, name):
    return func(f"Hello, {name}")

print(greet(shout, "Rokib"))
# Output: HELLO, ROKIB

print(greet(whisper, "Rokib"))
# Output: hello, rokib
```

## Functions as Return Values

Functions can return other functions.

### Example:

```python
def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(5))
# Output: 10

triple = multiplier(3)
print(triple(5))
# Output: 15
```

## Anonymous Functions (Lambda Functions)

Anonymous functions are functions without a name, defined using the `lambda` keyword.

### Example:

```python
square = lambda x: x * x
print(square(4))
# Output: 16

add = lambda x, y: x + y
print(add(3, 7))
# Output: 10
```

## Higher Order Functions

A **Higher Order Function** is a function that accepts other functions as arguments or returns a function.

### Example:

```python
def apply(func, value):
    return func(value)

result = apply(lambda x: x + 10, 20)
print(result)
# Output: 30
```

## Map Function

The `map()` function applies a given function to all items in an iterable.

### Example:

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)
# Output: [1, 4, 9, 16, 25]
```

### Assignment Example:

Convert bullet points:

```python
def change_bullet_style(document):
    convert = lambda line: line.replace("-", "*") if line.startswith("-") else line
    return "\n".join(map(convert, document.split("\n")))

doc = """- This is point 1
- This is point 2
* This is point 3"""

print(change_bullet_style(doc))
```

### Output:

```
* This is point 1
* This is point 2
* This is point 3
```

## Filter Function

The `filter()` function filters elements from an iterable based on a function that returns True or False.

### Example:

```python
nums = [10, 15, 20, 25, 30]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)
# Output: [10, 20, 30]
```

### Assignment Example:

Remove lines starting with `-`:

```python
def remove_invalid_lines(document):
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))

doc = """* Valid Line
- Invalid Line
* Another Valid Line"""

print(remove_invalid_lines(doc))
```

### Output:

```
* Valid Line
* Another Valid Line
```

## Reduce Function

The `reduce()` function reduces an iterable to a single value by applying a function repeatedly.

### Example:

```python
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)
# Output: 24
```

### Assignment Example:

Join sentences:

```python
from functools import reduce

def join(doc, sentence):
    return f"{doc}. {sentence}"

def join_first_sentences(sentences, n):
    return reduce(join, sentences[:n]) + "." if n > 0 else ""

sentences = ["Python is powerful", "It supports OOP", "It also supports FP"]
print(join_first_sentences(sentences, 2))
```

### Output:

```
Python is powerful. It supports OOP.
```

## Intersection

The `.intersection()` method finds common elements between two sets.

### Example:

```python
set1 = {"png", "jpg", "pdf"}
set2 = {"jpg", "pdf", "docx"}
common = set1.intersection(set2)
print(common)
# Output: {'jpg', 'pdf'}
```

## Zip Function

The `zip()` function combines two iterables element-wise into tuples.

### Example:

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
pairs = list(zip(names, ages))
print(pairs)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

## Conclusion

First Class Functions and Functional Programming concepts like `map()`, `filter()`, and `reduce()` make Python powerful and concise. They encourage writing clean, readable, and state-free code.

---

### Practice Questions

1. Write a lambda function to reverse a string.
2. Use `map()` to capitalize all words in a list.
3. Use `filter()` to extract all even numbers from a list.
4. Use `reduce()` to find the factorial of a number.
5. Find common elements between two lists using `.intersection()`.
