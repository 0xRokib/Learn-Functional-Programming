# =========================================================
# 1. Functions as Values
# =========================================================

# 1.1 Functions as Values Example
def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

# Assigning the function 'add' to a variable 'addition'
addition = add
print(addition(2, 5))  # Output: 7


# =========================================================
# 2. Assignment: `file_to_prompt` Function
# =========================================================

# 2.1 Assignment Example: file_to_prompt Function
def file_to_prompt(file, to_string):
    """Formats the file content into a prompt string."""
    return f"```\n{to_string(file)}\n```"

# Example usage
file_content = "Hello, World!"
print(file_to_prompt(file_content, str))  # Output: ```\nHello, World!\n```


# =========================================================
# 3. Anonymous Functions (Lambda Functions)
# =========================================================

# 3.1 Anonymous Functions Example
add_one = lambda x: x + 1  # Adds 1 to the input
print(add_one(2))  # Output: 3

# Lambda function to get age from a dictionary
get_age = lambda name: {"lane": 29, "hunter": 69, "allan": 17}.get(name, "not found")
print(get_age("lane"))  # Output: 29


# =========================================================
# 4. Assignment: `file_type_getter` Function
# =========================================================

# 4.1 Assignment Example: file_type_getter Function
def file_type_getter(types):
    """Maps file extensions to their types and returns a lookup function."""
    mapping = {}
    for file_type, extensions in types:
        for ext in extensions:
            mapping[ext] = file_type
    return lambda ext: mapping.get(ext, "Unknown")

# Example usage
types = [("Image", ["jpg", "png"]), ("Document", ["pdf", "doc"])]
get_type = file_type_getter(types)
print(get_type("jpg"))  # Output: Image
print(get_type("txt"))  # Output: Unknown


# =========================================================
# 5. First-Class & Higher-Order Functions
# =========================================================

# 5.1 First-Class Functions Example
def square(x):
    """Returns the square of a number."""
    return x * x

# Assigning the function 'square' to a variable 'f'
f = square
print(f(5))  # Output: 25

# 5.2 Higher-Order Function Example
def my_map(func, arg_list):
    """Applies a function to each element in a list and returns the results."""
    return [func(i) for i in arg_list]

# Using the higher-order function 'my_map'
squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)  # Output: [1, 4, 9, 16, 25]


# =========================================================
# 6. Map Example
# =========================================================

# 6.1 Map Example
def square(x):
    """Returns the square of a number."""
    return x * x

# Using the built-in 'map' function
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(square, nums))
print(squared_nums)  # Output: [1, 4, 9, 16, 25]


# =========================================================
# 7. Assignment: `change_bullet_style` Function
# =========================================================

# 7.1 Assignment Example: change_bullet_style Function
def change_bullet_style(document):
    """Converts bullet points from '-' to '*' in a document."""
    convert_line = lambda line: "*" + line[1:] if line.startswith("-") else line
    return "\n".join(map(convert_line, document.split("\n")))

# Example usage
document = "- Item 1\n- Item 2\nNot a bullet"
print(change_bullet_style(document))  # Output: * Item 1\n* Item 2\nNot a bullet


# =========================================================
# 8. Filter Example
# =========================================================

# 8.1 Filter Example
def is_even(x):
    """Checks if a number is even."""
    return x % 2 == 0

# Using the built-in 'filter' function
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)  # Output: [2, 4, 6]


# =========================================================
# 9. Assignment: `remove_invalid_lines` Function
# =========================================================

# 9.1 Assignment Example: remove_invalid_lines Function
def remove_invalid_lines(document):
    """Removes lines starting with '-' from a document."""
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))

# Example usage
document = "- Invalid line\nValid line\n- Another invalid line"
print(remove_invalid_lines(document))  # Output: Valid line


# =========================================================
# 10. Reduce Example
# =========================================================

# 10.1 Reduce Example
import functools

def add(sum_so_far, x):
    """Adds two numbers."""
    return sum_so_far + x

# Using the 'reduce' function from the 'functools' module
numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
print(sum)  # Output: 10


# =========================================================
# 11. Assignment: `join_first_sentences` Function
# =========================================================

# 11.1 Assignment Example: join_first_sentences Function
def join(doc_so_far, sentence):
    """Joins sentences with a '.' separator."""
    return f"{doc_so_far}. {sentence}"

def join_first_sentences(sentences, n):
    """Joins the first 'n' sentences from a list."""
    return functools.reduce(join, sentences[:n]) + "." if n > 0 else ""

# Example usage
sentences = ["This is sentence 1", "This is sentence 2", "This is sentence 3"]
print(join_first_sentences(sentences, 2))  # Output: This is sentence 1. This is sentence 2.


# =========================================================
# 12. Set Intersection Example
# =========================================================

# 12.1 Set Intersection Example
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)  # Output: {3, 4}


# =========================================================
# 13. Assignment: `get_common_formats` Function
# =========================================================

# 13.1 Assignment Example: get_common_formats Function
def get_common_formats(formats1, formats2):
    """Returns common formats between two lists."""
    return set(formats1).intersection(set(formats2))

# Example usage
formats1 = ["jpg", "png", "pdf"]
formats2 = ["pdf", "doc", "jpg"]
print(get_common_formats(formats1, formats2))  # Output: {'jpg', 'pdf'}


# =========================================================
# 14. Zip Example
# =========================================================

# 14.1 Zip Example
a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip(a, b))
print(c)  # Output: [(1, 4), (2, 5), (3, 6)]


# =========================================================
# 15. Assignment: `pair_document_with_format` Function
# =========================================================

# 15.1 Assignment Example: pair_document_with_format Function
def pair_document_with_format(doc_names, doc_formats, valid_formats):
    """Pairs document names with their formats if the format is valid."""
    pairs = zip(doc_names, doc_formats)
    return list(filter(lambda pair: pair[1] in valid_formats, pairs))

# Example usage
doc_names = ["doc1", "doc2", "doc3"]
doc_formats = ["pdf", "doc", "jpg"]
valid_formats = ["pdf", "jpg"]
print(pair_document_with_format(doc_names, doc_formats, valid_formats))  # Output: [('doc1', 'pdf'), ('doc3', 'jpg')]


# =========================================================
# 16. Assignment: `restore_documents` Function
# =========================================================

# 16.1 Assignment Example: restore_documents Function
def restore_documents(originals, backups):
    """Restores documents by combining originals and backups, filtering out numbers, and converting to uppercase."""
    return set(map(str.upper, filter(lambda doc: not doc.isdigit(), originals + backups)))

# Example usage
originals = ["doc1", "123", "doc2"]
backups = ["doc2", "doc3", "456"]
print(restore_documents(originals, backups))  # Output: {'DOC1', 'DOC2', 'DOC3'}