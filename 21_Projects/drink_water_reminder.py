import time
from plyer import notification
while True:
    print("Please sip some Water!")
    notification.notify(title="Please drink water",message="You need to drink some water")
    time.sleep(60*60)