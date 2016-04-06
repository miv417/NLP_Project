stopwordfile = open("stopwords.txt","r")
stopwords = stopwordfile.read()
#filestream= open("data.txt","r")
#line = filestream.readline()
lineData =""
with open("data.txt","r") as filestream:
	for line in filestream:
		line = line.lower()
		lineWP = "".join([c for c in line if c not in('!','?','.',',',':','(',')','-','+','/')])
		lineWS = ' '.join([word for word in lineWP.split() if word not in stopwords and word.isalpha()])
		lineData = lineData + lineWS + " "
SortedLine = lineData.split()
counts = {}
for word in SortedLine:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

outputstream = open("Vocabulary.txt","w")
for word in counts:
	if counts[word]>=2:
		outputstream.write(word + '\n')
		
		
	

	

