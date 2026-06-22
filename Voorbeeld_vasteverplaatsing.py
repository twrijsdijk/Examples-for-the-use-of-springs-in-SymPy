import os
import sys

path_to_fork = os.path.abspath('C:\\Users\\twrij\\GitHub\\sympy_clone')
sys.path.insert(0, path_to_fork)

from sympy.physics.continuum_mechanics import Beam
from sympy import symbols

#Omschrijving van de balk
r0,r6 = symbols(['r0', 'r6'])
b = Beam(6, 5000, 10)
b.apply_load(r0, 0, -1)
b.apply_load(r6, 6, -1)
b.apply_load(-250, 3, -1)
b.bc_deflection = [(0,0.02), (6,0)]

#berekeningen
b.solve_for_reaction_loads(r0, r6)
print('belasting', b.load)
print('Dwarskrachten', b.shear_force())
print('Reactiekrachten', b.reaction_loads)
print('Moment',b.bending_moment())
print('Hoeverdraaiing',b.slope())
print('Doorbuiging',b.deflection())

#plots
axes = b.plot_loading_results()