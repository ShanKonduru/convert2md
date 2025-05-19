
# --- Subclass for TXT Handling ---
from src.File_Converter import FileConverter


class TxtConverter(FileConverter):
    def convert_to_md(self):
        try:
            with open(self.input_file, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error processing TXT '{self.input_file.name}': {e}"
