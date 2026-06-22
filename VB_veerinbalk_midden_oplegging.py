import os
import sys

path_to_fork = os.path.abspath('C:\\Users\\twrij\\GitHub\\sympy_clone')
sys.path.insert(0, path_to_fork)

from sympy.physics.continuum_mechanics import Beam
from sympy import symbols

#Omschrijving van de balk
b = Beam(6, 500, 10)
r0 = b.apply_support(0,'pin')
r3 = b.apply_support(3,'pin')
r6 = b.apply_support(6,'pin')
b.apply_load(-100, 5, -1)
b.apply_load(-100, 2, -1)
b.apply_spring(3, 1000)

#berekeningen
b.solve_for_reaction_loads(r0, r3, r6)
print('belasting', b.load)
print('Dwarskrachten', b.shear_force())
print('Reactiekrachten', b.reaction_loads)
print('Moment',b.bending_moment())
print('Hoeverdraaiing',b.slope())
print('Doorbuiging',b.deflection())

#plots
axes = b.plot_loading_results()
d = b.draw()
d.show()