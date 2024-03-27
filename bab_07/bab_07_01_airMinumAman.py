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

berkasData = currentdir +'\\bab_07_01_dataAirMinumAman.csv'
berkasSimpan = currentdir +'\\bab_07_01_airMinumAman.pdf'
# judulDiagram = 'Cakupan Sarana Air Minum Aman\nTahun 2023'
sumbuX = 'Cakupan'
sumbuY = 'Kecamatan\ Kabupaten'
labelBar1 = 'Sarana Air Minum Aman'
tickerSumbuX = np.arange(0,110,25)

# read data file
colnames = ['kecamatan','airMinumAman']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.airMinumAman.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.5       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label=labelBar1)

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xlabel(sumbuX)
ax.set_ylabel(sumbuY)
formatter = FuncFormatter(lambda x, pos: "{:n}%".format(x))
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks(tickerSumbuX)

ax.set_yticks(ind)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in kecamatan ]))
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
#ax.grid(axis='y',ls='dashed')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# add data labels
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
#plt.show()