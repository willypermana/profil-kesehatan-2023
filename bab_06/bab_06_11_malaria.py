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

import konstan
berkasData = konstan.direktori6+'bab_06_15_dataMalaria.csv'
judulDiagram = 'Penemuan Kasus Malaria'
sumbuY = 'Jumlah'
berkasSimpan = konstan.direktori6+'bab_07_15_malaria.pdf'

# read data file
colnames = ['kecamatan','L','P','LP']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.L.tolist()
bar2 = data.P.tolist()
bar3 = data.LP.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.2       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='royalblue', label = 'L')
rects2 = ax.barh(ind + width, bar2, width, color='orangered', label = 'P')
rects3 = ax.barh(ind + 2*width, bar3, width, color='yellowgreen', label = 'L+P')

# add some text for labels, title and axes ticks
ax.set_title(judulDiagram)
# yticks can be set to auto
ax.set_xticks(np.arange(0,16,5)) 
ax.set_xlabel(sumbuY)
formatter = FuncFormatter(lambda y, pos: "%d" % (y))
ax.xaxis.set_major_formatter(formatter)

ax.set_yticks(ind + width)
ax.invert_yaxis()
wrapKecamatan = [ '\n'.join(wrap(l, 10)) for l in kecamatan ]
ax.set_yticklabels(list(wrapKecamatan), fontsize='small')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)

# make labels for bars
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v+0.5, i+0.3, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar3):
    ax.text(v+0.5, i+0.6, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')


# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
# fig.savefig(berkasSimpan, bbox_inches='tight')
# plt.close(pyrfig)
plt.show()