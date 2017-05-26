import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("Canal_ionico.txt")
x=datos[:,0]
y=datos[:,1]

datos1=np.loadtxt("Canal_ionico1.txt")
x1=datos1[:,0]
y1=datos1[:,1]

circulo_datos=np.genfromtxt("radios.txt",skip_footer=000)
xc=circulo_datos[:,0]
yc=circulo_datos[:,1]
rc=circulo_datos[:,2]

circulo_datos1=np.loadtxt("radios.txt", skiprows=3000)
xc1=circulo_datos1[:,0]
yc1=circulo_datos1[:,1]
rc1=circulo_datos1[:,2]

r_max=0
pos=0
for i in range(len(rc)):
	if (rc[i]>r_max):
		r_max=rc[i]
		pos=i


#print(xc[pos],yc[pos])

xx=xc[pos]
yy=yc[pos]
rr=rc[pos]
fig, ax=plt.subplots()
plt.scatter(x,y)
circle1=plt.Circle((xc[pos],yc[pos]),rc[pos],fill=False, color="red")
ax.add_artist(circle1)
ax.set_aspect('equal','datalim')
plt.title("Radio ionico")
plt.savefig("Radio_ionico.jpg")
plt.close()



r_max1=0
pos1=0
for i in range(len(rc1)):
	if (rc1[i]>r_max1):
		r_max1=rc1[i]
		pos1=i


#print(xc1[pos1],yc1[pos1])

xx1=xc1[pos]
yy1=yc1[pos]
rr1=rc1[pos]
fig, ax=plt.subplots()
plt.scatter(x1,y1)
circle11=plt.Circle((xc1[pos1],yc1[pos1]),rc1[pos1],fill=False, color="red")
ax.add_artist(circle11)
ax.set_aspect('equal','datalim')
plt.title("Radio Ionico 1")
plt.savefig("Radio_ion1.jpg")
plt.close()

#------------ HISTOGRAMAS

histograma=plt.hist([xc,yc],label=["x","y"])
plt.legend()
plt.title("Histograma 1")
plt.savefig("hist1.jpg")
plt.close()

histograma1=plt.hist([xc1,yc1],label=["x","y"])
plt.legend()
plt.title("Histograma 2")
plt.savefig("hist2.jpg")
plt.close()


