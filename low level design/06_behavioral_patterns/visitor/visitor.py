"""Visitor Pattern: Double-dispatch document exporting to HTML and Markdown."""

from abc import ABC, abstractmethod
from typing import List


# Forward declarations
class Heading:
    pass


class Paragraph:
    pass


class CodeBlock:
    pass


# 1. Visitor Interface
class DocumentVisitor(ABC):
    @abstractmethod
    def visit_heading(self, element: "Heading") -> str:
        pass

    @abstractmethod
    def visit_paragraph(self, element: "Paragraph") -> str:
        pass

    @abstractmethod
    def visit_code_block(self, element: "CodeBlock") -> str:
        pass


# 2. Element Interface
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: DocumentVisitor) -> str:
        pass


# 3. Concrete Elements
class Heading(DocumentElement):
    def __init__(self, text: str, level: int = 1) -> None:
        self.text = text
        self.level = level

    def accept(self, visitor: DocumentVisitor) -> str:
        return visitor.visit_heading(self)


class Paragraph(DocumentElement):
    def __init__(self, text: str) -> None:
        self.text = text

    def accept(self, visitor: DocumentVisitor) -> str:
        return visitor.visit_paragraph(self)


class CodeBlock(DocumentElement):
    def __init__(self, code: str, language: str = "python") -> None:
        self.code = code
        self.language = language

    def accept(self, visitor: DocumentVisitor) -> str:
        return visitor.visit_code_block(self)


# 4. Concrete Visitor 1: Markdown Exporter
class MarkdownVisitor(DocumentVisitor):
    def visit_heading(self, element: Heading) -> str:
        hashes = "#" * element.level
        return f"{hashes} {element.text}"

    def visit_paragraph(self, element: Paragraph) -> str:
        return f"{element.text}\n"

    def visit_code_block(self, element: CodeBlock) -> str:
        return f"```{element.language}\n{element.code}\n```"


# 5. Concrete Visitor 2: HTML Exporter
class HTMLVisitor(DocumentVisitor):
    def visit_heading(self, element: Heading) -> str:
        return f"<h{element.level}>{element.text}</h{element.level}>"

    def visit_paragraph(self, element: Paragraph) -> str:
        return f"<p>{element.text}</p>"

    def visit_code_block(self, element: CodeBlock) -> str:
        return f"<pre><code class=\"language-{element.language}\">{element.code}</code></pre>"


if __name__ == "__main__":
    doc: List[DocumentElement] = [
        Heading("Low Level Design", level=1),
        Paragraph("Visitor pattern decouples algorithms from the object structure."),
        CodeBlock("print('Hello Visitor')", language="python")
    ]

    print("--- Rendered as Markdown ---")
    md_exporter = MarkdownVisitor()
    for el in doc:
        print(el.accept(md_exporter))

    print("\n--- Rendered as HTML ---")
    html_exporter = HTMLVisitor()
    for el in doc:
        print(el.accept(html_exporter))
