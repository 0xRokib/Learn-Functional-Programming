# Pure Functions in Python

---

## 1. Pure Functions

A **pure function** is a function that:

1. Always returns the same output for the same input.
2. Has no side effects (it does not modify anything outside its scope).

### Example: Finding the Maximum Value in a List

```python
# Input
nums = [3, 1, 4, 1, 5, 9]

# Pure Function
def find_max(nums):
    max_val = float("-inf")  # Initialize with negative infinity
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

# Output
result = find_max(nums)
print(result)  # Output: 9

# Explanation:
# - The function `find_max` takes a list of numbers (`nums`) as input.
# - It iterates through the list to find the maximum value.
# - It does not modify any external state or rely on external data.
# - For the same input `nums`, it will always return the same output, making it a pure function.
```

---

## 2. Impure Functions

An **impure function** is a function that:

1. Modifies external state (e.g., global variables).
2. Relies on external data that can change.

### Example: Modifying a Global Variable

```python
# Input
nums = [3, 1, 4, 1, 5, 9]
global_max = float("-inf")  # Global variable

# Impure Function
def find_max(nums):
    global global_max  # Access the global variable
    for num in nums:
        if global_max < num:
            global_max = num

# Output
find_max(nums)
print(global_max)  # Output: 9

# Explanation:
# - The function `find_max` modifies the `global_max` variable, which exists outside its scope.
# - This makes the function impure because it has side effects.
# - If `global_max` is modified elsewhere in the program, the behavior of this function may change.
```

---

## 3. Pass by Reference vs. Pass by Value

In Python:

- **Mutable types** (e.g., lists, dictionaries) are passed by reference.
- **Immutable types** (e.g., integers, strings) are passed by value.

### Example: Modifying a List (Pass by Reference)

```python
# Input
outer_lst = [1, 2, 3]

# Function
def modify_list(inner_lst):
    inner_lst.append(4)  # Modifies the original list

# Output
modify_list(outer_lst)
print(outer_lst)  # Output: [1, 2, 3, 4]

# Explanation:
# - Lists are passed by reference, so the function modifies the original list.
# - This can lead to unintended side effects if the original list is used elsewhere in the program.
```

### Example: Modifying an Integer (Pass by Value)

```python
# Input
outer_num = 1

# Function
def attempt_to_modify(inner_num):
    inner_num += 1  # Modifies a copy of the integer

# Output
attempt_to_modify(outer_num)
print(outer_num)  # Output: 1

# Explanation:
# - Integers are passed by value, so the function does not modify the original integer.
# - This ensures that the original value remains unchanged, avoiding side effects.
```

---

## 4. Input and Output (I/O) in Pure Functions

Pure functions should avoid I/O operations like reading/writing files or printing to the console. Instead, they should return values.

### Example: Converting Text Case

```python
# Input
text = "Hello, World!"
target_format = "uppercase"

# Pure Function
def convert_case(text, target_format):
    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"Unsupported format: {target_format}")

# Output
result = convert_case(text, target_format)
print(result)  # Output: HELLO, WORLD!

# Explanation:
# - This function converts the case of the input text based on the `target_format`.
# - It does not perform any I/O operations, making it a pure function.
# - For the same input, it will always return the same output.
```

---

## 5. Memoization

**Memoization** is a technique to cache the results of expensive function calls to improve performance.

### Example: Caching Word Count

```python
# Input
document = "This is a sample document."
memos = {}

# Function
def word_count_memo(document, memos):
    memos_copy = memos.copy()  # Create a copy of the memo dictionary
    if document in memos_copy:
        return memos_copy[document], memos_copy  # Return cached result
    word_count = len(document.split())  # Compute word count
    memos_copy[document] = word_count  # Cache the result
    return word_count, memos_copy

# Output
word_count, memos = word_count_memo(document, memos)
print(word_count)  # Output: 5
print(memos)       # Output: {'This is a sample document.': 5}

# Explanation:
# - This function uses memoization to avoid recomputing the word count for the same document.
# - It creates a copy of the `memos` dictionary to avoid modifying the original input.
# - This ensures the function remains pure and predictable.
```

---

## 6. Referential Transparency

A function is **referentially transparent** if its call can be replaced by its return value without changing the program's behavior.

### Example: Adding Two Numbers

```python
# Input
x, y = 2, 3

# Function
def add(x, y):
    return x + y

# Output
result = add(x, y)
print(result)  # Output: 5

# Explanation:
# - The function call `add(2, 3)` can always be replaced with `5`.
# - This makes the function referentially transparent.
# - Referential transparency is a key property of pure functions.
```

---

## 7. Custom Commands and Side Effects

Avoid side effects by ensuring functions do not mutate their inputs.

### Example: Adding a Custom Command

```python
# Input
commands = {}
new_command = "greet"
function = lambda: print("Hello!")

# Pure Function
def add_custom_command(commands, new_command, function):
    commands_copy = commands.copy()  # Create a copy of the commands dictionary
    commands_copy[new_command] = function  # Add the new command
    return commands_copy

# Output
updated_commands = add_custom_command(commands, new_command, function)
print(updated_commands)  # Output: {'greet': <function <lambda> at 0x...>}

# Explanation:
# - This function adds a new command to a dictionary without modifying the original input.
# - It creates a copy of the `commands` dictionary to ensure no side effects.
# - This makes the function pure and predictable.
```

---

## 8. Sorting Dates

Sort dates by converting them into a consistent format.

### Example: Sorting Dates in "MONTH-DAY-YEAR" Format

```python
# Input
dates = ["12-31-2022", "01-15-2023", "10-05-2022"]

# Function
def sort_dates(dates):
    return sorted(dates, key=lambda date: date.split("-")[::-1])

# Output
sorted_dates = sort_dates(dates)
print(sorted_dates)  # Output: ['10-05-2022', '12-31-2022', '01-15-2023']

# Explanation:
# - This function sorts dates by converting them into "YEAR-MONTH-DAY" format for comparison.
# - It does not modify the original `dates` list, ensuring no side effects.
# - This makes the function pure and predictable.
```

---

## 9. Organizing Keywords

Filter and map keywords in a document without relying on global variables.

### Example: Finding Keywords in a Document

```python
# Input
document = "Functional programming is declarative and immutable."

# Function
def find_keywords(document):
    keywords = ["functional", "immutable", "declarative"]
    return [keyword for keyword in keywords if keyword in document.lower()]

# Output
keywords = find_keywords(document)
print(keywords)  # Output: ['functional', 'immutable', 'declarative']

# Explanation:
# - This function filters keywords in a document without modifying any external state.
# - It uses a list comprehension to check if each keyword exists in the document.
# - This makes the function pure and predictable.
```

---
