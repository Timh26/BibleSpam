
try:
	from collections import defaultdict
	import re,time,glob,os
	import pickle as pickle
except ImportError:
	print("Import error. Make sure you have the required libraries!")
	raise SystemExit



os.chdir('./sources') #load up list of sourcefiles. 
sources = glob.glob('*.txt')
for idx in range(len(sources)):
	sources[idx] = sources[idx].split(".")[0]
print (sources)

defdict = defaultdict(list)
for source in sources:
	with open(str(source)+'.txt') as f: 
		print(source)
		words = re.findall("[\w'.!?]+",f.read())
		print("Generating...")
		for num in range(10):
			print(words[num]) 
		for idx in range(0,len(words)-2):
			word1 = words[idx].lower().replace("\n",' ').replace(' ','')
			word2 = words[idx+1].lower().replace("\n",' ').replace(' ','')
			word3 = words[idx+2].lower().replace("\n",' ').replace(' ','')
			defdict[word1+'<>'+word2].append(word3)
		print("Done Generating")
		pickle.dump(defdict,open(str(source)+"wordDictionary.mch","wb"))
		print("Word dictionary written.")
		f.close()