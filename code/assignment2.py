#!/usr/bin/env python3
from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt

def rho(x, l, alfa, maxv):
    ft = lambda t: t*truncpareto.pdf(t,alfa,maxv)
    integral= quad(ft, 1, x)
    return integral[0]*l

fig, ax = plt.subplots(1, 1)
alfa = 1.4
maxv = 10000
x = np.linspace(1,20,100)
ax.plot(x, truncpareto.pdf(x, alfa, maxv), 'r-', lw=2, alpha=0.6, label='truncpareto pdf')
plt.show()

# mu = 3.14... and rho = 0.7

print(truncpareto.mean(alfa, maxv))
