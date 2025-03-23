# A Python Example with Sum Types and Enums

This repository provides a detailed Python example demonstrating the use of **sum types**, **enums**, and **match statements** to handle document parsing, format conversion, CSV export, and document editing. The example mimics a simplified document processing system called **Doc2Doc**, which is designed to showcase functional programming concepts in Python.

## Overview

The **Doc2Doc** system is designed to handle various document-related operations, such as parsing, converting formats, exporting to CSV, and tracking edits. The example demonstrates how to use Python's features to implement these operations in a clean and maintainable way, inspired by functional programming principles.

While Python is not a statically typed language, it provides tools like **classes**, **enums**, and **match statements** to emulate sum types and handle fixed sets of values. This example shows how to use these tools effectively.

---

## Key Concepts

### Sum Types

A **sum type** is a type that can hold one of several possible values. In Python, sum types can be emulated using class inheritance. For example:

- A `Parsed` class represents a successfully parsed document.
- A `ParseError` class represents a failed parsing operation.

These classes are subclasses of a base class (e.g., `Document`), and the `isinstance()` function is used to determine which type a given object belongs to.

### Enums

An **enum** (enumeration) is a set of named values. In Python, the `Enum` class from the `enum` module is used to define enums. Enums are useful for representing a fixed set of values, such as document types (`PDF`, `TXT`, `DOCX`, etc.) or edit types (`NEWLINE`, `SUBSTITUTE`, etc.).

### Match Statements

The `match` statement (introduced in Python 3.10) is used to handle different cases based on the value of a variable. It is particularly useful when working with enums or sum types, as it allows for clean and readable pattern matching.

---

## Code Examples

### Parsing Documents

The `Parsed` and `ParseError` classes represent the result of a document parsing operation. The `Parsed` class stores the document name and content, while the `ParseError` class stores the document name and an error message.

```python
class Parsed:
    def __init__(self, doc_name, text):
        self.doc_name = doc_name
        self.text = text

class ParseError:
    def __init__(self, doc_name, err):
        self.doc_name = doc_name
        self.err = err
```

To handle parsing results, use the `isinstance()` function:

```python
def handle_parsed(doc):
    if isinstance(doc, Parsed):
        print(f"Document '{doc.doc_name}' parsed successfully: {doc.text}")
    elif isinstance(doc, ParseError):
        print(f"Error parsing '{doc.doc_name}': {doc.err}")
```

### Format Conversion

The `convert_format()` function converts a document from one format to another using a `match` statement. Supported conversions include:

- **MD to HTML**: Convert a Markdown heading to an HTML heading.
- **TXT to PDF**: Add `[PDF]` tags to the content.
- **HTML to MD**: Convert an HTML heading to a Markdown heading.

```python
def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocType.MD, DocType.HTML):
            return f"<h1>{content.lstrip('# ')}</h1>"
        case (DocType.TXT, DocType.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocType.HTML, DocType.MD):
            return f"# {content.replace('<h1>', '').replace('</h1>', '')}"
        case _:
            raise Exception("invalid type")
```

### CSV Export

The `get_csv_status()` function handles the status of a CSV export operation. It uses a `match` statement to process the data based on the export status (`PENDING`, `PROCESSING`, `SUCCESS`, or `FAILURE`).

```python
def get_csv_status(status, data):
    match status:
        case "PENDING":
            return ("Pending...", [list(map(str, row)) for row in data])
        case "PROCESSING":
            return ("Processing...", "\n".join([",".join(row) for row in data]))
        case "SUCCESS":
            return ("Success!", data)
        case "FAILURE":
            processed_data = "\n".join([",".join(row) for row in data])
            return ("Unknown error, retrying...", processed_data)
        case _:
            raise Exception("unknown export status")
```

### Document Editing

The `handle_edit()` function applies edits to a document based on the edit type (`NEWLINE`, `SUBSTITUTE`, `INSERT`, or `DELETE`). It uses a `match` statement to handle each type of edit.

```python
def handle_edit(document, edit_type, edit):
    match edit_type:
        case EditType.NEWLINE:
            lines = document.split('\n')
            lines[edit['line_number']] += '\n'
            return '\n'.join(lines)
        case EditType.SUBSTITUTE:
            lines = document.split('\n')
            line = lines[edit['line_number']]
            lines[edit['line_number']] = line[:edit['start']] + edit['insert_text'] + line[edit['end']:]
            return '\n'.join(lines)
        case EditType.INSERT:
            lines = document.split('\n')
            line = lines[edit['line_number']]
            lines[edit['line_number']] = line[:edit['start']] + edit['insert_text'] + line[edit['start']:]
            return '\n'.join(lines)
        case EditType.DELETE:
            lines = document.split('\n')
            line = lines[edit['line_number']]
            lines[edit['line_number']] = line[:edit['start']] + line[edit['end']:]
            return '\n'.join(lines)
        case _:
            raise Exception("unknown edit type")
```

---

## Usage

### Parsing a Document

```python
parsed_doc = Parsed("example.txt", "This is a sample document.")
error_doc = ParseError("example.txt", "File not found.")

handle_parsed(parsed_doc)  # Output: Document 'example.txt' parsed successfully: This is a sample document.
handle_parsed(error_doc)   # Output: Error parsing 'example.txt': File not found.
```

### Converting Document Formats

```python
content = "# This is a heading"
converted_content = convert_format(content, DocType.MD, DocType.HTML)
print(converted_content)  # Output: <h1>This is a heading</h1>
```

### Exporting CSV

```python
data = [["Name", "Age"], ["Alice", "30"], ["Bob", "25"]]
status, result = get_csv_status("PENDING", data)
print(status)  # Output: Pending...
print(result)  # Output: [['Name', 'Age'], ['Alice', '30'], ['Bob', '25']]
```

### Editing a Document

```python
document = "Line 1\nLine 2\nLine 3"
edit = {"line_number": 1, "insert_text": " inserted", "start": 5}
edited_doc = handle_edit(document, EditType.INSERT, edit)
print(edited_doc)  # Output: Line 1\nLine 2 inserted\nLine 3
```

---
