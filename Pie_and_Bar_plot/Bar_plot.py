# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:11:31 2022

@author: Suresh BASNET
"""

import matplotlib.pyplot as plt  # Import the python plot library.
labels=['Python','Matlab','Fortran','Java', 'PHP'] # Labels

index=[1,2,3,4,5]           # Indexing the Labels.

sizes=[60,50,40,30,45]      # Height of bar plot (Magnitude of Labels). 

SE=[2.5, 1.5,1.0,0.5,0.8]   # Symmetric Standard Error on each Labels. 

#========Command for bar plot with including error, color, and capsize.
plt.bar(index,sizes,tick_label=labels,color="lightgray",yerr=SE,
        ecolor='r',capsize=5)

#====Y-label with fontsize and its color.
plt.ylabel('Number of users', fontsize=14,color='r')

#====X-label with fontsize and its color.
plt.xlabel('Programming language', fontsize=14,color='black')
#===========Title of the obtained plot with fontsize and its color.
plt.title('Bar plot of pragramming langugae users',fontsize=16, 
          color = "red")  

plt.xticks(fontsize=14)     # Fontsize of xticks
plt.yticks(fontsize=14)     # Fontsize of yticks

plt.ylim(0,70)              # y-limit.

#===Save the obtained plot with specified figure format, 
    # dpi and name of the plot.
plt.savefig('Bar_plot.pdf', dpi=300,bbox_inches='tight')

#=====Fonts in times new roman
plt.rcParams.update({'font.family':'Times New Roman'})

plt.show()

#===========================Grouped bar chart

Barwidth=0.3  #====Width of bar.

Team_A=[40,35,30,20,35]         # Magnitude of Team A.

SE_A = [1.5,0.8,0.6,0.4,0.6]    # Standard error for Team A for each labels.

Team_B=[60,50,40,30,45]         # Magnitude of Team B.

SE_B=[2.5,1.8,1.2,0.8,1.0]     # Standard error for Team B for each labels.

index_team_A=[1,2,3,4,5]       # Indexing the Labels for Team A.

# Indexing the Labels for Team B.
index_team_B=[i+Barwidth for i in index_team_A] 
 
# Determine the mid point for the ticks
ticks=[i+Barwidth/2 for i in index_team_A]

tick_labels=['Python','Matlab','Fortran','Java','PHP'] # Tick Labels

#========Command for groupbar plot with including error, color, and capsize.
plt.bar(index_team_A,Team_A,Barwidth,color='b', label='Team A',yerr=SE_A,
        ecolor='k',capsize=5)

plt.bar(index_team_B,Team_B,Barwidth,color='r', label='Team B',yerr=SE_B,
        ecolor='k',capsize=5)

#=======================Graph Set up
#====x-label with fontsize and its color.
plt.xlabel('Programming language',fontsize=14,color='k')
#====y-label with fontsize and its color.
plt.ylabel('Number of users', fontsize=14,color='r')

#==========Put ticks in x-label with fontsize.
plt.xticks(ticks,tick_labels,fontsize=12)

plt.yticks(fontsize=14)  # Fontsize of y-ticks.

plt.legend(fontsize=14,loc='upper right')  # Put the legend on the plot.

#===========Title of the obtained plot with fontsize and its color.
plt.title('Bar plot of programming language for two teams',
          fontsize=14,color='k')

plt.ylim(0,70)   # Assign the y-limit.
#===Save the obtained plot with specified figure format, 
    # dpi and name of the plot.
plt.savefig('Bar_plot_two_teams.pdf',dpi=300,bbox_inches='tight')

plt.show()



