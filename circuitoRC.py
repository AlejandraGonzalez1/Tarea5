import numpy as np 
import matplotlib.pyplot as plt


#Este ejercicio se realizo a partir del ejemplo del repositorio de metodo montecarlo MCMC https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipynb-----------------------------NO ES COPIA

data=np.loadtxt("CircuitoRC.txt")
tiempo=data[:,0]
q_exp=data[:,1]


def likelihood(q_exp,q_teo):
	chi2= (1.0/2.0)*sum((q_exp-q_teo)**2)/10000
	return np.exp(-chi2)

def funcion(v_0,tiempo,R,C):
	numero=-tiempo/R*C
	return v_0*C*(1.0-np.exp(numero))

#Listas para ir contando los pasos
step_R=np.empty((0))
step_C=np.empty((0))
step_lh=np.empty((0))

step_R=np.append(step_R, np.random.random())
step_C=np.append(step_C, np.random.random())

q_0=funcion(10,tiempo,step_R[0],step_C[0])
step_lh=np.append(step_lh,likelihood(q_exp,q_0))

iteraciones=2000

for i in range(iteraciones):
	R_paso=np.random.normal(step_R[i],0.1)
	C_paso=np.random.normal(step_C[i],0.1)

	q_0=funcion(10,tiempo,step_R[i],step_C[i])
	q_paso=funcion(10,tiempo,R_paso,C_paso)

	lh_paso=likelihood(q_exp,q_paso)
	lh_0=likelihood(q_exp,q_0)
    
	alpha = lh_0/lh_paso
	if(alpha>=1.0):
		step_R=np.append(step_R,R_paso)
		step_C=np.append(step_C,C_paso)
		step_lh=np.append(step_lh,lh_paso)
	else:
		beta = np.random.random()
		if(beta<=alpha):
			step_C = np.append(step_C,C_paso)
			step_R = np.append(step_R,R_paso)
			step_lh = np.append(step_lh, lh_paso)
		else:
			step_C = np.append(step_C,step_C[i])
			step_R = np.append(step_R,step_R[i])
			step_lh = np.append(step_lh, lh_0)

mejor_lk=np.argmax(step_lh)
mejor_C=step_C[mejor_lk]
mejor_R=step_R[mejor_lk]

#print(mejor_C)
#print(mejor_R)
mejor_Q=funcion(10,tiempo,mejor_R,mejor_C)

plt.scatter(tiempo,q_exp)
plt.plot(tiempo,mejor_Q)
plt.title("Datos experimentales")
plt.savefig("experimentales.jpg")
plt.close()

plt.hist([step_R,step_C],label=["R","C"])
plt.legend()
plt.savefig("histcircuitos.jpg")


