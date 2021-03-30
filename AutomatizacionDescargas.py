from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler as Fh

import os
import json
import time


class MyHandler(Fh):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            if "jpg" in str(filename) and "crdownload" not in str(filename):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
                print("Succesfully moved!")

if os.path.exists("Desktop/images") == False:
    os.chdir("Desktop/")
    os.mkdir("images")
else:
    print("Ya tiene la carpeta")

folder_to_track = "../Downloads"
folder_destination = "../Desktop/images"

handler = MyHandler()
observer = Observer()
observer.schedule(handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()



