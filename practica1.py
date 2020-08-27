import sys 
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import CosSignal  
from thinkdsp import decorate

#Módulo para mostrar gráficas
import matplotlib.pyplot as plt

#Crear señal senoidal
seno = SinSignal(freq=400, amp=0.7, offset=0)
coseno = CosSignal(freq=800, amp=1.1, offset=0)

#Crear gráfica en memoria
seno.plot()
decorate(xlabel='Tiempo (s)')
decorate(ylabel='Amplitud')

coseno.plot()

plt.show()