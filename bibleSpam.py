try:
	from collections import defaultdict
	import random,re,time,glob,os
	from twitter import Twitter, OAuth
	import pickle as pickle
except ImportError:
	print("Import error. Make sure you have the required libraries!")
	raise SystemExit

TESTING = True
with open('twitter.oauth') as OA: # the OAuth file should contain the OAuth token, OAuth secret, Consumer key, and Consumer secret, in that order, on separate lines.
	keys = OA.readlines()
	OAUTH_TOKEN = keys[0].replace("\n","")
	OAUTH_SECRET = keys[1].replace("\n","")
	CONSUMER_KEY = keys[2].replace("\n","")
	CONSUMER_SECRET = keys[3].replace("\n","")
print(keys)
#Connecting to twitter
try:
	twit = Twitter(auth = OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY, CONSUMER_SECRET)) #You'll need to get an OAuth key at http://dev.twitter.com/	
except Exception:
	print("Twitter connection error.")
	raise SystemExit


os.chdir('./sources') #load up list of sourcefiles. 
sources = glob.glob('*.txt')
for idx in range(len(sources)):
	sources[idx] = sources[idx].split(".")[0]
print (sources)
#putting out the tweets
outstring = ''
tweetcount = 0
while (True):
	currFile = random.choice(sources)
	sig = " - not "+str(currFile)
	print(currFile)
	with open(currFile+"wordDictionary.mch",'rb') as pkl:
		d2 = pickle.load(pkl)
	outstring = ''
	while (len(outstring)+len(sig)>140) or (len(outstring)<50):
		
		print("trying\n")
		p = random.choice(list(d2.keys())).split('<>')#choose a random word pair
		w1 = p[0]
		w2 = p[1]
		w3 = random.choice(d2[w1+'<>'+w2])
		wcount = 0
		stay = True
		cap = True
		outstring = ""
		while(stay):
			wcount +=1
			if cap:
				w3 = w3.capitalize()
			if ('.' in w3 or '?' in w3 or '!' in w3):
				cap = True
				if (wcount>2):
					stay=False
			else:
				cap = False
			# print(w3,end=" ")
			outstring += w3
			outstring +=" "
			w1=w2
			w2=w3.lower()
			w3 = random.choice(d2[w1+'<>'+w2])
	outstring += sig
	print(outstring+"\n")
	print("Success!")
	if(not TESTING):
		try:
			twit.statuses.update(status = outstring)
			tweetcount+=1
			print("Tweet #"+str(tweetcount))
			time.sleep(10)
		except Exception as e:
			print("EXCEPTION RAISED: ",e)
		for x in range(1,90):
			time.sleep(60)
			print(str(90-x)+" minutes until next tweet.")
	time.sleep(2)
	d2= 0
	pkl.close()
