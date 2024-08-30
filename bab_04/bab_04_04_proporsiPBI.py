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

berkasSimpan = currentdir + '\\bab_04_04_proporsiPBI.pdf'
# judulDiagram = 'Anggaran Kesehatan'
judulDiagram = 'Proporsi PBI'
 
# Data to plot
labels = '', 'PBI'
paguDinkes = 102135300434
paguJKN = 18799200000
paguDinkesNonJKN = paguDinkes - paguJKN
sizes = [paguDinkesNonJKN,paguJKN]
colors = ['lightskyblue', 'lightcoral']
explode = (0.05, 0.05)  # explode 1st slice

# we only want to display one slice
# return the desired format with replace instead of lambda
def my_autopct(pct):
    return ('%.2f%%' % pct).replace('.', ',') if pct < 20 else ''
    
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        # autopct=lambda p : '{:n}%'.format(round(p,2)), shadow=True, textprops=dict(fontsize=12), startangle=80)
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=my_autopct, shadow=True, textprops=dict(fontsize=12), startangle=90)
plt.pie(sizes, explode=explode, labels=labels, autopct=my_autopct, shadow=True, textprops=dict(fontsize=12), startangle=90)

centre_circle = plt.Circle((0,0),0.45,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')

pyrfig = plt.figure(1)
# pyrfig.suptitle(judulDiagram)
pyrfig.set_figwidth(7)
pyrfig.set_figheight(4)
pyrfig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
# plt.show(pyrfig)
