from variables import caso_1, caso_2, caso_3, gamma_agua, gamma_sturada, caso_escalado
from laplace_solver import laplace

laplace(caso_1, 'caso_1', 40)
laplace(caso_2, 'caso_2', 40)
laplace(caso_3, 'caso_3', 40)

#laplace(caso_escalado, 'caso_escalado', 40)