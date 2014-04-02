#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rra.py
#  
#  Copyright 2014 Thaha Muhammed <storm@storm-lappy>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
usn=""
usnl=[]
from bs4 import BeautifulSoup 
import re
import asys
import glob
import os
import sys
import sys
import shutil 
def inputIndex():
	import codecs
	x=0
	fl = codecs.open('output'+sys.argv[1]+sys.argv[2]+'.csv', 'wb',encoding="Utf-8")
	fl.write("usn,")
	while x<8:
		fl.write("External,Internal,Total,")
		x+=1
	fl.write("Main Total\n")
	fl.close()

def getval():
	import codecs
	lol=[]
	record=[]
	x=0
	while x<len(usnl):
		page_html=open("results/"+usnl[x]+".html", 'rb')
		soup=BeautifulSoup(page_html)
		soup.prettify()
		fl = codecs.open('output'+sys.argv[1]+sys.argv[2]+'.csv', 'ab',encoding="Utf-8")
		record=[texts.text for texts in soup.findAll('td',{"align":"center"})]
		"""for y in soup.findAll("td"):
			if y.parent.name=="tr":
				lol.append(y.text)
		if lol[-10] == "A" or lol[-10]=="P" or lol[-10]=="F":
			lol[-10],lol[-1]=lol[-1],lol[-10]"""
		del record[0:4]
		for y in record:
			if "P" in y: record.remove("P")
			elif "F" in y: record.remove("F")
			elif "A" in y: record.remove("A")
				
		if len(record)>24:
			del record[24:]
		if "Total" in record: del record[:]	
		if record:
			fl.write("\n"+usnl[x]+",")
			for y in record:
				fl.write(y)
				fl.write(",")	
				#fl.write(lol[-10])
			fl.close()
		x+=1
	
def parsehtml():
	records=[]
	files=glob.glob("results/*.*")
	print files.sort()
	x=0
	print files
	for f in files:
		page_html=open(f)
		soup=BeautifulSoup(page_html)
		all_tds = [td for td in soup.findAll("td", width="513")]
		fl = open("results/"+usnl[x]+".html", 'wb')
		lol=all_tds[0]
		record = '%s' % (lol)
		if record:
			fl.write(record)
		fl.close()
		x=x+1
		
def ret():
	import requests
	x=0
	year=sys.argv[1]
	branches=sys.argv[2]
	for rno in range(1,12):
		usn="4pa"+year+branches+"%03d"%rno
		payload={'rid':usn,'submit':'submit'}
		r=requests.post("http://results.vtu.ac.in/vitavi.php/post",data=payload)
		fl=open("results/"+usn+".html","wb")
		fl.write(r.text)
		fl.close()
		usnl.append(usn)
			

def main():
	inputIndex()
	if not os.path.exists("results"):
		os.makedirs("results")
	ret()
	parsehtml()
	getval()
	asys.Compavg()
	asys.compSub()
	shutil.rmtree('results')
	return 0


if __name__ == '__main__':
	inputIndex()
	main()
	asys.Compavg()
    	asys.compSub()

#TODO:Names of those whose result has not come out
