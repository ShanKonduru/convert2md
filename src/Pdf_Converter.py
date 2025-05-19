from src.File_Converter import FileConverter


class PdfConverter(FileConverter):
    def convert_to_md(self):
        try:
            from pdfminer.high_level import extract_text
            text = extract_text(self.input_file)
            return text
        except ImportError:
            return "Error: pdfminer.six library not installed. Please install it using 'pip install pdfminer.six'"
        except Exception as e:
            return f"Error processing PDF '{self.input_file.name}': {e}"
