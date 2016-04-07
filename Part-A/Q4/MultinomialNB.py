import pickle
#Opening vocabulary and getting count of the words in the vocabulary.
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
ncount=0
negative=0
with open ("RefinedData.txt","r") as fin2:
	for line in fin2:
		if line[0]=='+':
			for word in line.split():
				word+= '\n'
				pcount+=1
				if word not in PWcount:
					print word
					PWcount[word]=0	
				PWcount[word]= PWcount[word]+1
#				print PWcount[word]
			pcount-=1
			positive+=1
		else:
			for word in line.split():
				word+= '\n'
				ncount+=1
				if word not in NWcount:
					NWcount[word]= 0
				NWcount[word]= NWcount[word] + 1
			ncount-=1
			negative+=1

total=positive+negative
Ppositive=float(positive)/total
Pnegative=float(negative)/total
#print PWcount
FinalList=[]
with open ("Vocabulary.txt","r") as fin3:
	for word in fin3:
		if word not in PWcount:
			print word
			PWcount[word]=0	
		if word not in NWcount:
			NWcount[word]=0	
#		print NWcount[word]
#		print PWcount[word]
		PPW[word]= float(PWcount[word]+1)/float(pcount+vcount)
		PNW[word]= float(NWcount[word]+1)/float(ncount+vcount)
		FinalList.append("Word: %s  PositiveProbability: %f  NegativeProbability: %f" %(word,PPW[word],PNW[word]))



file_name= "MultinomialNB"
file_object=open(file_name,'wb')
pickle.dump(FinalList,file_object)
file_object.close()
