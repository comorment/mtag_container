#!/bin/sh
#SBATCH --job-name=$JOBNAME
#SBATCH --account=$ACCOUNT
#SBATCH --open-mode=truncate
#SBATCH --output=${JOBNAME}.out
#SBATCH --error=${JOBNAME}.err
#SBATCH --time=$WALLTIME
#SBATCH --cpus-per-task=$CPUS_PER_TASK
#SBATCH --mem-per-cpu=$MEM_PER_CPU

module load $SINGULARITY_MODULE

export ROOTDIR="$(dirname ${PWD})"
export SINGULARITY_BIND="$ROOTDIR/reference:/REF:ro"  # mount reference directory as /REF
export SIF=${ROOTDIR}/singularity
export PYTHON="singularity exec --home=$PWD:/home --cleanenv $SIF/mtag_container.sif python"

# Run some commands
$PYTHON --version  # print version
$PYTHON -c "print('hello mtag_container')"  # run a command
$PYTHON hello_world.py # run a script