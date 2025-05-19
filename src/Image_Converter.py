# --- Subclass for Image Handling ---
from src.File_Converter import FileConverter


class ImageConverter(FileConverter):
    def convert_to_md(self):
        try:
            from PIL import Image
            image = Image.open(self.input_file)
            alt_text = self.input_file.stem  # Use filename without extension as alt text
            markdown_text = f"![{alt_text}]({self.input_file.name})"
            return markdown_text
        except ImportError:
            return "Error: Pillow library not installed. Please install it using 'pip install Pillow'"
        except Exception as e:
            return f"Error processing Image '{self.input_file.name}': {e}"

