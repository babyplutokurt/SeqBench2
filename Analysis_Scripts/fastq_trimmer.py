import argparse


def extract_lines(num, input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for _ in range(num * 4):
                line = infile.readline()
                if not line:
                    break
                outfile.write(line)
        print(f"Successfully created {output_file} with the first {num} records from {input_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='Extract the first num lines from a FASTQ file.')
    parser.add_argument('num', type=int, help='Number of lines to extract')
    parser.add_argument('input_file', type=str, help='Input FASTQ file')
    parser.add_argument('output_file', type=str, help='Output FASTQ file')

    args = parser.parse_args()

    extract_lines(args.num, args.input_file, args.output_file)


if __name__ == "__main__":
    extract_lines(500000, "/scratch/tus53997/FASTQ/SRR1295433_1.fastq",
                  "/scratch/tus53997/FASTQ/SRR1295433_1_500000.fastq")
    extract_lines(500000, "/scratch/tus53997/FASTQ/SRR1295433_2.fastq",
                  "/scratch/tus53997/FASTQ/SRR1295433_2_500000.fastq")

    extract_lines(500000, "/scratch/tus53997/FASTQ/ERR899712_1.fastq",
                  "/scratch/tus53997/FASTQ/ERR899712_1_500000.fastq")
    extract_lines(500000, "/scratch/tus53997/FASTQ/ERR899712_2.fastq",
                  "/scratch/tus53997/FASTQ/ERR899712_2_500000.fastq")

    extract_lines(500000, "/scratch/tus53997/FASTQ/ERR1044277_1.fastq",
                  "/scratch/tus53997/FASTQ/ERR1044277_1_500000.fastq")
    extract_lines(500000, "/scratch/tus53997/FASTQ/ERR1044278_2.fastq",
                  "/scratch/tus53997/FASTQ/ERR1044278_2_500000.fastq")

    extract_lines(500000, "/scratch/tus53997/FASTQ/ERR1050080_1.fastq",
                  "/scratch/tus53997/FASTQ/ERR1050080_1_500000.fastq")

    extract_lines(10000, "/scratch/tus53997/FASTQ/HG00733_lib04_20171213_FAH37423_DD_guppy_0.5.1.fq",
                  "/scratch/tus53997/FASTQ/HG00733_lib04_20171213_FAH37423_DD_guppy_0.5.1_10000.fq")



