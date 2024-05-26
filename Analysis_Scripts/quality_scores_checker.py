import sys
def extract_quality_scores(fastq_file, num_lines=5000000):
    quality_scores = set()
    line_count = 0

    with open(fastq_file, 'r') as file:
        for line in file:
            line_count += 1
            # Quality scores are on every 4th line in a FASTQ file
            if line_count % 4 == 0:
                for char in line.strip():
                    quality_scores.add(char)
            # Stop after reading the specified number of lines
            if line_count >= num_lines:
                break

    return quality_scores


if __name__ == "__main__":
    fastq_file = "/home/tus53997/SeqBench/DecompressedOutput/ERR899714_1_10000000.fastq_-c_-l_-q_ill_bin.spring.fastq"
    quality_scores = extract_quality_scores(fastq_file)
    print("Individual Quality Scores Count:", len(quality_scores))
    for q in quality_scores:
        print(ord(q) - 33)
