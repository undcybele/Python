import time
import random
options = ["uhmmm, mby not", "cu voia lui dzeu - da","u wish bro","nope", "gurl, wake up", "mayhaps", "mayhaps:)", "ye pretty much", "oh yes. definitely", "yes!", "not sure"]
y = 0
while y == 0 :
    input("Ask me something>> ")
    print('thinking...')
    time.sleep(3.5)
    x = random.randrange(len(options))
    print(options[x])
    y = int(input("--would u wanna go again? yes = 0, no = 1\n"))
    if y == 1:
        print("Ok bye heathen")
        break
    else: continue