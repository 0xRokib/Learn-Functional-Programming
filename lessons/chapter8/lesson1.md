# Python Decorators

## Introduction

Python decorators are a powerful tool that allows the modification of functions or methods using a special `@decorator` syntax. They provide a clean and readable way to enhance function behavior without modifying their actual implementation. Decorators are essentially higher-order functions that take a function as input and return a modified version of it.

## Basic Example of a Decorator

A simple example of a decorator that counts vowels in a given document:

```python
# Decorator function
def vowel_counter(func_to_decorate):
    def wrapper(doc):
        vowel_count = sum(1 for char in doc if char.lower() in "aeiou")
        print(f"Vowel count: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

# Using the decorated function
process_doc("Hello World")
# Output:
# Vowel count: 3
# Document: Hello World
```

## Understanding \*args and \*\*kwargs

Python provides `*args` and `**kwargs` to handle variable numbers of arguments.

### Example:

```python
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Output:
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}
```

## Decorator with Variable Arguments

A decorator that logs the function's call count while passing through arguments:

```python
def log_call_count(func_to_decorate):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        return func_to_decorate(*args, **kwargs)
    return wrapper

@log_call_count
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
# Output:
# Called 1 times
# Hello, Alice!
# Called 2 times
# Hello, Bob!
```

## Markdown to Text Decorator

This decorator removes Markdown syntax from string arguments before passing them to the function:

```python
def convert_md_to_txt(text):
    return text.replace("#", "").strip()

def markdown_to_text_decorator(func_to_decorate):
    def wrapper(*args, **kwargs):
        new_args = [convert_md_to_txt(arg) if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: convert_md_to_txt(value) if isinstance(value, str) else value for key, value in kwargs.items()}
        return func_to_decorate(*new_args, **new_kwargs)
    return wrapper

@markdown_to_text_decorator
def display_text(text):
    print(text)

display_text("# Hello World")
# Output:
# Hello World
```

## HTML Escape Decorator

Replaces special HTML characters with their escape sequences:

```python
def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            return decorated_func(text.replace(old, new))
        return wrapper
    return replace

@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return text

print(tag_pre("<div>Sample & text</div>"))
# Output:
# &lt;div&gt;Sample &amp; text&lt;/div&gt;
```

## Memoization with `lru_cache`

The `lru_cache` decorator from `functools` caches function results to improve performance.

### Example: Recursive Factorial with Caching

```python
from functools import lru_cache

@lru_cache()
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))
print(factorial(5))
print(factorial(12))
```

## Palindrome Checker with `lru_cache`

A recursive function to check palindromes with memoization:

```python
from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

## Conclusion

Decorators enhance Python functions by providing reusable modifications without changing function logic. From logging and memoization to argument handling and HTML escaping, decorators make code cleaner and more maintainable. They are widely used in frameworks, authentication, and performance optimizations.
