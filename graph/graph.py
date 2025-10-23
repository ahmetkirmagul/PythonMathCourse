import matplotlib.pyplot as plt

x = range(-20,21)

for xi in x:
    plt.plot([0,xi],[0,abs(xi)**(1/2)])

plt.show()