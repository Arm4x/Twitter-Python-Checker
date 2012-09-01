import twitter, string, os

#Twitter checker, a simple tool for check a keyword in the tweet of an user that you like. Maded by @Armax for stalkering Farenz xD
#Attenzione il tool è fatto come "esercizio di programmazione e credo possa essere utile a qualcuno che voglia imparare ad usare i moduli di twitter su python... per quello ho deciso di pubblicarlo non credo ci sia qualcuno davvero interessato a controllare giorno e notte farenz... per gli altri spero che tutto quello che cercate sui moduli di twitter possiate trovarlo qua sotto forma di esempio altrimenti cercate sul sito di googlecode che trovere te sicuramente delle documentazioni più dettagliate"

api = twitter.Api()
print "Resetting twitter timeline..." 
os.system("rm tweet.txt")
os.system("touch tweet.txt")

#Apre il file in cui vengono inseriti i tweet"
tweet = open('tweet.txt', 'a+')


user = "AngoloDiFarenz"

keyword = ["Mare", "Aperitivo"]

print "[i] Checking twitter timeline..."
statuses = api.GetUserTimeline(user)
listtweet = [s.text for s in statuses]
tweet.write(str(listtweet))
tweet.close()

print
print "[i] Import the tweets in a list and split them..."

print "[i] Checking if the user use a keyword in the list..."
start = raw_input("Press any key to start the scanning...")

tweet = open('tweet.txt', 'r')
tw = tweet.read().split(" ")

i = 0
while i < len(keyword):
  print "	" + keyword[i]
  i = i + 1
print

i = 0
used = 0
while i < len(keyword):
  f = 0
  
  while f < len(tw):
    if keyword[i] == tw[f]:
	print "[!] " + user + " used the keyword " + keyword[i]
	used = used + 1 
	f = f + 1 
    else: 
    	f = f + 1
 		
  i = i + 1

print 
print "User selected use " + str(used) + " totally keywords"
