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

berkasData = currentdir +'\\bab_06_00_dataPenyakitTerbanyak.csv'
berkasSimpan = currentdir +'\\bab_06_00_penyakitTerbanyak.pdf'
# judulDiagram = '10 Penyakit Terbanyak\nTahun 2021'
sumbuX = 'Jumlah Kasus'
sumbuY = 'Penyakit'
labelBar1 = 'Penyakit terbanyak'
tickerSumbuX = np.arange(0,10100,2000)

colnames = ['penyakit','jumlahKasus']
data = pandas.read_csv(berkasData, names=colnames, delimiter=';')
penyakit = data.penyakit.tolist()
jumlahKasus = data.jumlahKasus.tolist()

# 10 penyakit terbanyak -> [0:10], 20 penyakit terbanyak -> [0:20]
y_pos = np.arange(0,len(penyakit[0:10])*2,2)
# need to space out bars
new_y = [1.5*i for i in y_pos]
# ...don't know what this supposed to do, nor where got it from
#performance = 5 + 10 * np.random.rand(len(penyakit[0:20]))
# width for data label spacing. depends on width of corresponding axis
widthDL = 100

# initiate plot
plt.rcdefaults()
fig, ax = plt.subplots()

# make bars
ax.barh(new_y, jumlahKasus[0:10], height=2, align='center',color='lightblue', ecolor='black', label = labelBar1)

# settings for y axis
ax.set_yticks(new_y)
ax.set_ylabel(sumbuY)
ax.invert_yaxis()  # labels read top-to-bottom

# setting for x axis
ax.set_xlabel(sumbuX)
ax.set_xticks(tickerSumbuX)
# plt.axis(xmin=(0), xmax=(10000))

# settings for both axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(left=False)

# add some text for title, labels and axes ticks
# ax.set_title(judulDiagram)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: "{:n}".format(x)))
#for i, v in enumerate(jumlahKasus[0:10]): plt.text(v,new_y[i], '{:n}'.format(v), va="center", fontsize=8)
for i, txt in enumerate(jumlahKasus[0:10]):
		#ax.annotate('{:n}'.format(txt), (txt,new_y[i]), fontsize=9, va="center")
        ax.text(txt + widthDL, new_y[i], '{:n}'.format(txt), ha='left', va='center', fontsize=9)
wrapLabels = [ '\n'.join(wrap(l, 30)) for l in penyakit[0:10] ]
ax.set_yticklabels(wrapLabels, fontsize=8)

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