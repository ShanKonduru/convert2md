from src.File_Converter import FileConverter


class DocConverter(FileConverter):
    def convert_to_md(self):
        try:
            from docx import Document
            document = Document(self.input_file)
            markdown_text = ""
            for paragraph in document.paragraphs:
                markdown_text += paragraph.text + "\n\n"
            return markdown_text.strip()
        except ImportError:
            return "Error: python-docx library not installed. Please install it using 'pip install python-docx'"
        except Exception as e:
            return f"Error processing DOC/DOCX '{self.input_file.name}': {e}"
