import asyncio
import random
import string
import os
import time

class FileMonitor:
    def __init__(self, file1, file2, logfile):
        self.file1 = file1
        self.file2 = file2
        self.logfile = logfile
        self.count1 = 0
        self.count2 = 0

    async def random_writer(self):
        with open(self.file1, 'a') as f1, open(self.file2, 'a') as f2:
            while True:
                f1.write(string_generater)
                self.count1 += 1
                f2.write(string_generater)
                self.count2 += 1
                await asyncio.sleep(1)
                print("done")

    async def monitor(self):
        while True:
            with open(self.logfile, "a") as log:
                log.write("File1: " + str(self.count1) + " File2: " + str(self.count2) + " at " + time.ctime() + "\n")
            await asyncio.sleep(10)

    def start(self):
        try:
            loop = asyncio.get_event_loop()
            loop.create_task(self.random_writer())
            loop.create_task(self.monitor())
            loop.run_forever()
        except KeyboardInterrupt:
            print("Monitoring system stopped.")

def random_string():
    len = random.choice(string.digits)
    length = int(len)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
#print(random_string())

def string_generater():
    mylist = [random_string(),"MARUTI"]
    return random.choices(mylist, weights=[50,50], k=1)
string_generater=str(string_generater())

monitor = FileMonitor("/home/mayur/Desktop/Demo_Folder/file1.txt", "/home/mayur/Desktop/Demo_Folder/file2.txt",
                      "/home/mayur/Desktop/Demo_Folder/counts.log")
monitor.start()
