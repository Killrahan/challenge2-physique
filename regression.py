"""
Created on Sat Nov 19 15:27:43 2022

@author: Killrahan
"""
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def linear(x,a): #fct dont on cherche a
    return a*x 

lTube = [4.9*10**(-2), 7.5*10**(-2), 10*10**(-2), 14.7*10**(-2), 20.3*10**(-2), 24.7*10**(-2), 30.2*10**(-2), 34.2*10**(-2)] # [m]
erreurLTube = [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001] 
invLTube = [1/(4.9*10**(-2)), 1/(7.5*10**(-2)), 1/(10*10**(-2)), 1/(14.7*10**(-2)), 1/(20.3*10**(-2)), 1/(24.7*10**(-2)), 1/(30.2*10**(-2)), 1/(34.2*10**(-2))]
erreurInvLTube = [0.001*invLTube[0]**2, 0.001*invLTube[1]**2, 0.001*invLTube[2]**2, 0.001*invLTube[3]**2, 0.001*invLTube[4]**2, 0.001*invLTube[5]**2, 0.001*invLTube[6]**2, 0.001*invLTube[7]**2] #Taylor
frequence = [1450, 1020, 760, 560, 407.5, 340, 271.5, 240] #[Hz]
erreurFrequence = [100, 125, 55, 40, 37.5, 60, 38.5, 40]

plt.plot(invLTube, frequence, "bx", label = 'mesures effectuées')
popt, pcov = curve_fit(linear, invLTube, frequence, sigma = erreurFrequence)
print(popt) #Nous donne la valeur de a 
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

