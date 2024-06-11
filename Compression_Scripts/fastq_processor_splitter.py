import csv
import json
import os
import subprocess
import logging
from jinja2 import Template
import sys
import time

sys.path.append('../')
sys.path.append(os.path.join(os.path.dirname(__file__), 'build'))
import fastq_processor
import fastq_reconstructor

start = time.time()
input_path = "/home/tus53997/SeqBench/Test/ERR899714_1_10000000.fastq"
base_identifiers_path = "/home/tus53997/SeqBench/FASTQ/FASTQ_fields/ERR899714_1_1000000_base_id.fastq"
dna_bases_path = "/home/tus53997/SeqBench/FASTQ/FASTQ_fields/ERR899714_1_1000000_dna_bases.fastq"
quality_identifiers_path = "/home/tus53997/SeqBench/FASTQ/FASTQ_fields/ERR899714_1_1000000_quality_id.fastq"
quality_scores_path = "/scratch/tus53997/DecompressedOutput/HG00733_lib04_20171213_FAH37423_DD_guppy_0.5.1.fq_-f_-1_{Binary_length}_-M_REL_0.05.sz.bin"
output_path = "/home/tus53997/SeqBench/Test/output.fastq"


start = time.time()
fastq_reconstructor.fastq_reconstructor(base_identifiers_path, dna_bases_path, quality_identifiers_path, quality_scores_path, output_path)
end = time.time()

print(f"FASTQ file processing completed successfully in {end - start} seconds")
