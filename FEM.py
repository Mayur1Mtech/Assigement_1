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
        while True:
            with open(self.file1, 'a') as f1, open(self.file2, 'a') as f2:
                if random.random() > 0.5:
                    f1.write("MARUTI ")
                    self.count1 += 1
                else:
                    f1.write(random_string(8) + " ")
                if random.random() > 0.5:
                    f2.write("MARUTI ")
                    self.count2 += 1
                else:
                    f2.write(random_string(8) + " ")
            await asyncio.sleep(1)

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

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

monitor = FileMonitor("file1.txt", "file2.txt", "counts.log")
monitor.start()

