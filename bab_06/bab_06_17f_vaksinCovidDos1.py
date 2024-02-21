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

berkasData = currentdir +'\\bab_06_17f_dataVaksinCovidDos1.csv'
berkasSimpan = currentdir +'\\bab_06_17f_vaksinCovidDos1.pdf'
# judulDiagram = 'Cakupan Vaksin COVID-19 Dosis 1\nTahun 2022'
sumbuX = 'Cakupan Vaksin COVID-19 Dosis 1'
sumbuY = 'Puskesmas/ Kabupaten'
tickerSumbuX = np.arange(0,110,25)
labelBar1 = '6-11 tahun'
labelBar2 = '12-17 tahun'
labelBar3 = '18-59 tahun'
labelBar4 = '$\geq$ 60 tahun'
labelBar5 = 'Total'

# read data file
colnames = ['puskesmas','vaksinAnak','vaksinRemaja','vaksinUsipro','vaksinUsila','vaksinTotal']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
puskesmas = data.puskesmas.tolist()
bar1 = data.vaksinAnak.tolist()
bar2 = data.vaksinUsila.tolist()
bar3 = data.vaksinUsipro.tolist()
bar4 = data.vaksinUsila.tolist()
bar5 = data.vaksinTotal.tolist()

ind = np.arange(len(puskesmas))  # the x locations for the groups
width = 0.18       # the width of the bars
widthDL = 0.5

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label=labelBar1)
rects2 = ax.barh(ind + width, bar2, width, color='tomato', label = labelBar2)
rects3 = ax.barh(ind + 2*width, bar3, width, color='yellowgreen', label = labelBar3)
rects4 = ax.barh(ind + 3*width, bar4, width, color='violet', label = labelBar4)
rects5 = ax.barh(ind + 4*width, bar5, width, color='teal', label = labelBar5)

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.set_xlabel(sumbuX)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}%".format(x)))

ax.set_yticks(ind+2*width)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in puskesmas ]))
ax.invert_yaxis()
ax.set_ylabel(sumbuY)

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

# add data label
for i, v in enumerate(bar1):
    ax.text(v + widthDL, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v + widthDL, i+width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar3):
    ax.text(v + widthDL, i+2*width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar4):
    ax.text(v + widthDL, i+3*width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar5):
    ax.text(v + widthDL, i+4*width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
    
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