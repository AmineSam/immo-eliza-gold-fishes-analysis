import csv

input_file = 'data/raw/TF_SOC_POP_STRUCT_2025.txt'
output_file = 'data/raw/TF_SOC_POP_STRUCT_2025.csv'

print(f"Converting {input_file} to {output_file}...")

# Read the pipe-delimited file and write as CSV
with open(input_file, 'r', encoding='utf-8-sig') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    csv_writer = csv.writer(outfile)

    line_count = 0
    for line in infile:
        # Split by pipe and write as CSV row
        row = line.strip().split('|')
        csv_writer.writerow(row)

        line_count += 1
        if line_count % 100000 == 0:
            print(f"Processed {line_count:,} lines...")

print(f"Conversion complete! Processed {line_count:,} lines.")
print(f"Output saved to: {output_file}")
