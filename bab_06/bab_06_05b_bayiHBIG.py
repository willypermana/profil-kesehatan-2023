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

berkasData = currentdir +'\\bab_06_05b_dataBayiHBIG.csv'
berkasSimpan = currentdir +'\\bab_06_05b_bayiHBIG.pdf'
# judulDiagram = 'Bayi dari Ibu Hamil HB mendapat HBIG\nTahun 2022'
sumbuX = 'Cakupan'
sumbuY = 'Puskesmas/ Kabupaten'
labelBar1 = 'Bayi dari Ibu HBsAg mendapat HBIG kurang dari 24 jam'
labelBar2 = 'Total bayi dari Ibu HBsAg mendapat HBIG'
tickerSumbuX = np.arange(0,110,25)

# read data file
colnames = ['puskesmas','bayiHBIG24','bayiHBIGtotal']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
puskesmas = data.puskesmas.tolist()
bar1 = data.bayiHBIG24.tolist()
bar2 = data.bayiHBIGtotal.tolist()

ind = np.arange(len(puskesmas))  # the x locations for the groups
width = 0.4      # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label = labelBar1)
rects2 = ax.barh(ind + width, bar2, width, color='orangered', label = labelBar2)

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.set_xlabel(sumbuX)
formatter = FuncFormatter(lambda x, pos: "{:n} %".format(x))
ax.xaxis.set_major_formatter(formatter)

ax.set_yticks(ind+0.5*width)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in puskesmas ]))
ax.set_ylabel(sumbuY)
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
ax.tick_params(axis='y')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# add data label
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v+0.5, i+width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
    
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