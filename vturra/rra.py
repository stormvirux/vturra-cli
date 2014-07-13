#!/usr/bin/env python
# -*- coding: utf-8 -*-

usn=""
usnl=[]
from bs4 import BeautifulSoup 
import select
import asys
import glob
import os
import sys
import shutil
from select import select
timeout=10

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
				# fl.write(lol[-10])
			fl.close()
		x+=1
	
def parsehtml(response,x):
	#files=glob.glob("results/*.*")
	#files.sort()
	#x=0
	#print files
	#for f in files:
	#page_html=open(f)
	soup=BeautifulSoup(response.read())
	all_tds = [td for td in soup.findAll("td", width="513")]
	fl = open("results/"+usnl[x]+".html", 'wb')
	lol=all_tds[0]
	record = '%s' % (lol)
	if record:
		fl.write(record)
	fl.close()
	#x=x+1
		
def ret():
	import requests
	import shutil
	import mechanize
	year=sys.argv[1]
	branches=sys.argv[2]
	x=0
	for rno in range(1,3):
		usn="4pa"+year+branches+"%03d"%rno
		print usn
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.open("http://results.vtu.ac.in/")
		#fl=open("results/"+usn+".html","wb")
		br.select_form(nr=0)
		br['rid']=usn
		response=br.submit()
		usnl.append(usn)
		parsehtml(response,x)
		x=x+1		
		#shutil.copyfileobj(br.submit(),fl)		
		#fl.close()
		
			

def main():
	inputIndex()
	if not os.path.exists("results"):
		os.makedirs("results")
	ret()
	#parsehtml()
	getval()
	while True:		
		print("""1.Compute average
2.Compare with max and average
3.Quit""")
		rlist, _, _ = select([sys.stdin], [], [], timeout)		
		if(rlist):
			sel=sys.stdin.readline()
		else:
			print "Time out exiting"			
			break		
		#sel=raw_input("Select an Analysis\n")
		if sel=="1":
			asys.Compavg()
		elif sel=='2':
			asys.compSub()
		elif sel=='3':
			print("Exiting")
			break
	shutil.rmtree('results')
	return 0


if __name__ == '__main__':
	inputIndex()
	main()
	#asys.Compavg()
	#asys.compSub()

# TODO:Names of those whose result has not come out
