no_of_lines_read = 0
file_no = 1
with open ("RandomizedData.txt","r") as fin:
	for line in fin:
		if no_of_lines_read> 468:
			with open ("file10.txt", "a") as fout10:
				fout10.write(line)
		elif no_of_lines_read > 416:
			with open ("file9.txt", "a") as fout9:
				fout9.write(line)
		elif no_of_lines_read > 364:
			with open ("file8.txt", "a") as fout8:
				fout8.write(line)
		elif no_of_lines_read > 312:
			with open ("file7.txt", "a") as fout7:
				fout7.write(line)
		elif no_of_lines_read > 260:
			with open ("file6.txt", "a") as fout6:
				fout6.write(line)
		elif no_of_lines_read > 208:
			with open ("file5.txt", "a") as fout5:
				fout5.write(line)
		elif no_of_lines_read > 156:
			with open ("file4.txt", "a") as fout4:
				fout4.write(line)
		elif no_of_lines_read > 104:
			with open ("file3.txt", "a") as fout3:
				fout3.write(line)
		elif no_of_lines_read >=52:
			with open ("file2.txt", "a") as fout2:
				fout2.write(line)
		else:
			with open ("file1.txt", "a") as fout1:
				fout1.write(line)
		no_of_lines_read+=1
