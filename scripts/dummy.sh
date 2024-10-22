#!/bin/bash
#SBATCH -p performance
#SBATCH -t 0-01:00:00
#SBATCH --gpus 1
#SBATCH -J dummy_model
#SBATCH -o dummy_out.log
#SBATCH -e dummy_err.log

# Check if sweep ID is provided as an argument
if [ -z "$1" ]; then
    # No sweep ID passed, run the initial command
    .venv/bin/python scripts/dummy.py
else
    # Sweep ID passed, add agent to existing sweep
    .venv/bin/python scripts/dummy.py --sweep_id "$1"
fi
