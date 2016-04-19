#filestream= open("data.txt","r")
#line = filestream.readline()
lineData =""
outputstream = open("BigramVocabulary.txt","a")
outputstream2 = open("BigramVocabulary2.txt","w")
with open("RefinedData.txt","r") as filestream:
	for line in filestream:
#		line[0]='$'
		line+='$'
#		print line
		lineWN = ' '.join([word for word in line.split() if not word.isdigit()])
		lineData = lineData + lineWN + " "
#print lineData
SplitLine= lineData.split()
countb = {}
for word in SplitLine:
	if word == "+" or word=="-":
			SplitLine[SplitLine.index(word)]= "*" 
nindex=1
#print SplitLine
for word in SplitLine:
#	print word
	if word!="$" :
#		print word 
#		print SplitLine.index(word)
		next_word = SplitLine[nindex]
#		print next_word
		biword = word + " " + next_word
#		print biword
#		print hai
		if biword not in countb:
			countb[biword] = 0
		countb[biword]+=1
	nindex+=1
for word in countb:
	if countb[word]>=3:
#		print word
#		print countb[word]
		outputstream.write(word + '\n')
		outputstream2.write(word + '\n')
		
		
		
		
