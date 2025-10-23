import matplotlib.pyplot as plt
import numpy as np

D_cm = [80, 70, 60, 50, 40, 30, 20, 10]
V_avg_cm_s = [51.18, 50.43, 50.13, 50.70, 51.88, 51.02, 53.62, 54.05]

a = -0.0475
b = 53.76

D_line = np.linspace(0, 80, 100)

V_avg_line = a * D_line + b

plt.figure(figsize=(10, 6),facecolor="blue")

plt.scatter(D_cm, V_avg_cm_s, label='Deneysel Veriler', color='blue', zorder=5)

plt.plot(D_line, V_avg_line, label=f'Regresyon Doğrusu: Ortalama Hız = {a} X D + {b}', color='pink')

plt.xlabel('Mesafe (D) [cm]')
plt.ylabel('Ortalama Hız (Ortalama hız) [cm/s]')
plt.title('Ortalama Hız vs. Mesafe Grafiği ve Ekstrapolasyon')
plt.grid(True)
plt.legend()

plt.scatter(0, b, color='green', zorder=10, s=100, label=f'Anlık Hız (D=0): {b:.2f} cm/s')
plt.legend()

plt.show()