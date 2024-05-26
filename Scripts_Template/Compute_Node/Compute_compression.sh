#!/bin/sh
#PBS -l walltime={{ walltime }}
#PBS -N {{ job_name }}
#PBS -l nodes={{ nodes }}:ppn={{ ppn }}
#PBS -M {{ email }}
#PBS -o {{ output_log }}
#PBS -e {{ error_log }}

{{ dependency_line }}

# change to directory where 'qsub' was called
cd $PBS_O_WORKDIR

source {{ conda_path }} compression

# Function to get current time in seconds with nanoseconds precision
get_time() {
    echo $(date +%s.%N)
}

BINARY_LENGTH=$(($(stat -c %s "{{ binary_input_file }}") / 4))

# Run compression and capture metrics
START_TIME=$(get_time)
{{ reference_command }}
{{ compression_command }}
END_TIME=$(get_time)
COMPRESSION_DURATION=$(echo "$END_TIME - $START_TIME" | bc)

INPUT_SIZE=$(stat -c %s "{{ input_path }}")
OUTPUT_SIZE=$(stat -c %s "{{ compressed_output_path }}")
RATIO=$(echo "scale=6; $INPUT_SIZE / $OUTPUT_SIZE" | bc)

sleep 20

# Run decompression and capture metrics
START_TIME=$(get_time)
{{ decompression_command }}
END_TIME=$(get_time)
DECOMPRESSION_DURATION=$(echo "$END_TIME - $START_TIME" | bc)

echo "{{ job_name }},{{ compressor_name }},$COMPRESSION_DURATION,$DECOMPRESSION_DURATION,$RATIO" >> "{{ metrics_csv_path }}"

conda deactivate
