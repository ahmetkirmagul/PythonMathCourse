import matplotlib.pyplot as plt

plt.axis([0,80,50.13,54.05])

x= [0,10,20,30,40,50,60,70,80]
y= [50,51.18, 50.43, 50.13, 50.70, 51.88, 51.02, 53.62, 54.05]

#for i in range(0,len(x)):
    #plt.plot(x[i],y[i],"s", label="t%s" %(i))#o = circle

plt.plot(x,y,"o-", label="Veri Grafiği")

plt.xticks(range(0,81,5))
plt.yticks(range(45,60))


plt.grid()#ızgara
plt.legend()#table that shows labels

plt.show()
