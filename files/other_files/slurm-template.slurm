#!/bin/bash

#SBATCH --job-name=aja.test
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --cpus-per-task=32
#SBATCH --time=00:05:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
# #SBATCH --mail-type=ALL
# #SBATCH --mail-user=aja@uark.edu

export OMP_NUM_THREADS=32

module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1

cd $SLURM_SUBMIT_DIR

# job command here
cat letters.txt
cat cowboy_carter.txt > out
cat andy.txt

