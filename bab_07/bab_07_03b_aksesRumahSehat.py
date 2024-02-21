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

berkasData = currentdir +'\\bab_07_03b_dataAksesRumahSehat.csv'
berkasSimpan = currentdir +'\\bab_07_03b_aksesRumahSehat.pdf'
# judulDiagram = 'Cakupan Akses Rumah Sehat\nTahun 2022'
sumbuX = 'Cakupan'
sumbuY = 'Kecamatan/ Kabupaten'
labelBar1 = 'Akses Rumah Sehat'
tickerSumbuX = np.arange(0,110,25)

# read data file
colnames = ['kecamatan','rumahSehat']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.rumahSehat.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.5       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label=labelBar1)

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xlabel(sumbuX)
ax.set_ylabel(sumbuY)

ax.set_xticks(tickerSumbuX)
formatter = FuncFormatter(lambda x, pos: "{:n}%".format(x))
ax.xaxis.set_major_formatter(formatter)

ax.set_yticks(ind)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in kecamatan ]))
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
#ax.grid(axis='y',ls='dashed')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=1)

# add data labels
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
#plt.show()