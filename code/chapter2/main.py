# Functions as Values Example
def add(x, y):
    return x + y

addition = add
print(addition(2, 5))  # Output: 7


# Assignment Example: file_to_prompt Function
def file_to_prompt(file, to_string):
    return f"```\n{to_string(file)}\n```"

# Example usage
file_content = "Hello, World!"
print(file_to_prompt(file_content, str))  # Output: ```\nHello, World!\n```



# Anonymous Functions Example
add_one = lambda x: x + 1
print(add_one(2))  # Output: 3

get_age = lambda name: {"lane": 29, "hunter": 69, "allan": 17}.get(name, "not found")
print(get_age("lane"))  # Output: 29


# Assignment Example: file_type_getter Function
def file_type_getter(types):
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


# First-Class & Higher-Order Functions Example
def square(x):
    return x * x

f = square
print(f(5))  # Output: 25

# Higher-Order Function Example
def my_map(func, arg_list):
    return [func(i) for i in arg_list]

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)  # Output: [1, 4, 9, 16, 25]


# Map Example
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = list(map(square, nums))
print(squared_nums)  # Output: [1, 4, 9, 16, 25]


# Assignment Example: change_bullet_style Function
def change_bullet_style(document):
    convert_line = lambda line: "*" + line[1:] if line.startswith("-") else line
    return "\n".join(map(convert_line, document.split("\n")))

# Example usage
document = "- Item 1\n- Item 2\nNot a bullet"
print(change_bullet_style(document))


# Filter Example
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)  # Output: [2, 4, 6]


# Assignment Example: remove_invalid_lines Function
def remove_invalid_lines(document):
    return "\n".join(filter(lambda line: not line.startswith("-"), document.split("\n")))

# Example usage
document = "- Invalid line\nValid line\n- Another invalid line"
print(remove_invalid_lines(document))


# Reduce Example
import functools

def add(sum_so_far, x):
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
print(sum)  # Output: 10

# Assignment Example: join_first_sentences Function
def join(doc_so_far, sentence):
    return f"{doc_so_far}. {sentence}"

def join_first_sentences(sentences, n):
    return functools.reduce(join, sentences[:n]) + "." if n > 0 else ""

# Example usage
sentences = ["This is sentence 1", "This is sentence 2", "This is sentence 3"]
print(join_first_sentences(sentences, 2))  # Output: This is sentence 1. This is sentence 2.


# Set Intersection Example
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)  # Output: {3, 4}


# Assignment Example: get_common_formats Function
def get_common_formats(formats1, formats2):
    return set(formats1).intersection(set(formats2))

# Example usage
formats1 = ["jpg", "png", "pdf"]
formats2 = ["pdf", "doc", "jpg"]
print(get_common_formats(formats1, formats2))  # Output: {'jpg', 'pdf'}


# Zip Example
a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip(a, b))
print(c)  # Output: [(1, 4), (2, 5), (3, 6)]


# Assignment Example: pair_document_with_format Function
def pair_document_with_format(doc_names, doc_formats, valid_formats):
    pairs = zip(doc_names, doc_formats)
    return list(filter(lambda pair: pair[1] in valid_formats, pairs))

# Example usage
doc_names = ["doc1", "doc2", "doc3"]
doc_formats = ["pdf", "doc", "jpg"]
valid_formats = ["pdf", "jpg"]
print(pair_document_with_format(doc_names, doc_formats, valid_formats))  # Output: [('doc1', 'pdf'), ('doc3', 'jpg')]

# Assignment Example: restore_documents Function
def restore_documents(originals, backups):
    return set(map(str.upper, filter(lambda doc: not doc.isdigit(), originals + backups)))

# Example usage
originals = ["doc1", "123", "doc2"]
backups = ["doc2", "doc3", "456"]
print(restore_documents(originals, backups))  # Output: {'DOC1', 'DOC2', 'DOC3'}