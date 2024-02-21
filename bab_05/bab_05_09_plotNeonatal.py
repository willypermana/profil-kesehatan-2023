import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
# locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')
locale.setlocale(locale.LC_ALL, 'Indonesian_indonesia.1252')

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

berkasData = currentdir +'\\bab_05_09_dataPlotNeonatal.csv'
berkasSimpan = currentdir +'\\bab_05_09_plotNeonatal.pdf'
# judulDiagram = 'Jumlah Kematian Neonatal\nTahun 2021'
sumbuX = 'Tahun'
sumbuY = 'per 1.000 kelahiran'
tickerSumbuY = np.arange(0,21,5)

# read data file
colnames = ['tahun','aknL', 'aknP', 'aknLP']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
tahun = data.tahun.tolist()
dataL = data.aknL.tolist()
dataP = data.aknP.tolist()
dataLP = data.aknLP.tolist()
 
# setting up x locations for the groups and width of the bars
ind = np.arange(len(tahun))
width = 0.25

# make plots
fig, ax = plt.subplots()
garis1 = ax.plot(ind, dataL, marker='.', color='royalblue', label='L')
garis2 = ax.plot(ind, dataP, marker='.', color='#cc0000', label='P')
garis3 = ax.plot(ind, dataLP, marker='.', color='yellowgreen', label='L+P')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
# yticks can be set to auto
ax.set_yticks(tickerSumbuY) 
ax.set_ylabel(sumbuY)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: '{:n}'.format(y)))

ax.set_xticks(ind)
ax.set_xticklabels(list(tahun), fontsize='small', ha='center')
ax.set_xlabel(sumbuX)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)

# make labels for plots
for i, txt in enumerate(dataL):
		ax.annotate(txt, xy=(ind[i]-0.3,dataL[i]-0.3), color='royalblue')
for i, txt in enumerate(dataP):
		ax.annotate(txt, xy=(ind[i]-0.1,dataP[i]+0.3), color='#cc0000')
for i, txt in enumerate(dataLP):
		ax.annotate(txt, xy=(ind[i]+0.1,dataLP[i]),  color='darkgreen')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
plt.savefig(berkasSimpan)
plt.close(pyrfig)
# plt.show()