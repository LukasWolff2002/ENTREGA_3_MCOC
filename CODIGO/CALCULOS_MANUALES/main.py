from variables import caso_1, caso_2, caso_3
import matplotlib.pyplot as plt

#En primer lugar se haran los modelo en A4
from grafico import graficar, graficar_lineas_con_pendientes

ax, pendientes, coordenadas = graficar(caso_1, 'caso_1', 50, 297)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"HOJAS_A4/caso_1.pdf", format='pdf', bbox_inches='tight', pad_inches=0)

ax, pendientes, corrdenadas = graficar(caso_2, 'caso_2', 50, 297)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"HOJAS_A4/caso_2.pdf", format='pdf', bbox_inches='tight', pad_inches=0)

ax, pendientes, corrdenadas = graficar(caso_3, 'caso_3', 50, 297)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"HOJAS_A4/caso_3.pdf", format='pdf', bbox_inches='tight', pad_inches=0)

#En segundo lugar desarollo los modelos para el informe

ax, pendientes, coordenadas = graficar(caso_1, 'caso_1', 0, 150)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"INFORME/GRAFICOS/caso_1.jpg", format='jpg', bbox_inches='tight', pad_inches=0)

ax, pendientes, corrdenadas = graficar(caso_2, 'caso_2', 0, 150)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"INFORME/GRAFICOS/caso_2.jpg", format='jpg', bbox_inches='tight', pad_inches=0)

ax, pendientes, corrdenadas = graficar(caso_3, 'caso_3', 0, 150)
graficar_lineas_con_pendientes(ax, coordenadas, pendientes, color='green', grosor=1)
plt.savefig(f"INFORME/GRAFICOS/caso_3.jpg", format='jpg', bbox_inches='tight', pad_inches=0)

#Calculo las presiones totales
from presion_ataguia_total import presiones_ataguia

presiones_ataguia(caso_1, 'caso_1', 0, '_presion_ataguia_total')
presiones_ataguia(caso_2, 'caso_2', 0, '_presion_ataguia_total')
presiones_ataguia(caso_3, 'caso_3', 0, '_presion_ataguia_total')



#Ahora calculo y grafico las presiones netas sobre la ataguia
from presion_ataguia_neta import presiones_ataguia
print('Calculando presiones sobre la ataguia')
print('Caso 1')
presiones_ataguia(caso_1, 'caso_1', 0, '_presion_ataguia_neta')
print('')
print('Caso 2')
presiones_ataguia(caso_2, 'caso_2', 0, '_presion_ataguia_neta')
print('')
print('Caso 3')
presiones_ataguia(caso_3, 'caso_3', 0, '_presion_ataguia_neta')
print('')

#Finalmente grafico el centroide
from presion_ataguia_centroide import presiones_ataguia
print('Calculando centroide de las presiones sobre la ataguia')
print('Caso 1')
presiones_ataguia(caso_1, 'caso_1', 0, '_centroide_y')
print('')
print('Caso 2')
presiones_ataguia(caso_2, 'caso_2', 0, '_centroide_y')
print('')
print('Caso 3')
presiones_ataguia(caso_3, 'caso_3', 0, '_centroide_y')
print('')

#Ahora calculo las presiones de poros con mapa de calor
from mapa_calor import presiones_poros

presiones_poros(caso_1, 'caso_1', 0, '_presion_poros')
presiones_poros(caso_2, 'caso_2', 0, '_presion_poros')
presiones_poros(caso_3, 'caso_3', 0, '_presion_poros')

#Calculo el maximo gradiente hidraulico
from max_gradiente_hidraulico import max_gradiente_hidraulico
print('Calculando maximo gradiente hidraulico')
print('Caso 1')
max_gradiente_hidraulico(caso_1, 'caso_1')
print('')
print('Caso 2')
max_gradiente_hidraulico(caso_2, 'caso_2')
print('')
print('Caso 3')
max_gradiente_hidraulico(caso_3, 'caso_3')

#Calculo el caudal de infiltracion
from infiltracion import infiltracion
print('Calculando caudal de infiltracion')
print('Caso 1')
infiltracion(caso_1, 'caso_1')
print('')
print('Caso 2')
infiltracion(caso_2, 'caso_2')
print('')
print('Caso 3')
infiltracion(caso_3, 'caso_3')


