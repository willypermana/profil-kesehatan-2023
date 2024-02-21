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

berkasData = currentdir +'\\bab_05_14a_dataPlotKN1KN3.csv'
berkasSimpan = currentdir +'\\bab_05_14a_plotKN1KN3.pdf'
# judulDiagram = 'Capaian KN1 dan KN3\nTahun 2016-2021'
sumbuX = 'Tahun'
sumbuY = 'Cakupan'
tickerSumbuY = np.arange(0,110,25)

# read data file
colnames = ['tahun','KN1','KN3']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
tahun = data.tahun.tolist()
dataGaris1 = data.KN1.tolist()
dataGaris2 = data.KN3.tolist()

ind = np.arange(len(tahun))  # the x locations for the groups
width = 0.25       # the width of the bars

# make bars
fig, ax = plt.subplots()
garis1 = ax.plot(ind, dataGaris1, marker='.', color='royalblue', label='KN1')
garis2 = ax.plot(ind, dataGaris2, marker='.', color='#cc0000', label='KN3')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_yticks(tickerSumbuY)
ax.set_xlabel(sumbuX)
ax.set_ylabel(sumbuY)
formatter = FuncFormatter(lambda y, pos: '{:.0f}%'.format(y))
ax.yaxis.set_major_formatter(formatter)

ax.set_xticks(ind)
ax.set_xticklabels(list(tahun), ha='center')

ax.tick_params(axis='both', which='major', labelsize='small')
#ax.grid(axis='x',ls='dashed')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

#make labels for plots
for i, txt in enumerate(dataGaris1):
		ax.annotate('{:n}'.format(txt), (ind[i],dataGaris2[i]), xytext=(0,5), textcoords='offset points', fontsize='x-small', color='royalblue')
for i, txt in enumerate(dataGaris2):
		ax.annotate('{:n}'.format(txt), (ind[i],dataGaris2[i]), xytext=(0,-10), textcoords='offset points', fontsize='x-small', color='#cc0000')


# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(7)
pyrfig.set_figheight(5)
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
plt.savefig(berkasSimpan)
plt.close(pyrfig)
# plt.show()