from pathlib import Path
from abc import ABC, abstractmethod
import os

# --- Base Class for File Conversion ---
class FileConverter(ABC):
    def __init__(self, input_file, input_root_path):
        self.input_file = Path(input_file)
        self.input_root_path = Path(input_root_path)
        self.output_root_path = self.input_root_path.parent / f"{self.input_root_path.name}-output"
        self.output_file = self._generate_output_path()

    def _generate_output_path(self):
        relative_path = self.input_file.relative_to(self.input_root_path)
        output_path = self.output_root_path / relative_path.with_suffix(".md")
        os.makedirs(output_path.parent, exist_ok=True)
        return output_path
        
    @abstractmethod
    def convert_to_md(self):
        pass

    def save_markdown(self, content):
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Converted '{self.input_file.name}' to '{self.output_file.name}' under '{self.output_root}'")
        except Exception as e:
            print(f"Error saving Markdown for '{self.input_file.name}': {e}")

