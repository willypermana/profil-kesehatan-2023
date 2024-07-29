import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

berkasData = currentdir +'\\bab_05_03a_dataPlotK1K4SalinNifas.csv'
berkasSimpan = currentdir +'\\bab_05_03a_plotK1K4.pdf'
# judulDiagram = 'Capaian K1 dan K4\nTahun 2021'
sumbuX = 'Tahun'
sumbuY = 'Cakupan'
tickerSumbuY = np.arange(0,110,20)

# read data file
colnames = ['tahun','K1','K4','Salin','Nifas']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
tahun = data.tahun.tolist()
dataK1 = data.K1.tolist()
dataK4 = data.K4.tolist()
dataSalin = data.Salin.tolist()
dataNifas = data.Nifas.tolist()

ind = np.arange(len(tahun))  # the x locations for the groups
width = 0.25       # the width of the bars

# make bars
fig, ax = plt.subplots()
garis1 = ax.plot(ind, dataK1, marker='.', color='royalblue', label='K1')
garis2 = ax.plot(ind, dataK4, marker='.', color='#cc0000', label='K4')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_yticks(tickerSumbuY)
ax.set_ylabel(sumbuY)
formatter = FuncFormatter(lambda y, pos: '{:n}%'.format(y))
ax.yaxis.set_major_formatter(formatter)

ax.set_xticks(ind)
ax.set_xticklabels(list(tahun), ha='center')
ax.set_xlabel(sumbuX)

ax.tick_params(axis='both', which='major', labelsize='small')
#ax.grid(axis='x',ls='dashed')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

#make labels for plots
for i, txt in enumerate(dataK1):
		ax.annotate('{:n}'.format(txt), (ind[i],dataK1[i]), xytext=(0,5), textcoords='offset points', fontsize='x-small', color='royalblue')
for i, txt in enumerate(dataK4):
		ax.annotate('{:n}'.format(txt), (ind[i],dataK4[i]), xytext=(0,-10), textcoords='offset points', fontsize='x-small', color='#cc0000')


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