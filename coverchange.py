import os
import sys

def process_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                process_markdown_file(filepath)

def process_markdown_file(filepath):
    lines = []
    cover_image = None

    with open(filepath, "r") as f:
        lines = f.readlines()

    with open(filepath, "w") as f:
        for line in lines:
            if line.strip().startswith("coverImage:") and ("." in line.strip()):
                cover_image = line.strip().split(":")[1].strip()[1:-1]
            f.write(line)
            if line.strip() == "---" and cover_image:
                f.write(f"\n![{cover_image}](/uploads/{cover_image})\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python this.py directory")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory.")
        sys.exit(1)

    process_markdown_files(directory)
