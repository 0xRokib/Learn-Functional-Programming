# Recursion Explained with Examples

This repository provides a clear explanation of recursion along with practical examples in Python. Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, more manageable subproblems. Each example is explained with a different case to help you understand how recursion works and when to use it.

---

## What is Recursion?

Recursion is a method of solving problems where a function calls itself in its definition. It consists of two main parts:

1. **Base Case**: The condition under which the recursion stops. Without a base case, the function would call itself indefinitely, leading to a stack overflow.
2. **Recursive Case**: The part of the function where it calls itself with a modified input, moving closer to the base case.

Recursion is particularly useful for problems that can be divided into smaller, similar subproblems, such as traversing trees, calculating factorials, or processing nested data structures.

---

## Examples

### 1. Factorial Calculation

**Problem:** Calculate the factorial of a number using recursion.

**Code:**

```python
def factorial_r(x):
    if x == 0:  # Base case
        return 1
    return x * factorial_r(x - 1)  # Recursive case

print(factorial_r(5))  # Output: 120
```

**Explanation:**

- The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`.
- **Base Case**: When `x == 0`, the factorial is `1` (by definition).
- **Recursive Case**: The function calls itself with `x - 1`, multiplying the result by `x`. This continues until the base case is reached.

**Example Walkthrough:**

```
factorial_r(5)
= 5 * factorial_r(4)
= 5 * (4 * factorial_r(3))
= 5 * (4 * (3 * factorial_r(2)))
= 5 * (4 * (3 * (2 * factorial_r(1))))
= 5 * (4 * (3 * (2 * (1 * factorial_r(0)))))
= 5 * (4 * (3 * (2 * (1 * 1))))  # Base case reached
= 120
```

---

### 2. Zipmap Function

**Problem:** Create a dictionary by mapping two lists (keys and values) using recursion.

**Code:**

```python
def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:  # Base case
        return {}
    rest = zipmap(keys[1:], values[1:])  # Recursive case
    rest[keys[0]] = values[0]
    return rest

zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# Output: {'Avatar: The Last Airbender': 9.9, 'Avatar (in Papyrus font)': 6.1, 'The Last Airbender (Live Action)': 2.1}
```

**Explanation:**

- The function maps the first element of `keys` to the first element of `values`, then recursively processes the rest of the lists.
- **Base Case**: If either list is empty, return an empty dictionary.
- **Recursive Case**: Call `zipmap` on the remaining elements of the lists and add the current key-value pair to the result.

**Example Walkthrough:**

```
zipmap(["A", "B"], [1, 2])
= {"A": 1} + zipmap(["B"], [2])
= {"A": 1} + ({"B": 2} + zipmap([], []))
= {"A": 1} + ({"B": 2} + {})  # Base case reached
= {"A": 1, "B": 2}
```

---

### 3. Nested Sum

**Problem:** Calculate the sum of all integers in a nested list using recursion.

**Code:**

```python
def sum_nested_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):  # Base case
            total += item
        elif isinstance(item, list):  # Recursive case
            total += sum_nested_list(item)
    return total

root = [1, 2, [3, 4]]
print(sum_nested_list(root))  # Output: 10
```

**Explanation:**

- The function iterates through each item in the list.
- **Base Case**: If the item is an integer, add it to the total.
- **Recursive Case**: If the item is a list, recursively call `sum_nested_list` to sum its elements.

**Example Walkthrough:**

```
sum_nested_list([1, 2, [3, 4]])
= 1 + 2 + sum_nested_list([3, 4])
= 1 + 2 + (3 + 4)  # Base case reached for [3, 4]
= 10
```

---

### 4. List Files in a Directory

**Problem:** Recursively list all file paths in a nested directory structure represented as a dictionary.

**Code:**

```python
def list_files(parent_directory, current_filepath=""):
    file_paths = []
    for key in parent_directory:
        new_filepath = current_filepath + "/" + key if current_filepath else key
        if parent_directory[key] == None:  # Base case
            file_paths.append(new_filepath)
        else:  # Recursive case
            file_paths.extend(list_files(parent_directory[key], new_filepath))
    return file_paths

directory = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}

file_paths = list_files(directory)
print(file_paths)
# Output: ['/Documents/Proposal.docx', '/Documents/Receipts/January/receipt1.txt', '/Documents/Receipts/January/receipt2.txt', '/Documents/Receipts/February/receipt3.txt']
```

**Explanation:**

- The function traverses a nested dictionary representing a directory structure.
- **Base Case**: If the value is `None`, the key is a file, and its path is added to the list.
- **Recursive Case**: If the value is a dictionary, the function calls itself to process the nested directory.

**Example Walkthrough:**

```
list_files({
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            }
        }
    }
})
= ["/Documents/Proposal.docx"] + list_files({"Receipts": {"January": {"receipt1.txt": None, "receipt2.txt": None}}})
= ["/Documents/Proposal.docx"] + (["/Documents/Receipts/January/receipt1.txt", "/Documents/Receipts/January/receipt2.txt"])
= ["/Documents/Proposal.docx", "/Documents/Receipts/January/receipt1.txt", "/Documents/Receipts/January/receipt2.txt"]
```

---

## Conclusion

Recursion is a powerful and elegant technique for solving problems that can be broken down into smaller, similar subproblems. By understanding the base case and recursive case, you can apply recursion to a wide range of problems, from mathematical calculations to processing complex data structures. These examples demonstrate how recursion works in practice and provide a foundation for tackling more advanced problems.
