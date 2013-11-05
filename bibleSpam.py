try:
	from collections import defaultdict
	import random,re,time
	from twitter import Twitter, OAuth
except ImportError:
	print("Import error. Make sure you have python-twitter!")
	raise SystemExit

d2= defaultdict(list)
f=open('Bible Text2.txt')
words = re.findall("[\w'.!?]+",f.read())

# Connecting to twitter
twit = Twitter(auth = OAuth("OAUTH_TOKEN", "OAUTH_SECRET","CONSUMER_KEY", "CONSUMER_SECRET")) #You'll need to get an OAuth key at http://dev.twitter.com/


#Generating the markov chain
print("Generating...")
for idx in range(0,len(words)-2):
	word1 = words[idx].lower().replace("\n",' ').replace(' ','')
	word2 = words[idx+1].lower().replace("\n",' ').replace(' ','')
	word3 = words[idx+2].lower().replace("\n",' ').replace(' ','')
	d2[word1+'<>'+word2].append(word3)
print("Done Generating")

#putting out the tweets
outstring = ''
tweetcount = 0
while (True):
	outstring = ''
	while (len(outstring)>140) or (len(outstring)<50):
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
	print(outstring+"\n")
	print("Success!")
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
f.close()
