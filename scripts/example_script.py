# scripts/example_script.py
import sys
import os
import json

def process_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    
    output_files = []
    for i, line in enumerate(lines):
        output_data = {"part_number": line}
        output_file = f"output/output_{i}.json"
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=4)
        output_files.append(output_file)
    
    return output_files

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_files = process_file(input_file)
    print("Generated files:", output_files)
