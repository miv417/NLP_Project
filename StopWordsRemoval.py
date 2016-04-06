stopwordfile = open("stopwords.txt","r")
stopwords = stopwordfile.read()
#filestream= open("data.txt","r")
#line = filestream.readline()
outputstream = open("RefinedData.txt","w")
with open("data.txt","r") as filestream:
	for line in filestream:
		line = line.lower()
		lineWP = "".join([c for c in line if c not in('!','?','.',',',':','(',')','/','1','2','3','4','5','6','7','8','9','0')])
		lineWS = ' '.join([word for word in lineWP.split() if word not in stopwords])
		outputstream.write(lineWS + "\n")
	

