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

berkasData = currentdir + '\\bab_04_03_dataAnggaran.csv'
berkasSimpan = currentdir + '\\bab_04_03_anggaranKesehatan.pdf'
# judulDiagram = 'Anggaran Kesehatan'

# read data file
colnames = ['jenisJaminan','jumlahPeserta']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
labelJenis = data.jenisJaminan.tolist()
listJumlah = data.jumlahPeserta.tolist()
sliceJumlah = np.array(data.jumlahPeserta.tolist())
porcent = 100.*sliceJumlah/sliceJumlah.sum()

fig1, ax1 = plt.subplots()
# explodeTuple = (0.05, 0, 0.1, 0.0, 0.1, 0.3)
# patches, texts, autotexts = ax1.pie(listPagu, autopct='%.2f%%', pctdistance=0.85, explode=explodeTuple, startangle=80)
explodeTuple = (0.05, 0.07, 0.00, 0.05, 0.2, 0.1, 0)
patches, texts, autotexts = ax1.pie(listJumlah[0:8], autopct='%.2f%%', pctdistance=1.18, explode=explodeTuple, startangle=90, counterclock=False)

for t in autotexts:
    t.set_size(9)
# for i, a in enumerate(autotexts):
    # a.set_text("Rp {0:n}".format(listPagu[i]))
#autotexts[0].set_color('y')

centre_circle = plt.Circle((0,0),0.65,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

#labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labelJenis, slicePagu)]
labels = ['{0} - Rp {1:n}'.format(i,j) for i,j in zip(labelJenis, sliceJumlah)]

sort_legend = False
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, slicePagu),
                                          key=lambda labelJenis: labelJenis[2],
                                          reverse=True))


box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
plt.legend(patches, labels, loc='center', bbox_to_anchor=(0.5, -0.15),fontsize=8, fancybox=True, shadow=True, ncol=2)
		   
plt.axis('equal')

pyrfig = plt.figure(1)
# pyrfig.suptitle(judulDiagram)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
# tight_layout to make consistent size
# adjust subplot to make room for legend
fig.subplots_adjust(bottom=-0.15)
plt.tight_layout()
plt.savefig(berkasSimpan)
plt.close(pyrfig)
# plt.show()