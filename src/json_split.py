import json
import os
import sys
from colorama import Fore, Style, init
from InquirerPy import prompt

# Initialize colorama
init(autoreset=True)

def split_json(input_file, output_dir, num_files):
    with open(input_file, 'r') as f:
        data = json.load(f)

    input_filename = os.path.splitext(os.path.basename(input_file))[0]

    num_items = len(data)
    items_per_file = num_items // num_files

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_files):
        start = i * items_per_file
        end = (i + 1) * items_per_file
        if i == num_files - 1:
            end = num_items
        output_file = os.path.join(output_dir, f'{input_filename}_{i}.json')
        with open(output_file, 'w') as f:
            json.dump(data[start:end], f, indent=4)

    print(Fore.GREEN + f'Split {input_file} into {num_files} files in {output_dir}')

def main():
    # Command-line arguments
    args = sys.argv[1:]

    if len(args) < 1:
        input_file = prompt([{"type": "input", "message": "Enter the path to the input JSON file:", "name": "input_file"}])["input_file"]
    else:
        input_file = args[0]

    if len(args) < 2:
        output_dir = prompt([{"type": "input", "message": "Enter the output directory:", "name": "output_dir"}])["output_dir"]
    else:
        output_dir = args[1]

    if len(args) < 3:
        num_files = int(prompt([{"type": "input", "message": "Enter the number of files to split into:", "name": "num_files"}])["num_files"])
    else:
        num_files = int(args[2])

    split_json(input_file, output_dir, num_files)

if __name__ == '__main__':
    main()
