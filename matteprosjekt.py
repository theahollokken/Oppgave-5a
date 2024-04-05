#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:40:00 2024

@author: mathildelouisedreyersorbu
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Definerer konstantene for bølgefunksjonen
g = 9.81  # tyngdeakselerasjonen i m/s^2

# Velger en representativ verdi for dybden h
h = 10  # dypde i meter (dette er et eksempel, den faktiske verdien må gis)

# Lager en grid av x og t verdier
x = np.linspace(0, 20, 400)  # x-verdier over en strekning
t_values = np.linspace(1, 5, 3)  # tidsverdier

# Plotter bølgefunksjonen for flere tidspunkter
for t in t_values:
    zeta = np.cos(x - np.sqrt(g*h)*t)
    plt.plot(x, zeta, label=f't={t}')

plt.xlabel('x (posisjon)')
plt.ylabel('zeta (bølgehøyde)')
plt.title('Bølgefunksjonen zeta(x, t) over tid')
plt.legend()
plt.grid(True)
plt.show()
