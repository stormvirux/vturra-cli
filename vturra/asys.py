#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy import stats
# import statsmodels.api as sm
# from numpy.random import randn
import matplotlib as mpl
# import seaborn as sns

# sns.set_color_palette("deep", desat=.6)
mpl.rc("figure", figsize=(8, 4))

def Compavg():
	data=Total()
	markMax=[]
	markAvg=[]
	N = 5
	ind = np.arange(N)    
	width = 0.35 
	fig = plt.figure()
	ax = fig.add_subplot(111)      
	markMax.extend((data["Total"].max(),data["Total.1"].max(),data["Total.2"].max(),data["Total.3"].max(),data["Total.4"].max()))
	markAvg.extend((data["Total"].mean(),data["Total.1"].mean(),data["Total.2"].mean(),data["Total.3"].mean(),data["Total.4"].mean()))
	rects1 = ax.bar(ind, markMax, width, color='black')
	rects2 = ax.bar(ind+width, markAvg, width, color='green')
	ax.set_xlim(-width,len(ind)+width)
	ax.set_ylim(0,120)
	ax.set_ylabel('Marks')
	ax.set_title('Max, Mean and Your Marks')
	xTickMarks = ['Subject'+str(i) for i in range(1,6)]
	ax.set_xticks(ind+width)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=10, fontsize=10)
	ax.legend( (rects1[0], rects2[0]), ('Max', 'Mean') )
	plt.show()
	
def compSub():
	# max_data = np.r_[data["Total"]].max()
	# bins = np.linspace(0, max_data, max_data + 1)
	data=Total()
	plt.hist(data['Total'],linewidth=0, alpha=.7)
	plt.hist(data['Total.1'],linewidth=0,alpha=.7)
	plt.hist(data['Total.2'],linewidth=0,alpha=.7)
	plt.hist(data['Total.3'],linewidth=0,alpha=.7)
	plt.hist(data['Total.4'],linewidth=0,alpha=.7)
	plt.title("Total marks Histogram")
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	plt.show()

def Total():
	data=pd.read_csv("output10cs.csv")
	df3=data[['Total','Total.1','Total.2','Total.3','Total.4','Total.5','Total.6','Total.7']]
	data["Main Total"]=df3.sum(axis=1)
	data = data.dropna()
	data.reset_index(drop=True)
	return data

#compSub()
# Compavg()
