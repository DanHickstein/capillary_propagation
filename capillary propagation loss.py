"""
danhickstein@gmail.com

This uses the equation from the bottom of the Fig. 7 caption on page 1797 of
Marcatili and Schmeltzer 1964:
https://doi.org/10.1002/j.1538-7305.1964.tb04108.x

dB_per_km = 1.85 lambda^2/a^3
"""

import numpy as np
import matplotlib.pyplot as plt

length = 10        # mm
wl_micron = 0.633  # um
radius_mm = 0.025  # mm, *radius* not diameter!
dB_per_km = 1.85 * wl_micron**2 / radius_mm**3

print('For radius of %.6f mm and wavelength of %.3f micron:'%(radius_mm, wl_micron))
print('dB per km: %.0f' % (dB_per_km))
print('dB per km: %.3f' % (dB_per_km*1e-3))
print('dB per mm: %.6f' % (dB_per_km*1e-6))

loss_dB = dB_per_km * 1e-6 * length

transmission = 10**(-loss_dB*0.1)
loss = 1 - transmission

print('dB loss over %.1f mm: %.2f' % (length, loss_dB))
print('Transmission over %.1f mm: %.2f percent' % (length, transmission*100))
print('Loss over %.1f mm: %.2f percent' % (length, loss*100))
