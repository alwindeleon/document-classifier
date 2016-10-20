import os, re
from decimal import *

# stackoverflow
regex = re.compile('[^a-zA-Z]')

# get dictionary
myDictFile = open('dictionary')
myDict = eval( myDictFile.read() )
myDictFile.close()

# constant/s
LAMBDA = 0.1
lengthDataset = 18846
types = ['comp.graphics', 'sci.med', 'comp.sys.mac.hardware', 'talk.politics.misc', 'soc.religion.christian', 'rec.motorcycles', 'talk.religion.misc', 'comp.windows.x', 'comp.sys.ibm.pc.hardware', 'talk.politics.guns', 'talk.politics.mideast', 'sci.crypt', 'misc.forsale', 'sci.space', 'alt.atheism', 'rec.sport.hockey', 'rec.sport.baseball', 'sci.electronics', 'comp.os.ms-windows.misc', 'rec.autos']


# helper functions
def getFeatureVector(dict, doc):
	featureVector = [0 for i in range(len(dict))]
	processedDoc = docToSet(doc)

	for ind,word in enumerate(dict):
		if word in processedDoc:
			featureVector[ind] = 1
	return featureVector

def docToSet(doc):
	rawText = doc.split()
	text = set(map(lambda x: regex.sub('',x.strip().lower()), rawText))
	return text

def computeNbNumerator(featureVector, classification, probabilityTable, probabilityPerClassification, currentArgMax):
	biggerThanArgmax = True;
	classInd = types.index(classification)
	probability = probabilityPerClassification[ classInd ]
	for ind,wordPresence in enumerate(featureVector) :
		if ( currentArgMax == None or probability > currentArgMax ):
			if (wordPresence == True):
				probabilityOfWord = probabilityTable[types.index(classification)][ind]
				probability *= probabilityOfWord
			else:
				probabilityOfWord = 1-probabilityTable[types.index(classification)][ind]
				probability *= probabilityOfWord
		else:
			return [False, 0]
	return [True, probability]
	
	# return [bool, value(Decimal)] bool is true if bigger than argmax, otherwise false
# get indexing of dataset
indexFile = open('index');
index = map(lambda x: x.split()[1], indexFile.read().splitlines())
numPerType = [0 for i in xrange(20)]



# # compute for probability table   # up to 60%
# arrNumPerClassification = [0 for i in xrange(20)] #length 20 
# arrContainsWordsPerClassification = [[0 for i in xrange(len(myDict))] for j in xrange(20)]

# for id,filename in enumerate(os.listdir(os.getcwd()+'/data')):
# 	if(id > 11308):
# 		continue
# 	print id
# 	tempFile = open('./data/'+filename)
# 	rawText = tempFile.read().split()
# 	text = map(lambda x: regex.sub('',x.strip().lower()), rawText)
# 	text = set(text) #optimization 
# 	classificationIndex = types.index(index[int(filename)])
# 	numPerType[classificationIndex] +=1
# 	for wordIndex,word in enumerate(myDict):
# 		if word in text:
# 			arrContainsWordsPerClassification[classificationIndex][wordIndex]+=1
# 	tempFile.close()
# print numPerType
# # save values
# rawTableFile = open('table',"w")
# rawTableFile.write(repr(arrContainsWordsPerClassification))
# rawTableFile.close()


# # get and solve actual probabilitytable
# probabilityTable = arrContainsWordsPerClassification
# for rowIndex in xrange(len(probabilityTable)):
# 	probabilityTable[rowIndex] = map(lambda num: Decimal(num+LAMBDA) / Decimal(numPerType[rowIndex] + LAMBDA), probabilityTable[rowIndex] )
# # get probability per classification
# probabilityPerClassification = []
# for num in numPerType:
# 	probabilityPerClassification.append(Decimal(num)/lengthDataset)

# print probabilityPerClassification

# # save values
# probabilityTableFile = open('probability',"w")
# probabilityTableFile.write(repr(probabilityTable))
# probabilityTableFile.close()
# probabilityPerClassificationFile = open('probability_class','w')
# probabilityPerClassificationFile.write(repr(probabilityPerClassification))
# probabilityPerClassificationFile.close()



# alternate
probabilityTableFile = open('probability')
probabilityTable = eval( probabilityTableFile.read() )
probabilityTableFile.close()
probabilityPerClassificationFile = open('probability_class')
probabilityPerClassification = eval( probabilityPerClassificationFile.read() )
probabilityPerClassificationFile.close()

NUMBER_OF_CORRECT = 0
TOTAL = 0
for id,filename in enumerate(os.listdir(os.getcwd()+'/data')):
	if(id < 11308):
		continue
	print "CURRENT FILE CHECKING FOR PROBABILITY: ",
	print id
	tempFile = open('./data/'+filename)
	rawText = tempFile.read()
	tempFeatureVector = getFeatureVector(myDict, rawText)
	argmax = None
	argmaxClass = None
	for ind,classification in enumerate(types):
		result = computeNbNumerator(tempFeatureVector, classification, probabilityTable, probabilityPerClassification, argmax)
		if(result[0] == True):
			argmax = result[1]
			argmaxClass = classification
	if(argmaxClass == index[id]):
		NUMBER_OF_CORRECT+=1
	TOTAL += 1
	print "CORRECT: ",
	print NUMBER_OF_CORRECT
	print "TOTAL: ",
	print TOTAL
	print "current accuracy: ",
	print Decimal(NUMBER_OF_CORRECT)/TOTAL

print "CORRECT: ",
print NUMBER_OF_CORRECT
print "TOTAL: ",
print TOTAL
