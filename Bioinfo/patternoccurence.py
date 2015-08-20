#Finds the index where a pattern appears in a string
def patternOccurence(pattern, genome):
	stIndex = ""
	patLength = len(pattern)
	
	for i in range(len(genome) - len(pattern)):
		if genome[i: i + patLength] == pattern[0:patLength]:
			stIndex += str(i) + " "

	return stIndex

'''
pat = "ATAT"
gen = "GATATATGCATATACTT"
#1 3 9 
print(patternOccurence(pat,gen))

pat = "CTTGATCAT"
#1 3 9 
print(patternOccurence(pat,gen))
'''