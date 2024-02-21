import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')
plt.rcParams['pdf.fonttype'] = 42

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# data seluruh kunjungan per FKTP
berkasData = currentdir +'\\bab_02_1_dataKunjunganFaskes.csv'
berkasSimpan = currentdir +'\\bab_02_1_kunjunganFaskes.pdf'
# judulDiagram = 'Kunjungan Pasien di Fasilitas Kesehatan'
tickerSumbuX = np.arange(0,150100,50000)
sumbuX = 'Jumlah Kunjungan'
sumbuY = 'Jenis Fasyankes'
labelBar1 = 'Laki-laki'
labelBar2 = 'Perempuan'
labelBar3 = 'Laki-laki + Perempuan'

# read data file
colnames = ['faskes','L','P','LP']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
faskes = data.faskes.tolist()
bar1 = data.L.tolist()
bar2 = data.P.tolist()
bar3 = data.LP.tolist()

ind = np.arange(len(faskes))  # the x locations for the groups
width = 0.25       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label=labelBar1)
rects2 = ax.barh(ind + width, bar2, width, color='tomato', label=labelBar2)
rects3 = ax.barh(ind + width + width, bar3, width, color='yellowgreen', label = labelBar3)

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.set_xlabel(sumbuX)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}".format(x)))

ax.set_ylabel(sumbuY)
ax.set_yticks(ind+0.25)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in faskes ]))
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
#ax.grid(axis='y',ls='dashed')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box below chart
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)

# horizontal bar labels. remember to figure out converting to function
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, "{:n}".format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v+0.6, i+0.25, "{:n}".format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar3):
    ax.text(v+0.6, i+0.5, "{:n}".format(v), ha='left', va='center', fontsize='x-small')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
plt.savefig(berkasSimpan, metadata={"Author": "Willy"})
plt.close(pyrfig)
# plt.show()
# bbox tight remove whitespace, but makes the documents size inconsistent
# fig.savefig(berkasSimpan, bbox_inches='tight')