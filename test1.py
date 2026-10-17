from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from mace.calculators import mace_mp

# MACE calculator (EMT ki jagah)
calc = mace_mp(model="small", default_dtype="float64", device="cpu")

# Clean slab
clean = fcc111('Au', size=(3, 3, 3), vacuum=10.0)
clean.calc = calc
BFGS(clean, logfile=None).run(fmax=0.05)
e_clean = clean.get_potential_energy()

# Akela oxygen atom
o_atom = Atoms('O')
o_atom.calc = calc
e_o = o_atom.get_potential_energy()

# Alag-alag sites
results = {}
for site in ['ontop', 'bridge', 'fcc', 'hcp']:
    slab = fcc111('Au', size=(3, 3, 3), vacuum=10.0)
    add_adsorbate(slab, 'O', height=1.5, position=site)
    slab.calc = calc
    BFGS(slab, logfile=None).run(fmax=0.05)
    results[site] = slab.get_potential_energy() - e_clean - e_o

for site, e in results.items():
    print(f"{site:8s} adsorption energy = {e:.3f} eV")

print("Sabse stable site:", min(results, key=results.get))