import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

jumlah_data = 100 
y = np.array([i * 0.1 + np.random.randn() for i in range (jumlah_data)])
x = np.array([i * 0.1 for i in range (jumlah_data) ])

def regresion_linier (x,gradien) :
    y = gradien * x
    return y 

x_prediksi = np.array([0,10])
m_awal = 5
y_prediksi = regresion_linier(x_prediksi,m_awal)

m_prediction = m_awal
m_list_prediksi = []
y_list_prediksi = []
x_list_prediksi = []
learning_rate = 0.1
for i in range (1,jumlah_data) :
    y_prediksi = regresion_linier(x[i],m_prediction)
    y_actual = y[i] 
    error = y_actual - y_prediksi
    delta_m = learning_rate * error / x[i]
    m_prediction = m_prediction + delta_m
    m_list_prediksi.append(m_prediction)
    y_list_prediksi.append(y_prediksi)
    x_list_prediksi.append(x[i])

fig = plt.figure(figsize=(4,4))
line, = plt.plot([],[],'r')
def animate (frame_num) :
    x = [0 , x_list_prediksi[frame_num]]
    y = [0, y_list_prediksi[frame_num]]
    line.set_data(x,y)
    return line
plt.scatter(x,y)
plt.axis([0,10,0,10])
anim =FuncAnimation(fig,animate,frames=jumlah_data-1,interval = 100,repeat=False)
plt.show()