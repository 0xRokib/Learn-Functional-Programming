# Currying in Functional Programming

## What is Currying?

Currying is a functional programming technique where a function that takes multiple arguments is transformed into a sequence of functions, each taking a single argument.

### Normal Function:

```python
# A function that takes multiple arguments
def box_volume(length, width, height):
    return length * width * height

print(box_volume(3, 4, 5))  # Output: 60
```

### Curried Function:

```python
# A curried function that takes arguments one at a time
def box_volume(length):
    def with_width(width):
        def with_height(height):
            return length * width * height
        return with_height
    return with_width

print(box_volume(3)(4)(5))  # Output: 60
```

## Why Use Currying?

Currying allows for function reuse and partial application, making code more modular and composable. It also helps functions conform to expected argument structures, making them compatible with higher-order functions.

### Example: Function Transformation for Compatibility

```python
def colorize(converter, doc):
    converter(doc)

# Function that normally takes two arguments
def markdown_to_html(asterisk_style):
    def asterisk_md_to_html(doc):
        pass  # Implementation
    return asterisk_md_to_html

markdown_to_html_italic = markdown_to_html('italic')
colorize(markdown_to_html_italic, "Sample doc")
```

## Examples of Currying

### 1. Adjusting Font Size

This function returns a modified font size based on the document type.

```python
def converted_font_size(font_size):
    def for_doc_type(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return for_doc_type

print(converted_font_size(12)("md"))  # Output: 24
```

### 2. Finding Lines Containing a Sequence

This function counts the number of lines in a document that contain a specified character sequence of a given length.

```python
def lines_with_sequence(char):
    def with_length(length):
        sequence = char * length
        def count_lines(doc):
            return sum(1 for line in doc.split("\n") if sequence in line)
        return count_lines
    return with_length

sample_doc = """aaaa
bbbb
ccdd
aabb"""
print(lines_with_sequence("a")(2)(sample_doc))  # Output: 2
```

### 3. Creating an HTML Table

This function generates an HTML table by first defining rows and then adding headers.

```python
def create_html_table(data_rows):
    rows = "".join(f"<tr>{''.join(f'<td>{cell}</td>' for cell in row)}</tr>" for row in data_rows)
    def create_table_headers(headers):
        nonlocal rows
        header_row = "<tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr>"
        return f"<table>{header_row}{rows}</table>"
    return create_table_headers

print(create_html_table([["Row 2, Cell 1", "Row 2, Cell 2"]])(["Header 1", "Header 2"]))
```

### 4. Markdown Image Generator

This function generates a Markdown image link with an optional title.

```python
def create_markdown_image(alt_text):
    def with_url(url):
        url = url.replace("(", "%28").replace(")", "%29")
        markdown = f"![{alt_text}]({url})"
        def with_title(title=None):
            return markdown if title is None else markdown[:-1] + f' "{title}")'
        return with_title
    return with_url

print(create_markdown_image("Example")("https://example.com")("Sample Title"))
```

### 5. Image Resizer

This function resizes an image while ensuring it stays within the given min and max constraints.

```python
def new_resizer(max_width, max_height):
    def set_min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise ValueError("minimum size cannot exceed maximum size")
        def resize_image(width, height):
            return min(max_width, max(min_width, width)), min(max_height, max(min_height, height))
        return resize_image
    return set_min_size

print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)
```

## Conclusion

Currying is a powerful technique in functional programming that allows for greater flexibility, code reusability, and function composition. It is particularly useful when dealing with higher-order functions, transformations, and function customization.
