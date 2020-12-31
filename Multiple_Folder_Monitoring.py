import sys
import time
import logging
import multiprocessing
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

event_handler = LoggingEventHandler()
observer=Observer()

folder="C:/Users/My/Desktop/Py"
folder1="C:/Users/My/Desktop/C and C++"

def monitor(folder):
    logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(message)s',datefmt='%Y-%m-%d %H:%H:%S')
    observer.schedule(event_handler,folder,recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__=="__main__":
    m=multiprocessing.Process(target=monitor,args=(folder,))
    m1=multiprocessing.Process(target=monitor,args=(folder1,))
    m.start()
    m1.start()
