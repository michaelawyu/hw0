#Intro. to Databases Homework 0
#Chen Yu
#!/usr/bin/env python


wordCount=0
def findString(string):
	global wordCount
	if string.find('single malt scotch')!=-1:
		wordCount=wordCount+1
newfile=open('iowa-liquor-sample.csv','r')
for line in newfile:
	lowerLine=line.lower()
	findString(lowerLine)
print 'Wordcount:',wordCount
newfile.close()

