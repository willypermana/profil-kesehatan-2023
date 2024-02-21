import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'Indonesian_indonesia.1252')

berkasData = r'F:\dokumenDinkesBeltim2019\juknis profil 2018_new\profil kesehatan 2018\grafik\bab_6_5a_dataSalinNakes.csv'
judulDiagram = 'Cakupan Persalinan Ditolong Nakes Terlatih'
sumbuY = 'Cakupan'
berkasSimpan = r'F:\dokumenDinkesBeltim2019\juknis profil 2018_new\profil kesehatan 2018\grafik\bab_6_5a_salinNakes.pdf'

# read data file
colnames = ['kecamatan','salinNakes']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
kecamatan = data.kecamatan.tolist()
bar1 = data.salinNakes.tolist()

ind = np.arange(len(kecamatan))  # the x locations for the groups
width = 0.5       # the width of the bars

# make bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind, bar1, width, color='steelblue', label = 'Persalinan ditolong Nakes')

# add some text for labels, title and axes ticks
ax.set_title(judulDiagram)
ax.set_ylim(0,115)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: '{:.0f}%'.format(y)))

ax.set_xticks(ind)
wrapKecamatan = [ '\n'.join(wrap(l, 10)) for l in kecamatan ]
ax.set_xticklabels(list(wrapKecamatan), fontsize='small')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
ax.legend(fontsize='x-small', loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# make labels for bars
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.1+height,
                locale.format('%.2f',height),
                ha='center', va='bottom', fontsize='xx-small',)

autolabel(rects1)


# finishing
pyrfig = plt.figure(1)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
#fig.savefig(berkasSimpan, bbox_inches='tight')
#plt.close(pyrfig)
plt.show()