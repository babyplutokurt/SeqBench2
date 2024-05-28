#!/bin/sh
#PBS -l walltime={{ walltime }}
#PBS -N {{ job_name }}
#PBS -q large
#PBS -l nodes={{ nodes }}:ppn={{ ppn }}
#PBS -M {{ email }}
#PBS -o {{ output_log }}
#PBS -e {{ error_log }}

{{ dependency_line }}

# change to directory where 'qsub' was called
cd $PBS_O_WORKDIR

source {{ conda_path }} compression

BINARY_LENGTH=$(($(stat -c %s "{{ binary_input_file }}") / 4))

get_time() {
    echo $(date +%s.%N)
}

# Run compression and capture metrics
START_TIME=$(get_time)

{{ reference_command }}
{{ compression_command }}

END_TIME=$(get_time)
COMPRESSION_DURATION=$(echo "$END_TIME - $START_TIME" | bc)

INPUT_SIZE_BYTES=$(stat -c %s "{{ input_path }}")
OUTPUT_SIZE_BYTES=$(stat -c %s "{{ compressed_output_path }}")
INPUT_SIZE_MB=$(echo "scale=6; $INPUT_SIZE_BYTES / 1048576" | bc)
OUTPUT_SIZE_MB=$(echo "scale=6; $OUTPUT_SIZE_BYTES / 1048576" | bc)

RATIO=$(echo "scale=6; $INPUT_SIZE_MB / $OUTPUT_SIZE_MB" | bc)
COMPRESSION_THROUGHPUT=$(echo "scale=6; $INPUT_SIZE_MB / $COMPRESSION_DURATION" | bc)

sleep 3

# Run decompression and capture metrics
START_TIME=$(get_time)

{{ decompression_command }}

END_TIME=$(get_time)
DECOMPRESSION_DURATION=$(echo "$END_TIME - $START_TIME" | bc)
DECOMPRESSION_THROUGHPUT=$(echo "scale=6; $INPUT_SIZE_MB / $DECOMPRESSION_DURATION" | bc)

echo "{{ job_name }},{{ compressor_name }},$COMPRESSION_DURATION,$COMPRESSION_THROUGHPUT,$DECOMPRESSION_DURATION,$DECOMPRESSION_THROUGHPUT,$RATIO" >> "{{ metrics_csv_path }}"

conda deactivate
