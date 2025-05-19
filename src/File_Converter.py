from pathlib import Path
from abc import ABC, abstractmethod

# --- Base Class for File Conversion ---
class FileConverter(ABC):
    def __init__(self, input_file):
        self.input_file = Path(input_file)
        self.output_file = self._generate_output_path()

    def _generate_output_path(self):
        return self.input_file.with_suffix(".md")

    @abstractmethod
    def convert_to_md(self):
        pass

    def save_markdown(self, content):
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Converted '{self.input_file.name}' to '{self.output_file.name}'")
        except Exception as e:
            print(f"Error saving Markdown for '{self.input_file.name}': {e}")

