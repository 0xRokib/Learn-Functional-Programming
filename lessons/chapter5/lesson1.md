# Function Transformations

## Overview

Function transformation is a type of higher-order function where a function takes another function as input and returns a new function. This technique enhances code reusability and flexibility.

## Why Use Function Transformations?

- **Code Reusability:** Functions can be dynamically modified without rewriting them.
- **Cleaner Code:** Function transformations keep logic modular and maintainable.
- **Customizable Behaviors:** Enables dynamic configuration of functions at runtime.
- **Dynamic Function Generation:** Allows functions to be created on the fly with different behaviors.

Function transformations help in developing scalable and maintainable applications by promoting code flexibility and reusability.

---

## Example: Higher-Order Function

```python
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))  # 25
print(double_func(5))  # 10
```

### Explanation

- The `self_math` function accepts a mathematical function (like `multiply` or `add`).
- It returns a new function `inner_func`, which applies the provided function with the same argument twice.
- `square_func(5)` computes `5 * 5 = 25`, and `double_func(5)` computes `5 + 5 = 10`.

---

## Assignment 1: Logging System

### Task

Implement the `get_logger` function to log messages using a given formatter function.

### Solution

```python
def get_logger(formatter):
    def logger(first, second):
        print(formatter(first, second))
    return logger
```

### Example Usage

```python
def colon_delimit(first, second):
    return f"{first}: {second}"

def dash_delimit(first, second):
    return f"{first} - {second}"

db_errors = ["out of memory", "cpu is pegged", "networking issue", "invalid syntax"]
logger = get_logger(colon_delimit)
for err in db_errors:
    logger("Doc2Doc FATAL", err)
```

### Expected Output

```
Doc2Doc FATAL: out of memory
Doc2Doc FATAL: cpu is pegged
Doc2Doc FATAL: networking issue
Doc2Doc FATAL: invalid syntax
```

### Explanation

- `get_logger` returns a `logger` function that prints messages using the provided `formatter` function.
- The example demonstrates logging database errors with a colon delimiter.

---

## Assignment 2: Filter Command

### Task

Implement `get_filter_cmd` that takes two filter functions and returns a filtering function.

### Solution

```python
def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option == "--one":
            return filter_one(content)
        elif option == "--two":
            return filter_two(content)
        elif option == "--three":
            return filter_two(filter_one(content))
        else:
            raise Exception("invalid option")
    return filter_cmd
```

### Example Usage

```python
def replace_bad(text):
    return text.replace("bad", "good")

def replace_ellipsis(text):
    return text.replace("..", "...")

filter_cmd = get_filter_cmd(replace_bad, replace_ellipsis)
print(filter_cmd("This is bad..", "--three"))
```

### Expected Output

```
This is good...
```

### Explanation

- The `filter_cmd` function applies different filters based on the provided option.
- `--one` replaces "bad" with "good".
- `--two` replaces ".." with "...".
- `--three` applies both filters sequentially.

---

## Assignment 3: Advanced Filter Command

### Task

Implement `get_filter_cmd` that processes content using multiple filters from a dictionary.

### Solution

```python
def get_filter_cmd(filters):
    def filter_cmd(content, options, word_pairs):
        if not options:
            raise Exception("missing options")

        for option in options:
            if option in filters:
                content = filters[option](content, word_pairs)
            else:
                raise Exception("invalid option")

        return content

    return filter_cmd
```

### Example Usage

```python
def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content

def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content

def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))

def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content

filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}

filter_cmd = get_filter_cmd(filters)
content = "this is a test. hello world."
print(filter_cmd(content, ["--capitalize"], []))
```

### Expected Output

```
This is a test. Hello world.
```

### Explanation

- `filter_cmd` processes the content based on given options and word pairs.
- `--replace` substitutes words.
- `--remove` removes specified words.
- `--capitalize` capitalizes sentences.
- `--uppercase` transforms words to uppercase.

---

These function transformation examples demonstrate how higher-order functions enhance flexibility and maintainability in programming!
