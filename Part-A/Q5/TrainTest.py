
from math import log
#Opening vocabulary and getting count of the words in the vocabulary.
vcount=0
PWcount={}
NWcount={}
PPW={}
PNW={}
sum_of_accuracy = 0
with open ("Vocabulary.txt","r") as fin:
	for word in fin:
		vcount+=1;
#print vcount

#Getting the priors, ie, Probability that a given comment is +ve/-ve
positive=0
pcount=0
ncount=0
negative=0
no_of_lines_read = 0

#	Reading from 9 files and testing the 10th 
string1 = "file"
string2= ".txt"
testing_no = 10

#							Training
while testing_no!=0:
	no=1
	while no!=testing_no:
		with open (string1+str(no)+string2,"r") as fin1:
			for line in fin1:
				if line[0]=='+':
					for word in line.split():
						word+= '\n'
						pcount+=1
						if word not in PWcount:
	#						print word
							PWcount[word]=0	
						PWcount[word]= PWcount[word]+1
	#					print PWcount[word]
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
		no+=1

	total=positive+negative
	Ppositive=log(float(positive)/total)
	Pnegative=log(float(negative)/total)
	#print PWcount
#								Testing
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
	
	ans = 0 
	tp=0
	tn=0
	fp=0
	fn=0
	line_count = 0
	with open (string1+str(testing_no)+string2,"r") as fin4:
		for line in fin4:
			line_count+=1
			pprob = float (Ppositive)
			nprob = float (Pnegative)
	#		print line
			for word in line.split():
				if word =='+' or word == '-': 
					if word == '+':
						ans = 1
					else:
						ans = 0
				else:
					if word+'\n' not in PPW:
						PPW[word+'\n']=1
					if word+'\n' not in PNW:
						PNW[word+'\n']=1
	#				print PPW[word+'\n']
	#				print PNW[word+'\n']
					pprob+=PPW[word+'\n']
					nprob+=PNW[word+'\n']
	
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
