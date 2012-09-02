import twitter, string, os

# Twitter checker, a simple tool for check a keyword in the tweet of an user that you like. Maded by @Armax for stalkering Farenz xD
# Attenzione il tool è fatto come "esercizio di programmazione e credo possa essere utile a qualcuno che voglia imparare 
# ad usare i moduli di twitter su python... per quello ho deciso di pubblicarlo non credo ci sia qualcuno davvero 
# interessato a controllare giorno e notte farenz... per gli altri spero che tutto quello che cercate sui moduli di 
# twitter possiate trovarlo qua sotto forma di esempio altrimenti cercate sul sito di googlecode che trovere te 
# sicuramente delle documentazioni più dettagliate"
# Come potete notare ho commentato anche le cose più banali in modo che sia un aiuto per tutti 


api = twitter.Api()
print "Resetting twitter timeline..." 
os.system("rm tweet.txt")
os.system("touch tweet.txt")

#Apre il file in cui vengono inseriti i tweet"
tweet = open('tweet.txt', 'a+')

#Utente di cui viene controllata la timeline
user = "AngoloDiFarenz"

#Lista di parole che vengono controllate
keyword = ["Mare", "Aperitivo"]

#Controllo della timeline apt.GetUserTimeline(user) ottiene la timeline dell'utente specificato
#tweet.write scrive i tweet nel file specificato sopra con tweet = open('tweet.txt', 'a+')
print "[i] Checking twitter timeline..."
statuses = api.GetUserTimeline(user)
listtweet = [s.text for s in statuses]
tweet.write(str(listtweet))
tweet.close()

print
print "[i] Import the tweets in a list and split them..."

print "[i] Checking if the user use a keyword in the list..."
start = raw_input("Press any key to start the scanning...")

#Apriamo il file tweet.txt in sola lettura
tweet = open('tweet.txt', 'r')
#Splittiamo il file in modo che ogni parola divisa da uno spazio venga salvata per se nella lista
tw = tweet.read().split(" ")

#Mostriamo le keyword inserite nella lista
i = 0

while i < len(keyword):
  print "	" + keyword[i]
  i = i + 1
print

#Stariamo il while che controllerà le keyword
i = 0
used = 0
#Selezioniamo la prima keyword della lista
while i < len(keyword):
  f = 0
  #Startiamo un'altro while che sceglierà invece le parole dei tweet splittate precedentemente
  while f < len(tw):
    #Controlliamo se la keyword corrisponde alla parola 	
    if keyword[i] == tw[f]:
	print "[!] " + user + " used the keyword " + keyword[i]
	used = used + 1 
	#se si procediamo aumentando di uno il conto (used = used + 1) in maniera che venga cambiata la parola da controllare
	f = f + 1 
    else: 
    	f = f + 1
 	#la keyword non corrisponde alla parola printiamo niente e procediamo
  #while sopra finito vuol dire che tutte le parole sono state controllate con la keyword scelta	
  i = i + 1
  #Aggiungiamo 1 al conto del primo while in modo che cambi la keyword e ricominci
  
print 
print "User selected use " + str(used) + " totally keywords"
