import neuralnet

from random import choice, sample,randrange


myname = "kate" # Name used to adress the program 
lib = set() # Tuples of (response,sender) sent to the program
n = 100

# Add the response to the library
def put(response):
    lib.add(response)

# Get some response from the library
def get(recipient,respondence):
    global n
    if randrange(1,n) < 5:
        response = sample(lib,1)[0]
    else:
        response = max(lib,key=(lambda x: neuralnet.rate(respondence,x)))
    n += 1
    return response.replace("$MYNAME$",myname).replace("$THEIRNAME$",recipient)

def study(path,amount=None):
    with open(path) as file:
        lines = file.read().splitlines()
        lib.add(lines[0])
        pairs = zip(lines[:-1],lines[1:])
        for i,(message,response) in enumerate(pairs):
            if i % 1000 == 0:
                print(str(i) + '/' + str(len(lines)-1))
            if amount is not None and i > amount:
                return
            lib.add(response)
            neuralnet.note(message.lower(),response.lower())

message = "$START$"
theirname = input("What is your name? ").lower()
while True:
    print(">",end = " ")
    response = input()
    response = response.lower()
    response = response.replace(theirname,"$MYNAME$")
    response = response.replace(myname,"$THEIRNAME$")
    put(response)
    neuralnet.note(message,response)
    message = get(theirname,response)
    print(message)
