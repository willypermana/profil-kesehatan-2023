import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# run this script from any directory
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

berkasData = currentdir +'\\bab_07_05_dataTPPHSP.csv'
berkasSimpan = currentdir +'\\bab_07_05_TPPHSP.pdf'
# judulDiagram = 'Cakupan Tempat Pengolahan Makanan Sehat'
sumbuX = 'Cakupan'
sumbuY = 'Jenis TPP'
labelBar1 = 'TPP laik HSP'
tickerSumbuX = np.arange(0,110,25)

# read data file
colnames = ['jenisTPP','TPP']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
jenisTPP = data.jenisTPP.tolist()
data.TPP.fillna(np.nan)
bar1 = data.TPP.tolist()

ind = np.arange(len(jenisTPP))  # the x locations for the groups
width = 0.5       # the width of the bars
widthDL = 0.2      # spacing for data labels

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label=labelBar1)
# in case need to set individual color
#rects1[7].set_color('tomato')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}%".format(x)))
ax.set_xlabel(sumbuX)

ax.set_yticks(ind)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 15)) for l in jenisTPP ]))
ax.set_ylabel(sumbuY)
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=1)

# add data labels
for i, v in enumerate(bar1):
    # check if the coordinate is not NaN
    # the script run fine without it, but it was nice to not see any error popping
    if np.isfinite(v):
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
# plt.show()