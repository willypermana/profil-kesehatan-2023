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

## import konstan no longer needed, use currentdir instead
# import konstan
berkasData = currentdir +'\\bab_05_01_dataKematianIbu.csv'
# judulDiagram = 'Kematian Ibu\nTahun 2021'
berkasSimpan = currentdir +'\\bab_05_01_kematianIbu.pdf'
sumbuX = 'Jumlah'
sumbuY = 'Puskesmas/ Kabupaten'

# read data file
colnames = ['kecamatan','kasusIbuHamil','kasusIbuSalin','kasusIbuNifas','jumlahKasusIbu']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.kasusIbuHamil.tolist()
bar2 = data.kasusIbuSalin.tolist()
bar3 = data.kasusIbuNifas.tolist()
bar4 = data.jumlahKasusIbu.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.24       # the width of the bars
widthDL = 0.1      # spacing for data labels

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='royalblue', label = 'Kematian Ibu Hamil')
rects2 = ax.barh(ind + width, bar2, width, color='#cc0000', label = 'Kematian Ibu Bersalin')
rects3 = ax.barh(ind + 2*width, bar3, width, color='navy', label = 'Kematian Ibu Nifas')
rects4 = ax.barh(ind + 3*width, bar4, width, color='yellowgreen', label = 'Jumlah Kematian Ibu')

# add some text for labels, title and axes ticks
# ax.set_title(judulDiagram)
ax.set_xlim(0,5)
ax.set_xlabel(sumbuX)
ax.set_ylabel(sumbuY)
formatter = FuncFormatter(lambda x, pos: "{:n}".format(x))
ax.xaxis.set_major_formatter(formatter)

ax.set_yticks(ind+0.36)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in kecamatan ]))
ax.invert_yaxis()

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# add data label
for i, v in enumerate(bar1):
    ax.text(v+widthDL, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar2):
    ax.text(v+widthDL, i+width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar3):
    ax.text(v+widthDL, i+2*width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')
for i, v in enumerate(bar4):
    ax.text(v+widthDL, i+3*width, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
# plt.show()