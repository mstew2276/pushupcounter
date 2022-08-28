import random
from time import sleep

pushup = random.randint (5, 50)
print("Alright time to get off your ass the amount of pushups you will do is", pushup)

if pushup < 20:
    print("Guess it's your lucky day")
    sleep(4)
else:
    print("Lucky you, you get to do a lot of pushups")
    sleep(4)

print("IN PUSHUP POSITION!")
sleep(10)

count = 1
while True:
    if count < pushup:
        print("DOWN!")
        sleep(3)
        print("UP!")
        sleep(3)
        if count == pushup:
            print("Well done I look forward to seeing you next time")
            break
        count += 1
