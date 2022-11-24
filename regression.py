"""
Created on Sat Nov 19 15:27:43 2022

@author: Killrahan
"""
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
corr = True #Active le modèle de correction prenant en compte le rayon des tubes

def linear(x,a): #fct dont on cherche a et b pour la régression linéaire. 
    return a*x 

if corr == True: 
    R = 0.7
else:
    R = 0

lTube = [(4.9 + 0.6*R)*10**(-2), (7.5 + 0.6*R)*10**(-2), (10 + 0.6*R)*10**(-2), (14.7 + 0.6*R)*10**(-2), (20.3 + 0.6*R)*10**(-2), (24.7 + 0.6*R)*10**(-2), (30.2 + 0.6*R)*10**(-2), (34.2 + 0.6*R)*10**(-2)] # [m]
erreurLTube = [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001] 
invLTube = [1/lTube[0], 1/lTube[1], 1/lTube[2], 1/lTube[3], 1/lTube[4], 1/lTube[5], 1/lTube[6], 1/lTube[7]]
erreurInvLTube = [0.001*invLTube[0]**2, 0.001*invLTube[1]**2, 0.001*invLTube[2]**2, 0.001*invLTube[3]**2, 0.001*invLTube[4]**2, 0.001*invLTube[5]**2, 0.001*invLTube[6]**2, 0.001*invLTube[7]**2] #Taylor
frequence = [1450, 1020, 760, 560, 407.5, 340, 271.5, 240] #[Hz]
erreurFrequence = [100, 125, 55, 40, 37.5, 60, 38.5, 40]

plt.plot(invLTube, frequence, "bx", label = 'mesures effectuées')
popt, pcov = curve_fit(linear, invLTube, frequence, sigma = erreurFrequence)
print(popt) #Nous donne les valeurs de a et b trouvées par la régression linéaire. Dans notre cas a = 71.11781122  et b = 49.19614534
xFit2 = np.linspace(0,25,1000) 
plt.grid()

#matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, elinewidth=None, capsize=None, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, *, data=None, **kwargs)
plt.title("fréquence fondamentale (f) en fonction de l'inverse de la longueur de chaque tube [Hz]")
plt.errorbar(invLTube, frequence, yerr = erreurFrequence , xerr = erreurInvLTube,  fmt = 'bx', ecolor = 'black', capsize = 2, label = 'erreur associée à la mesure', barsabove = True)

plt.xlabel('inverse de la longueur de chaque tube [1/m]') 
plt.ylabel('fréquence fondamentale [Hz]')
plt.plot(xFit2, linear(xFit2, *popt), 'r', label = 'régression linéaire 77.41401352x')

plt.legend(loc="upper left")
plt.show()
""" 

la vitesse du son est obtenue en multipliant la pente de la droite par 4 au vu de la formule f1 = vSon/4L puisque notre graphique représente f = 1/L

"""
vSon = 4*popt[0]
print(vSon)





