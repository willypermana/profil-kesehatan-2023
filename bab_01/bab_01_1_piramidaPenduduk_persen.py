import numpy as np
import matplotlib.pyplot as plt
import pandas
import locale
locale.setlocale(locale.LC_ALL, 'Indonesian_indonesia.1252')
## change used fonts
#plt.rcParams['font.sans-serif'] = 'Roboto'
## force matplotlib to use TrueType fonts
plt.rcParams['pdf.fonttype'] = 42
plt.style.use('seaborn-paper')

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

berkasData = currentdir + '\\bab_01_1_dataPiramidaPenduduk.csv'
berkasSimpan = currentdir +'\\bab_01_1_piramidaPenduduk.pdf'
# judulDiagram = 'Piramida Penduduk Kabupaten Belitung Timur\nTahun 2023'

colnames = ['kelompokUmur','popLakiLaki','popPerempuan']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
sumbuY = data.kelompokUmur.tolist()
bar2 = data.popLakiLaki.tolist()
bar1 = data.popPerempuan.tolist()
bar2_persen =[round(i/sum(bar2)*100,2) for i in bar2]
bar1_persen =[round(i/sum(bar1)*100,2) for i in bar1]
print(bar2_persen)
print(bar1_persen)

def pyramid_plot(ylabels, data_left, xlabel_left, data_right, xlabel_right, fig=None, **kwargs):
    if(fig is None):
        fig = plt.figure()

    y_pos = np.arange(len(ylabels))
    empty_ticks = tuple('' for n in ylabels)
    rentang = 15

    fig.add_subplot(121)
    plt.barh(y_pos, data_left, **kwargs)
    #plt.barh(y_pos, data_left, color ="#bfe4ff", **kwargs)
    for i, v in enumerate(data_left): plt.text(v,i, '{:n} %'.format(v), ha="right", va="center", fontsize="small")	
    plt.yticks(y_pos, empty_ticks, va="center", ha='center')
    #oldlims = plt.gca().get_xlim()
    #print oldlims
    #plt.axis(xmin=oldlims[1], xmax=oldlims[0])
    plt.axis(xmin=rentang, xmax=(0))
    plt.tick_params(axis='x', which='major', labelsize='small')
    plt.tick_params(axis='y', which='major', length=0)
    plt.xlabel(xlabel_left)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)

    fig.add_subplot(122)
    plt.barh(y_pos, data_right, color="red", **kwargs)
    plt.axis(xmin=(0), xmax=rentang)
    plt.yticks(y_pos, ylabels)
    for i, v in enumerate(data_right): plt.text(v,i, '{:n} %'.format(v), va="center", fontsize="small")
    plt.xlabel(xlabel_right)
    plt.tick_params(axis='x', which='major', labelsize='small')
    plt.tick_params(axis='y', which='major', length=0)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    return fig
	
# Plot the data
pyrfig = plt.figure(1)
pyrfig = pyramid_plot(sumbuY, bar2_persen, 'Laki-Laki', bar1_persen, 'Perempuan', pyrfig, align='center', alpha=0.4)

pyrfig.suptitle('Piramida Penduduk Kabupaten Belitung Timur\nTahun 2019')
#pyrfig.set_figwidth(1.5*pyrfig.get_figheight())
pyrfig.set_figwidth(9)
pyrfig.set_figheight(5)
plt.tick_params(axis='both', which='major', labelsize='small')
#pyrfig.savefig(berkasSimpan,bbox_inches='tight')
#plt.close(pyrfig)
plt.show()