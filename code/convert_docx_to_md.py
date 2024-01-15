
import os
from pathlib import Path
import subprocess

def convert_docs_to_md(source_folder: str, output_folder: str) -> None:
    """
    Convert .docx files in the source_folder to .md files and save them in the output_folder.

    Args:
        source_folder (str): The directory where the .docx files are located.
        output_folder (str): The directory where the .md files will be saved.

    Returns:
        None
    """
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for original_filename in os.listdir(source_folder):
        if original_filename.endswith('.docx'):
            original_filepath = os.path.join(source_folder, original_filename)
            converted_filename = os.path.splitext(original_filename.replace(" ","-"))[0] + '.md'
            converted_file_path = os.path.join(output_folder, converted_filename)
            print(f"-------\nConverting:\n {original_filename}\n-to-\n{converted_filename}")
            # Call pandoc to convert docx to markdown
            subprocess.run(['pandoc', '-o', converted_file_path, original_filepath])
            print("Success!\n-------")

            

if __name__ == "__main__":
    source_directory = r'C:\Users\jonma\Downloads\UnterseeCapstoneMaterialsDocx'
    output_directory = r'C:\Users\jonma\Downloads\UnterseeCapstoneMaterialsMd'
    Path(output_directory).mkdir(exist_ok=True, parents=True)

    convert_docs_to_md(source_directory, output_directory)
