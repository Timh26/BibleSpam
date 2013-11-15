from nltk.corpus import brown
from collections import defaultdict
import random,re,time
import cPickle as pickle #faster pickler written in c. Improves pickling/unpickling by about 4-5x

wChain= defaultdict(list)
posDict = defaultdict(list)
totSen = 0
totWds = 0

varin = raw_input("Rebuild dictionaries?(Y/N): ").lower()

avail = True
if(varin == 'n'):
        try:
                sTime = time.time()
                wChain =pickle.load( open("wordDictionary.mch","rb"))#using *.mch to represent a pickled markov chain
                print("Words chain loaded from wordDictionary.mch")
                print(time.time()-sTime)
                sTime = time.time()
                posDict = pickle.load( open("posDictionary.mch","rb"))
                print("Part of speech chain loaded from posDictionary.mch")
                print(time.time()-sTime)
        except Exception, e:
                print("Error: "+str(e))
                print("Couldn't load dictionary.")
                avail = False
if(not avail or varin == 'y'):
        print("Generating now.")
        sents = brown.tagged_sents(simplify_tags=True)
        print("Corpus loaded.")
        totSen = len(sents)
        for sentence in sents:
                totWds += len(sentence)
                for i in range(0,len(sentence)-1):
                        (word1,tag1) = sentence[i]
                        (word2,tag2) = sentence[i+1]
                        wChain[word1].append(word2)
                        posDict[tag1].append(tag2)
        pickle.dump(wChain,open("wordDictionary.mch","wb"))
        print("Words chain written to wordDictionary.mch")
        pickle.dump(posDict,open("posDictionary.mch","wb"))
        print("Part of speech chain written to posDictionary.mch")
        print("Average sentence length: "+str(totWds//totSen))

