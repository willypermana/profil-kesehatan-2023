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

judulDiagram = 'Distribusi Gender'
berkasSimpan = currentdir + '\\bab_01_2_distribusiGender.pdf'
 
# Data to plot
labels = 'Laki-laki', 'Perempuan'
sizes = [66201,62847]
colors = ['lightskyblue', 'lightcoral']
explode = (0.1, 0)  # explode 1st slice
 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct=lambda p : '{:n}%'.format(round(p,2)), shadow=True, textprops=dict(fontsize=12), startangle=80)

plt.axis('equal')
pyrfig = plt.figure(1)
# pyrfig.suptitle(judulDiagram)
pyrfig.set_figwidth(7)
pyrfig.set_figheight(4)
pyrfig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
# plt.show(pyrfig)
