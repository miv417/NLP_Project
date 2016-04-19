from math import log
vcount=0
PWcount={}
NWcount={}
PPW={}
PNW={}
with open ("Vocabulary.txt","r") as fin:
	for word in fin:
		vcount+=1;
#print vcount

#Getting the priors, ie, Probability that a given comment is +ve/-ve
positive=0
pcount=0
sum_of_accuracy = 0
ncount=0
negative=0
string1 = "file"
string2= ".txt"
testing_no = 10
while testing_no!=0:
	no=1
	while no!=testing_no:
		with open (string1+str(no)+string2,"r") as fin2:
			for line in fin2:
				if line[0]=='+':
					for word in line.split():
						word+= '\n'
						pcount+=1
						if word not in PWcount:
#							print word
							PWcount[word]=0	
						PWcount[word]= PWcount[word]+1
#						print PWcount[word]
					pcount-=1
					positive+=1
				else:
					for word in line.split():
						word+='\n'
						ncount+=1
						if word not in NWcount:
							NWcount[word]= 0
						NWcount[word]= NWcount[word] + 1
					ncount-=1
					negative+=1
		no+=1
	total=positive+negative
	Ppositive=log(float(positive)/total)
	Pnegative=log(float(negative)/total)
	#print PWcount
	FinalList=[]
	with open ("Vocabulary.txt","r") as fin3:
		for word in fin3:
			if word not in PWcount:
	#			print word
				PWcount[word]=0	
			if word not in NWcount:
				NWcount[word]=0	
	#		print NWcount[word]
	#		print PWcount[word]
			PPW[word]= log(float(PWcount[word]+1)/float(pcount+vcount))
			PNW[word]= log(float(NWcount[word]+1)/float(ncount+vcount))
	
	#vcount is count of V
	bvcount =0
	bigramv={}
	with open ("BigramVocabulary2.txt","r") as fin:
		for word in fin:
			bvcount+=1;
			bigramv[word]=0;
	
	lineData =""
	with open("RefinedData.txt","r") as filestream:
		for line in filestream:
			line+='$'
	#		print line
			lineWN = ' '.join([word for word in line.split() if not word.isdigit()])
			lineData = lineData + lineWN + "\n"
	#print lineData
	
	SplitLine= lineData.split()
	#print SplitLine
	
	counts = {}
	for word in SplitLine:
	    if word not in counts:
	        counts[word] = 0
	    counts[word] += 1
		
	
	nindex=1
	n=-1
	fw="*"
	bigramp={}
	bigramn={}
	#print SplitLine
	for word in SplitLine:
		if word== "+":
			n=1
			next_word = SplitLine[nindex]
			biword = fw + " " + next_word+"\n"
		
		elif word== "-":
			n=0
			next_word = SplitLine[nindex]
			biword = fw + " " + next_word+"\n"
			
		else :
	#	print word
			if word!="$" :
	#			print word 
	#			print SplitLine.index(word)
				next_word = SplitLine[nindex]
	#			print next_word
				biword = word + " " + next_word+"\n"
	#			print biword
	#			print hai
			if biword in bigramv:
				if n==1 :
					if biword not in bigramp:
						bigramp[biword]=0
					bigramp[biword]+=1
				else:
					if biword not in bigramn:
						bigramn[biword]=0
					bigramn[biword]+=1
		nindex+=1
	#print "HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOOOIIIIIIIIIIIIIIIIIIIIIII"
	#print bigramv	
	PPBW={}
	PNBW={}
	#print "HAAAAAooooooooooooooooooooooooooooooooooooAOOOIIIIIIIIIIIIIIIIIIIIIII"
	for word in bigramv:
		word1=word.split()
		if word not in bigramp:
	#		print word
			bigramp[word]=0	
		if word not in bigramn:
			bigramn[word]=0	
		if word1[0] not in PWcount:
			PWcount[word1[0]]=0
		if word1[0] not in NWcount:
			NWcount[word1[0]]=0
	#	print NWcount[word]
	#	print PWcount[word]
		PPBW[word]= float(bigramp[word]+1)/float(PWcount[word1[0]]+bvcount)
		PNBW[word]= float(bigramn[word]+1)/float(NWcount[word1[0]]+bvcount)
	#	print PNBW[word]
	
	#TESTING!
	
	ans = 0 
	tp=0
	tn=0
	fp=0
	fn=0
	line_count = 0
	with open (string1+str(testing_no)+string2,"r") as fin4:
		for line in fin4:
			line+='$'
			line_count+=1
			pprob = float (Ppositive)
			nprob = float (Pnegative)
	#		print line
			sline = line.split()
			nindex=1
			for word in sline:
				
				n=-1
				fw="*"
				if word =='+' or word == '-': 
					if word == '+':
						ans = 1
						n=1
						next_word = sline[nindex]
						biword = fw + " " + next_word+"\n"
					else:
						ans = 0
						n=0
						next_word = sline[nindex]
						biword = fw + " " + next_word+"\n"
						
				elif word=="$": break
				else:
					next_word= sline[nindex]
					biword = word + " " + next_word+"\n"
					
					if biword not in bigramp:
						if next_word +'\n' not in PPW:
							PPW[next_word+'\n']=1
						pprob+=PPW[next_word+'\n']
					else:
						pprob+=bigramp[biword]
						
					if biword not in bigramn:
						if next_word +'\n' not in PNW:
							PNW[next_word+'\n']=1
						nprob+=PNW[next_word+'\n']
					else:
						nprob+=bigramn[biword]
				nindex+=1
	#				print PPW[word+'\n']
	#				print PNW[word+'\n']

	
			if ans==0 and nprob>pprob:
				tn+=1
			if ans==0 and nprob<pprob:
				fp+=1
			if ans==1 and pprob>nprob:
				tp+=1
			if ans==1 and pprob<nprob:
				fn+=1
	
	accuracy = (float (tp+tn))/ line_count
#	print accuracy
	sum_of_accuracy+=accuracy
	testing_no-=1
avg_accuracy = sum_of_accuracy * 10
print avg_accuracy
		
	
