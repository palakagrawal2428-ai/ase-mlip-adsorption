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

# ASE MLIP Adsorption

Study of oxygen adsorption on an Au(111) gold surface using the ASE (Atomic Simulation Environment) library in Python.

## What it does
- Calculates the adsorption energy of oxygen at 4 different sites on Au(111)
- Computes thermochemistry using vibrational analysis
- Compares the EMT calculator with the MACE machine-learning potential (mace_mp, small model)

## Result
The fcc site was the most stable adsorption site in both methods.

## Tech Used
Python, ASE, MACE
