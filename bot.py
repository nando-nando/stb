from twython import Twython
import random
import time


def get_kiss(): #these phrases go at the end of messages
    """
    Randomly pick a phrase for the homies
    """
    
    k = ["Mwah",
        "BESITO",
        "KISS KISS KISS",
        "XXX", 
        "BESO!",
        "smooch", 
        "smooch smooch", 
        "Homie love is the best type of love",
         "kith",
         "I look at the stars and then your lips, oh man you need a KISS!",
         "I give beso now you give me beso",
         "Here's your beso",
         "You are loved",
         "I hope your day gets better",
         ";)",
         "Beijos",
         "I love you", 
         "I've always wanted this",
         "Love you boo", 
         "Damn you be outchea cheecked up, TODAY? TODAY!!!??!", 
         ":p"
        ]
    
    lower_bound = 0
    upper_bound = len(k) - 1
    rKiss = random.randint(lower_bound, upper_bound)
    
    return k[rKiss]


def getLastId(file):
    """
    Get id in file specified
    """
    readFile = open(file, "r")
    lastId = int(readFile.read().strip())
    readFile.close()

    return lastId


def storeLastId(idNumber, file):
    """
    Stores id in file specified
    """
    writeFile = open(file, "w")
    writeFile.write(str(idNumber))
    writeFile.close()
    
    return True


def getApiKeys(file): 
    """
    Read in access keys from file
    """
    file = open(file, "r")
    a = file.read().split("\n")
    
    API_KEY = a[0]
    API_KEY_SECRET = a[1]
    ACCESS_TOKEN = a[2]
    ACCESS_TOKEN_SECRET = a[3]
    
    file.close()
    return API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

getApiKeys("keys.txt")



try:
    time.sleep(1)
    twitter = Twython(getApiKeys("keys.txt")[0], getApiKeys("keys.txt")[1], getApiKeys("keys.txt")[2], getApiKeys("keys.txt")[3])
    dms = twitter.get_direct_messages()["events"]
    
except: 
    print("Dms cannot be pulled at this moment")


pullId = []
pullTxt = []


for x in range(len(dms)):
    
    anId = dms[x]["id"]
    someTxt = dms[x]["message_create"]["message_data"]["text"]
    
    pullId.append(anId) 
    pullTxt.append(someTxt)


for x in range(len(pullTxt)):
    
    pullTxt[x] = pullTxt[x].split(" ")[0]


for x in range(len(pullId)):

    if pullTxt[x][0] == "@":
    
        if int(pullId[x]) != getLastId("id.txt"):
            print(pullId[x])
            print(pullTxt[x])
            
            time.sleep(7)
            twitter.update_status(status = (pullTxt[x] + " your homie sent you a gn kiss; " +  get_kiss()))
            
        else:
            break
    
    else:
        break
        
storeLastId(pullId[0], "id.txt")
