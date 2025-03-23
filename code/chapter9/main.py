from enum import Enum

# Sum Types for Document Parsing
class Parsed:
    def __init__(self, doc_name, text):
        self.doc_name = doc_name
        self.text = text

class ParseError:
    def __init__(self, doc_name, err):
        self.doc_name = doc_name
        self.err = err

# Enum for Document Types
class DocType(Enum):
    PDF = "PDF"
    TXT = "TXT"
    DOCX = "DOCX"
    MD = "MD"
    HTML = "HTML"

# Format Conversion Function
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

# CSV Export Status Function
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

# Enum for Edit Types
class EditType(Enum):
    NEWLINE = "NEWLINE"
    SUBSTITUTE = "SUBSTITUTE"
    INSERT = "INSERT"
    DELETE = "DELETE"

# Document Editing Function
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

# Example Usage
if __name__ == "__main__":
    # Parsing Documents
    parsed_doc = Parsed("example.txt", "This is a sample document.")
    error_doc = ParseError("example.txt", "File not found.")

    def handle_parsed(doc):
        if isinstance(doc, Parsed):
            print(f"Document '{doc.doc_name}' parsed successfully: {doc.text}")
        elif isinstance(doc, ParseError):
            print(f"Error parsing '{doc.doc_name}': {doc.err}")

    handle_parsed(parsed_doc)  # Output: Document 'example.txt' parsed successfully: This is a sample document.
    handle_parsed(error_doc)   # Output: Error parsing 'example.txt': File not found.

    # Format Conversion
    content = "# This is a heading"
    converted_content = convert_format(content, DocType.MD, DocType.HTML)
    print(converted_content)  # Output: <h1>This is a heading</h1>

    # CSV Export
    data = [["Name", "Age"], ["Alice", "30"], ["Bob", "25"]]
    status, result = get_csv_status("PENDING", data)
    print(status)  # Output: Pending...
    print(result)  # Output: [['Name', 'Age'], ['Alice', '30'], ['Bob', '25']]

    # Document Editing
    document = "Line 1\nLine 2\nLine 3"
    edit = {"line_number": 1, "insert_text": " inserted", "start": 5}
    edited_doc = handle_edit(document, EditType.INSERT, edit)
    print(edited_doc)  # Output: Line 1\nLine 2 inserted\nLine 3