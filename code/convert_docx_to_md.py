
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

    for filename in os.listdir(source_folder):
        if filename.endswith('.docx'):
            filepath = os.path.join(source_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.md'
            output_file_path = os.path.join(output_folder, output_filename)

            # Call pandoc to convert docx to markdown
            subprocess.run(['pandoc', '-o', output_file_path, filepath])

            print(f"Converted {filename} to {output_filename}")

if __name__ == "__main__":
    source_directory = r'C:\Users\jonma\Downloads\UnterseeCapstoneMaterialsDocx'
    output_directory = r'C:\Users\jonma\Downloads\UnterseeCapstoneMaterialsMd'
    Path(output_directory).mkdir(exist_ok=True, parents=True)

    convert_docs_to_md(source_directory, output_directory)
