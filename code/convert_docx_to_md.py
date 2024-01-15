
import subprocess
from pathlib import Path

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
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    for original_filepath in Path(source_folder).glob('*.docx'):        
        # original_filepath = original_filepath.resolve()
        # original_filename = original_filepath.name
        converted_filename = original_filepath.stem.replace(" ","-") + '.md'
        converted_file_path = Path(output_folder, converted_filename)
        print(f"-------\nConverting:\n {original_filepath}\n-to-\n{converted_file_path}")
        # Call pandoc to convert docx to markdown
        subprocess.run(['pandoc', '-o', str(converted_file_path), str(original_filepath)])
        print("Success!\n-------")


if __name__ == "__main__":
    source_directory = r'C:\Users\jonma\Downloads\UnterseeCapstoneMaterialsDocx'
    output_directory = r'C:\Users\jonma\Downloads\UnterseeCapstoneMaterialsMd'
    convert_docs_to_md(source_directory, output_directory)
