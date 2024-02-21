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

berkasData = currentdir +'\\bab_02_3_dataPosyandu.csv'
judulDiagram = 'Cakupan Posyandu Aktif'
sumbuX = 'Cakupan'
tickerSumbuX = np.arange(0,101,25)
sumbuY = 'Kecamatan/ Kabupaten'
berkasSimpan = currentdir +'\\bab_02_3_posyandu.pdf'

# read data file
colnames = ['kecamatan','posyandu']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.posyandu.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.5       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label = 'Posyandu Aktif')

# add some text for labels, title and axes ticks
ax.set_title(judulDiagram)
ax.set_xticks(tickerSumbuX)
ax.set_xlabel(sumbuX)
ax.set_ylabel(sumbuY)
formatter = FuncFormatter(lambda x, pos: "%d%%" % (x))
ax.xaxis.set_major_formatter(formatter)

ax.set_yticks(ind)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in kecamatan ]))
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
#ax.grid(axis='y',ls='dashed')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box below chart
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=1)

# make labels for bars
# def autolabel(rects):
    # """
    # Attach a text label above each bar displaying its height
    # """
    # for rect in rects:
        # width = rect.get_width()
        # ax.text(rect.get_y() + rect.get_height()/2., 1.01*width,
                # '%.2f' % float(width),
                # ha='center', va='bottom', fontsize='x-small')

# autolabel(rects1)

# horizontal bar labels. remember to figure out converting to function
for i, v in enumerate(bar1):
    ax.text(v+0.5, i, locale.format_string('%.2f',float(v)), ha='left', va='center', fontsize='x-small')
    #locale.format('%.2f',height)

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