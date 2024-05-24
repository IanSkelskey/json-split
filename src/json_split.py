# Split a large json file into a specified number of smaller json files
# Usage: python json_split.py <input_file> <output_dir> <num_files>
# Example: python json_split.py input.json output 10
# This will split input.json into 10 smaller files in the output directory

from InquirerPy import prompt
from colorama import init, Fore, Style

init(autoreset=True)
def split_json(input_file, output_dir, num_files):
    with open(input_file, 'r') as f:
        data = json.load(f)

    num_items = len(data)
    items_per_file = num_items // num_files

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_files):
        start = i * items_per_file
        end = (i + 1) * items_per_file
        if i == num_files - 1:
            end = num_items
        output_file = os.path.join(output_dir, 'output_{}.json'.format(i))
        with open(output_file, 'w') as f:
            json.dump(data[start:end], f, indent=4)

    print(Fore.GREEN + 'Split {} into {} files in {}'.format(input_file, num_files, output_dir))
				end = num_items
			output_file = os.path.join(output_dir, 'output_{}.json'.format(i))
			with open(output_file, 'w') as f:
				json.dump(data[start:end], f, indent=4)
    
	print('Split {} into {} files in {}'.format(input_file, num_files, output_dir))
 
if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Usage: python json_split.py <input_file> <output_dir> <num_files>')
		sys.exit(1)
	input_file = sys.argv[1]
	output_dir = sys.argv[2]
	num_files = int(sys.argv[3])
	split_json(input_file, output_dir, num_files)
