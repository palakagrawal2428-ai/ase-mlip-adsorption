# ASE + MLIP: Oxygen Adsorption on Au(111)

Practice project using the Atomic Simulation Environment (ASE).

## What it does
- Builds a gold Au(111) surface and places an oxygen atom on 4 sites (ontop, bridge, fcc, hcp)
- Optimizes the geometry and computes adsorption energy
- Compares a simple calculator (EMT) with a machine-learned potential (MACE-MP)

## Result
The fcc hollow site came out as the most stable site.

## Tools
Python, ASE, MACE (mace-torch)

## How to run
pip install ase mace-torch
python test1.py
