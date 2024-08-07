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

berkasData = currentdir +'\\bab_06_11_dataMalaria.csv'
berkasSimpan = currentdir +'\\bab_06_11_malaria.pdf'
# judulDiagram = 'Penemuan Kasus Malaria\nTahun 2021'
sumbuX = 'Jumlah'
sumbuY = 'Puskesmas/ Kabupaten'
tickerSumbuX = np.arange(0,11,5)

# read data file
colnames = ['puskesmas','L','P','LP']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
puskesmas = data.puskesmas.tolist()
bar1 = data.L.tolist()
bar2 = data.P.tolist()
bar3 = data.LP.tolist()

ind = np.arange(len(puskesmas))  # the x locations for the groups
width = 0.2       # the width of the bars
widthDL = 0.5      # spacing for data labels

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='royalblue', label = 'L')
rects2 = ax.barh(ind + width, bar2, width, color='orangered', label = 'P')
rects3 = ax.barh(ind + 2*width, bar3, width, color='yellowgreen', label = 'L+P')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
# yticks can be set to auto
ax.set_xticks(np.arange(0,16,5)) 
ax.set_xlabel(sumbuY)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}".format(x)))

ax.set_yticks(ind+width)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in puskesmas ]))
ax.invert_yaxis()
ax.set_ylabel(sumbuY)

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

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
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
plt.savefig(berkasSimpan)
plt.close(pyrfig)
# plt.show()