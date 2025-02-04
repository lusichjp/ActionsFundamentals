# scripts/example_script.py
import sys
import os
import json

def process_file(input_file):
    # Ensure the output directory exists
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    
    output_files = []
    for i, line in enumerate(lines):
        output_data = {"part_number": line}
        output_file = f"{output_dir}/output_{i}.json"
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=4)
        output_files.append(output_file)
    
    return lines

if __name__ == "__main__":
    input_file = sys.argv[1]
    elements = process_file(input_file)
    with open("elements.txt", "w") as f:
        for element in elements:
            f.write(f"{element}\n")
    print("Generated elements:", elements)
