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

berkasData = currentdir +'\\bab_05_06a_dataKB4TALKI.csv'
berkasSimpan = currentdir +'\\bab_05_06a_KB4TALKI.pdf'
# judulDiagram = 'KB4TALKI\nTahun 2022'
sumbuX = 'Cakupan'
sumbuY = 'Puskesmas\ Kabupaten'
tickerSumbuX = np.arange(0,110,25)

# read data file
colnames = ['puskesmas','KB4T','ALKI']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
puskesmas = data.puskesmas.tolist()
bar1 = data.KB4T.tolist()
bar2 = data.ALKI.tolist()

ind = np.arange(len(puskesmas))  # the x locations for the groups
width = 0.35       # the width of the bars
widthDL = 0.2      # spacing for data labels

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label = 'PUS 4T menjadi peserta KB Aktif')
rects2 = ax.barh(ind + width, bar2, width, color='orangered', label = 'PUS ALKI menjadi peserta KB Aktif')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.set_xlabel(sumbuX)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}%".format(x)))

ax.set_yticks(ind+width/2)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in puskesmas ]))
ax.invert_yaxis()
ax.set_ylabel(sumbuY)

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=1)

# add data label
for i, v in enumerate(bar1):
    ax.text(v + widthDL, i, '{:n}'.format(round(v,2)), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v + widthDL, i + width, '{:n}'.format(round(v,2)), ha='left', va='center', fontsize='x-small')

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