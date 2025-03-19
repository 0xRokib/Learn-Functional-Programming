# Closures in Python

## Introduction

A **closure** is a function that remembers variables from its enclosing scope, even after the scope has finished executing. This allows the function to retain state across multiple calls.

Closures are useful for:

- **Maintaining state** across multiple function calls without using global variables.
- **Encapsulating logic** while keeping data private.
- **Creating flexible function factories** that return specialized functions.

## How Closures Work

A closure is created when:

1. A function (inner function) is defined inside another function (outer function).
2. The inner function references variables from the outer function.
3. The outer function returns the inner function.
4. The returned inner function retains access to the outer function’s variables, even after the outer function has finished execution.

## Example

```python
def concatter():
    doc = ""
    def doc_builder(word):
        nonlocal doc
        doc += word + " "
        return doc
    return doc_builder

harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")
print(harry_potter_aggregator("Drive"))
```

### Output

```
Mr. and Mrs. Dursley of number four, Privet Drive
```

## Nonlocal Keyword

The `nonlocal` keyword allows modifying variables from an enclosing scope when they are immutable (like integers or strings). For mutable data types (like lists and dictionaries), `nonlocal` is not required.

---

## Assignments

### 1. Word Count Aggregator

Create a closure that tracks the total number of words across multiple documents.

#### Example Implementation

```python
def word_count_aggregator():
    count = 0
    def add_word_count(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return add_word_count

counter = word_count_aggregator()
print(counter("Hello world"))  # 2
print(counter("Python closures are useful"))  # 5
```

---

### 2. New Collection

Create a closure that maintains a list of document names without modifying the original input list.

#### Example Implementation

```python
def new_collection(initial_docs):
    docs = initial_docs[:]
    def add_doc(doc):
        docs.append(doc)
        return docs
    return add_doc

collection = new_collection(["doc1", "doc2", "doc3"])
print(collection("doc4"))  # ['doc1', 'doc2', 'doc3', 'doc4']
```

---

### 3. Clipboard Functionality

Create a clipboard system using closures.

#### Example Implementation

```python
def new_clipboard():
    clipboard = {}
    def copy_to_clipboard(key, value):
        clipboard[key] = value
    def paste_from_clipboard(key):
        return clipboard.get(key, "")
    return copy_to_clipboard, paste_from_clipboard

copy, paste = new_clipboard()
copy("greeting", "Hello World!")
print(paste("greeting"))  # Hello World!
```

---

### 4. User Words

Allow users to add words to a spellchecker.

#### Example Implementation

```python
def user_words(initial_words):
    words = set(initial_words)
    def add_word(word):
        words.add(word)
        return tuple(words)
    return add_word

spell_checker = user_words(("hello", "world"))
print(spell_checker("Python"))  # ('hello', 'world', 'Python')
```

---

### 5. CSS Styles

Manage CSS styles dynamically.

#### Example Implementation

```python
def css_styles(initial_styles):
    styles = {k: v.copy() for k, v in initial_styles.items()}
    def add_style(selector, property, value):
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property] = value
        return styles
    return add_style

styles = css_styles({"body": {"color": "black"}})
print(styles("h1", "font-size", "24px"))
```

---

### 6. Line Breaking

Break text into lines based on length constraints.

#### Example Implementation

```python
def line_breaker(line_length):
    def add_word_to_lines(lines, word):
        if not lines:
            return [word]
        current_line = lines[-1]
        if len(current_line) + len(word) + 1 > line_length:
            lines.append(word)
        else:
            lines[-1] += " " + word
        return lines
    return add_word_to_lines

breaker = line_breaker(10)
print(breaker([], "Hello"))
print(breaker(["Hello"], "World!"))
```

---

### 7. Currying Example

Implement currying for font size transformation.

#### Example Implementation

```python
def converted_font_size(font_size):
    def apply_doc_type(doc_type):
        scaling = {"header": 2, "body": 1, "footer": 0.8}
        return font_size * scaling.get(doc_type, 1)
    return apply_doc_type

font_converter = converted_font_size(12)
print(font_converter("header"))  # 24
print(font_converter("body"))  # 12
```

---

## Conclusion

Closures are useful for:

- **Retaining state** across function calls.
- **Encapsulating logic** while avoiding unnecessary global variables.
- **Functional programming paradigms**, such as currying and higher-order functions.

Mastering closures will help you write cleaner and more efficient Python code!
