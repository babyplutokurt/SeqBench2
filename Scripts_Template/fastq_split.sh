#!/bin/sh
#PBS -l walltime={{ walltime }}
#PBS -N {{ job_name }}
#PBS -l nodes={{ nodes }}:ppn={{ ppn }}
#PBS -M {{ email }}
#PBS -o {{ output_log }}
#PBS -e {{ error_log }}

{{ dependency_line }}

cd $PBS_O_WORKDIR

source {{ conda_path }} compression

python -c "import sys
sys.path.append('{{ get_build_pre_processing_cpp_path }}')
import fastq_processor; fastq_processor.process_fastq('{{ input_path }}', '{{ output_bases_id_path }}', '{{ output_bases_path }}', '{{ output_quality_id_path }}', '{{ output_quality_path }}')"

conda deactivate