import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

#Henter verdi fra filer
norge = pd.read_csv("https://raw.githubusercontent.com/andreasdh/Programmering-og-modellering/master/docs/Datafiler/CO2_Norge.txt")
india = pd.read_csv("https://raw.githubusercontent.com/andreasdh/Programmering-og-modellering/refs/heads/master/docs/Datafiler/CO2_India.txt")

#Med bæreevne
U0 = 0.01
a = 0.055
a1 = -0.05
t0 = 1825
t_slutt = 2100
dt = 1
N = int((t_slutt-t0)/dt)
b = 10
k1 = 2015 - t0
k2 = t_slutt - 2015
t = np.zeros(k1+1)
U = np.zeros(k1+1)
t1 = np.zeros(k2+1)
U1 = np.zeros(k2+1)
t[0] = t0
U[0] = U0

t1[0] = 2018
U1[0] = U0

for i in range(k1): 
    U[i+1] = U[i] + a*U[i]*(1-(U[i]/b)) #Dette er en diskret modell (Differenslikning)
    t[i+1] = t[i] + dt

for i in range(k2):
    U1[i+1] = U1[i] + a1*U1[i] #Dette er en diskret modell (Differenslikning)
    t1[i+1] = t1[i] + dt


plt.scatter(t,U, label = "Simulert utslipp")
plt.scatter(t1,U1, label = "Simulert utslipp")
plt.scatter(norge['year'],norge['CO2'], label = "CO_2/innbygger Norge")
plt.scatter(india['year'],india['CO2'], label = "CO_2/innbygger India")
plt.title('Utslipp CO_2 per innbygger')
plt.legend()
plt.xlabel("Tid i år")
plt.ylabel("Antall tonn $CO_2$")
plt.grid()
plt.show()

#print(f"Utslippet i 2100 kommer til å blir: {U[N]} tonn CO_2, mens utslippet i 2018 var: {U[N-82]} tonn CO_2")