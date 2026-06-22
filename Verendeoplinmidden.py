import os
import sys

path_to_fork = os.path.abspath('C:\\Users\\twrij\\GitHub\\sympy_clone')
sys.path.insert(0, path_to_fork)

from sympy.physics.continuum_mechanics import Beam
from sympy import symbols

#Omschrijving van de balk
R_3, R_0, R_6 = symbols(['R_3', 'R_0', 'R_6'])
b = Beam(6, 200, 20)
#belastingen
b.apply_load(R_0,0,-1)
b.apply_load(R_6,6,-1)
b.apply_load(R_3,3,-1)
b.apply_load(-250,3,-1)

b.bc_deflection = [(3,-R_3 / 1000), (0,0), (6,0)]
#b.apply_rotation_spring(6, 100)
b.solve_for_reaction_loads(R_0, R_3, R_6)
#berekeningen
print('belasting', b.load)
print('Dwarskrachten', b.shear_force())
print('Reactiekrachten', b.reaction_loads)
print('Moment',b.bending_moment())
print('Hoeverdraaiing',b.slope())
print('Doorbuiging',b.deflection())
axes = b.plot_deflection()
