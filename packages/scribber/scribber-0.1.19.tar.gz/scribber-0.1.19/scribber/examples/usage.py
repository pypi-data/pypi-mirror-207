from scribber import (
    SimpleDocument,
    Title,
    EmptyLine,
    Paragraph,
    Table,
    Director,
    CodeBlock,
    DocumentBuilder,
    ExcelDocument,
    MarkdownDocument,
    TextDocument,
    WordDocument,
)

CODE_EXAMPLE = """
import platform

def main():
    print("Hello World!")
    print(f"OS: {platform.system()}")
    
if __name__ == "__main__":
    main()             
"""

CODE_RESULT = """Hello World!
OS: Linux"""


if __name__ == "__main__":
    # Create abstract document
    doc = SimpleDocument()
    doc.add(Title(title="Funny report"))
    doc.add(EmptyLine())
    doc.add(Paragraph(text="Let me show you report"))
    doc.add(
        Table(
            headers=["one", "two", "three", "four"],
            content=[
                (1, 2, 3, 4),
                ("234", 345, 986, ""),
                (89, 35, 587643, 8675),
            ],
        )
    )
    doc.extend(
        (
            EmptyLine(),
            Title(title="Code block", level=2),
            CodeBlock(style="python", code=CODE_EXAMPLE),
            CodeBlock(style="console", code=CODE_RESULT),
            Paragraph(text="It's Ok!"),
        )
    )

    director = Director()
    text_report_builder = DocumentBuilder(doc=TextDocument())
    word_report_builder = DocumentBuilder(doc=WordDocument())
    excel_report_builder = DocumentBuilder(doc=ExcelDocument())
    markdown_report_builder = DocumentBuilder(doc=MarkdownDocument())

    print("Make a Text Document")
    director.builder = text_report_builder
    director.build_report_from_doc(doc)
    text_report_builder.parts.save("test.txt")

    print("Make a Word Document")
    director.builder = word_report_builder
    director.build_report_from_doc(doc)
    word_report_builder.parts.save("test.docx")

    print("Make a Excel Document")
    director.builder = excel_report_builder
    director.build_report_from_doc(doc)
    excel_report_builder.parts.save("test.xlsx")

    print("Make a Markdown Document")
    director.builder = markdown_report_builder
    director.build_report_from_doc(doc)
    markdown_report_builder.parts.save("test.md")

    print()
    print("Build without Director")
    text_report_builder.add_title(Title(title="Next report"))
    text_report_builder.add_paragraph(Paragraph(text="That is all!"))
    print(text_report_builder.parts.get_result())
