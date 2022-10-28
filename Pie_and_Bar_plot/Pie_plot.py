# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:23:44 2022

@author: Suresh BASNET
"""

import matplotlib.pyplot as plt       # Import the python plot library.

labels=['Python', 'Matlab','Java','Fortran'] # Labels or Users

sizes=[40, 35, 15, 10]           # Size of Users or Labels.

plt.figure(figsize = [10,6])        # Control the figure size

#========Command for Pie plot with including size,
 # autopct(Add the percentage contribution of each labels with 
 # formatting the decimal places, with direction of labels, 
 # inclination of initiated label, and fontsize of assign autopact.)
 
plt.pie(sizes,autopct='%1.1f%%',counterclock=False,startangle=90,
        textprops={"fontsize":14})

#=====Fonts in times new roman
plt.rcParams.update({'font.family':'Times New Roman'})

#==========Title of plot with fontsize and its color.
plt.title('Pie Chart plot', fontsize=16, color='blue')

#=============
plt.legend(labels=labels, fontsize=14, loc='upper center', 
         bbox_to_anchor=(0.5, -0.001), ncol=4) # bbox_to_anchor=
   # (Change the position of legend,change the gap between plot and legend)

#===Save the obtained plot with specified figure format, 
    # dpi and name of the plot.
plt.savefig('Pie_plot.pdf', dpi=300,bbox_inches='tight')

plt.show()