#Name: Michael
#Supervisor: Rex Ben
import time
import random
import webbrowser

while True:
    websites=random.choice(["google.com","python.org","facebook.com","apple.com","revdl.com","o2tvseries.com","wattpad.com","waptrick.com"])
    go_to="http://()".format(websites)
    webbrowser.open(go_to)
    seconds_intervals=random.randrange(5,20)
    time.sleep(seconds_intervals)
