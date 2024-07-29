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

berkasData = currentdir +'\\bab_05_26_dataKesehatanSiswa.csv'
berkasSimpan = currentdir +'\\bab_05_26_kesehatanSiswa.pdf'
# judulDiagram = 'Pelayanan Kesehatan Peserta Didik\nTahun 2021'
sumbuX = 'Cakupan'
sumbuY = 'Kecamatan/ Kabupaten'
tickerSumbuX = np.arange(0,110,25)
labelRects1 = 'Kelas 1 SD/MI'
labelRects2 = 'Kelas 7 SMP/MTs'
labelRects3 = 'Kelas 10 SMA/MA'

# read data file
colnames = ['kecamatan','SD','SMP','SMA']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.SD.tolist()
bar2 = data.SMP.tolist()
bar3 = data.SMA.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.3       # the width of the bars
widthDL = 0.5      # spacing for data labels

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label=labelRects1)
rects2 = ax.barh(ind + width, bar2, width, color='orangered', label = labelRects2)
rects3 = ax.barh(ind + 2*width, bar3, width, color='yellowgreen', label = labelRects3)

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.set_xlabel(sumbuX)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}%".format(x)))

ax.set_yticks(ind+width)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in kecamatan ]))
ax.invert_yaxis()
ax.set_ylabel(sumbuY)

ax.tick_params(axis='both', which='major', labelsize='small')
# ax.tick_params(axis='y', length=0, which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)

# add data label
for i, v in enumerate(bar1):
    ax.text(v + widthDL, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v + widthDL, i + width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar3):
    ax.text(v + widthDL, i + 2*width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')

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