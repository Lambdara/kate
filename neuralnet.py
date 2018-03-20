from re import sub

net = dict() # Keep track of how often `word1 in message` implies `word2 in response` as (word1,word2,freq)

regexFilter = "[^(\w|\$|\')]" # What has to be filtered in the messages

# Add a word to the net
def put(word):
    if word not in net.keys():
        net[word] = dict()
        for w in net.keys():
            net[w][word] = 0
            net[word][w] = 0
        net[word][word] = 0

# Save the data of one message-response pair
def note(message,response):
    # Convert both to list of words
    message = sub(regexFilter, " ",  message.lower()).split()
    response = sub(regexFilter, " ", response.lower()).split()

    if message == [] or response == []:
        return

    # make sure they are all in net:
    for word in message:
        put(word)
    for word in response:
        put(word)

    for word1 in message:
        for word2 in response:
            net[word1][word2] += 1

class Counter(dict):
    def __missing__(self, key):
        return 0
    
def rate (message, response):
    # message to wordlist
    message = sub(regexFilter, " ",  message.lower()).split()
    response = sub(regexFilter, " ", response.lower()).split()

    if message == [] or response == []:
        return 0
    
    if len(response) == 0:
        print(response)

    # rate
    score = 0
    for word1 in message:
        for word2 in response:
            score += net[word1][word2]
    score /= len(response)


    return score
