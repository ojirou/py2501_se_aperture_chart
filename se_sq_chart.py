import matplotlib.pyplot as plt
import numpy as np
import subprocess
try:
    a0 = np.genfromtxt('data_chart\\250113se_sq_chart.csv', delimiter=",", skip_header=1)
except Exception as e:
    print(f"Error loading data: {e}")
    raise
fig, ax = plt.subplots(figsize=(5.5, 3.5))
ax.plot(a0[:, 0], a0[:, 1], color="black", lw=1, ls='-', marker='o', markersize=0, label=r'1MHz')
ax.plot(a0[:, 0], a0[:, 2], color="red", lw=1, ls='-', marker='o', markersize=0, label=r'10MHz')
ax.plot(a0[:, 0], a0[:, 3], color="green", lw=1, ls='-', marker='o', markersize=0, label=r'100MHz')
ax.plot(a0[:, 0], a0[:, 4], color="blue", lw=1, ls='-', marker='o', markersize=0, label=r'1000MHz')
ax.set_xscale('log')
ax.set_yscale('linear')
ax.set_xlim([0.001, 1])
ax.set_ylim([0, 120])
ax.set_title(r'Shield Effect of a Slot Aperture')
ax.set_xlabel(r'Aperture Length [m]', fontsize=11)
ax.set_ylabel(r'Shield Effect [dB]', fontsize=11)
ax.legend(loc='upper right')
ax.grid(ls=':')
fig.subplots_adjust(left=0.13, right=0.95, bottom=0.15, top=0.92)
PdfFile = 'data_chart\\250113se_sq_chart.pdf'
# fig.savefig(PdfFile)
# subprocess.Popen(['start', PdfFile], shell=True)