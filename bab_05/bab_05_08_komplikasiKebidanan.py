# this file is not used. we use 05_05e instead
import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'Indonesian_indonesia.1252')
# utf-8 doesn't work with Windows 8 or older
# locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')

## necessary if you need to refer other directory
## otherwise just refer it directly
# import sys, os, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

# import konstan
# berkasData = konstan.direktori5 + 'bab_05_08_dataKomplikasiKebidanan.csv'

berkasData = 'bab_05_08_dataKomplikasiKebidanan.csv'
judulDiagram = 'Penanganan Komplikasi Kebidanan'
sumbuX = 'Cakupan'
sumbuY = 'Puskesmas'
berkasSimpan = 'bab_05_8_dataKomplikasiKebidanan.pdf'

# read data file
colnames = ['puskesmas','komplikasi']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
puskesmas = data.puskesmas.tolist()
bar1 = data.komplikasi.tolist()

ind = np.arange(len(puskesmas))  # the x locations for the groups
width = 0.4       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.barh(ind, bar1, width, color='steelblue', label = 'Komplikasi Kebidanan')

# add some text for labels, title and axes ticks
ax.set_title(judulDiagram)

ax.set_xticks(np.arange(0,310,50))
ax.set_xlabel(sumbuX)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}%".format(x)))

ax.set_yticks(ind)
ax.set_yticklabels(list([ '\n'.join(wrap(l, 10)) for l in puskesmas ]))
ax.invert_yaxis()
ax.set_ylabel(sumbuY)

ax.tick_params(axis='both', which='major', labelsize='small')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# make legend box
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# make labels for bars
# add data label
for i, v in enumerate(bar1):
    ax.text(v, i, '{:n}'.format(v), ha='left', va='center', fontsize='x-small')

# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
# plt.show()