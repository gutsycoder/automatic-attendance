from notify_run import Notify
import time
notify=Notify()
notify.register()
print(notify.info())
while(True):
    
    
    notify.send("Hello World ")
    time.sleep(10)
