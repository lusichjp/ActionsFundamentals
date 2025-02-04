# scripts/example_script.py
import sys
import os

def process_file(input_file):
    # Simulate processing and generating output files
    with open(input_file, 'r') as f:
        data = f.read()
    
    output_files = []
    for i in range(3):  # Example: generating 3 output files
        output_file = f"output/output_{i}.txt"
        with open(output_file, 'w') as f:
            f.write(f"Processed data {i}: {data}")
        output_files.append(output_file)
    
    return output_files

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_files = process_file(input_file)
    print("Generated files:", output_files)
