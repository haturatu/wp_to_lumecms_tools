import os
import shutil
from deep_translator import GoogleTranslator

def translate_text(text, dest='en'):
    translator = GoogleTranslator(source='auto', target=dest)
    translation = translator.translate(text)
    return translation

def rename_index_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "index.md":
                parent_dir = os.path.basename(dirpath)
                new_filename = parent_dir + ".md"
                
                # Translate directory name if it contains non-ASCII characters
                if any(ord(char) > 127 for char in parent_dir):
                    translated_dir = translate_text(parent_dir)
                    new_filename = translated_dir + ".md"
                
                old_filepath = os.path.join(dirpath, filename)
                new_filepath = os.path.join(dirpath, new_filename)
                
                # Rename the file
                shutil.move(old_filepath, new_filepath)
                print(f"Renamed {old_filepath} to {new_filepath}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rename index.md files to their parent directory names.")
    parser.add_argument("directory", help="The root directory to start renaming from.")

    args = parser.parse_args()
    root_dir = args.directory

    rename_index_files(root_dir)

