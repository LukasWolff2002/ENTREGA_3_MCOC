#Variables suelo
k = 5.8e-1 #cm/s

a1 = 0
b1 = 14.5 #cm
c1 = 15.5 #cm
a2 = 15 #cm
b2 = 2.5 #cm #no se observaba agua
c2 = 12.5 #cm
d = c2 - 12
caso_licuefaccion = {'a1': a1, 'a2': a2, 'b1': b1, 'c1': c1, 'b2': b2, 'c2': c2, 'd': d, 'k': k}

from grafico import graficar, graficar_lineas_con_pendientes
import matplotlib.pyplot as plt
ax, pendientes, coordenadas = graficar(caso_licuefaccion, 'caso_licuefaccion', 0, 150)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"caso_licuefaccion.jpg", format='jpg', bbox_inches='tight', pad_inches=0)

#Perfecto, calculemos ahora el mapa de calor
from mapa_calor import presiones_poros
presiones_poros(caso_licuefaccion, 'caso_licuefaccion', 0, '_presion_poros')
