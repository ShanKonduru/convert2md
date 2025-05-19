import os
from pathlib import Path

from src.Doc_Converter import DocConverter
from src.Image_Converter import ImageConverter
from src.Pdf_Converter import PdfConverter
from src.Txt_Converter import TxtConverter

def process_directory(root_dir):
    root_path = Path(root_dir)
    for item in root_path.rglob("*"):  # Recursively go through all files and directories
        if item.is_file():
            file_extension = item.suffix.lower()
            converter = None

            if file_extension == ".pdf":
                converter = PdfConverter(item, root_path)
            elif file_extension in [".doc", ".docx"]:
                converter = DocConverter(item, root_path)
            elif file_extension == ".txt":
                converter = TxtConverter(item, root_path)
            elif file_extension in [".jpg", ".jpeg", ".png", ".gif"]: # Add more image formats if needed
                converter = ImageConverter(item, root_path)
            elif file_extension == ".ppt" or file_extension == ".pptx":
                print(f"Skipping PPT/PPTX file: '{item.name}'. Conversion not yet implemented.")
                continue # Skip PPT for now
            else:
                print(f"Skipping unsupported file type: '{item.name}'")
                continue

            if converter:
                markdown_content = converter.convert_to_md()
                converter.save_markdown(markdown_content)

def main():
    print("Hello, World!")
    target_directory = input("Enter the root directory to process: ")
    if os.path.isdir(target_directory):
        process_directory(target_directory)
        print("Directory processing complete.")
    else:
        print(f"Error: '{target_directory}' is not a valid directory.")
if __name__ == "__main__":
    main()
