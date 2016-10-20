import os, re
from nltk.corpus import stopwords
from nltk.corpus import words

# stackoverflow
regex = re.compile('[^a-zA-Z]')
count = 0
myDict = set()
badwords = ['the','be','to','of','and','a','in','that','have','i','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','no','just','him','know','take','people','into','year','your','good','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us']
stop = list(set(stopwords.words('english')))
englishwords = words.words()
badwords = badwords + stop
badwords = set(badwords)
englishwords = set(englishwords)

print len(englishwords)
print len(list(set(englishwords)))
for id,filename in enumerate(os.listdir(os.getcwd()+'/data')):
	print id
	tempFile = open('./data/'+filename)
	words =  map( lambda x: regex.sub('',x.strip().lower()), tempFile.read().split())
	for word in words: 
		if not( word in badwords or word in myDict) and word in englishwords:
			myDict.add(word)
	tempFile.close()

print 'done building dictionary, now saving...'
dictFile = open('dictionary','w')
dictFile.write(repr(myDict))
print myDict
print "LENGTH OF DICTIONARY: ",
print len(myDict)
dictFile.close()
print 'done'

"""
	things to count
	1. number of docs per classification
	2. for each classification get, probability of a word -> probability table
"""
types = ['comp.graphics', 'sci.med', 'comp.sys.mac.hardware', 'talk.politics.misc', 'soc.religion.christian', 'rec.motorcycles', 'talk.religion.misc', 'comp.windows.x', 'comp.sys.ibm.pc.hardware', 'talk.politics.guns', 'talk.politics.mideast', 'sci.crypt', 'misc.forsale', 'sci.space', 'alt.atheism', 'rec.sport.hockey', 'rec.sport.baseball', 'sci.electronics', 'comp.os.ms-windows.misc', 'rec.autos']
