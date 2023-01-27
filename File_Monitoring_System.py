import asyncio
import random
import string
import os
import aiofiles


class RandomWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.maruti_count = 0

    async def write_to_file(self):
        while True:
            try:
                if random.random() > 0.5:
                    rand_string = 'MARUTI'
                    self.maruti_count += 1
                else:
                    k = random.randint(10,20)
                    rand_string = ''.join(random.choices(string.ascii_letters,k=k))
                async with aiofiles.open(self.file_name, 'a') as file:
                    await file.write(rand_string + '\n')
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Error writing to file {self.file_name}: {e}")
                break

async def monitor_files():
    writer1 = RandomWriter("file5.txt")
    writer2 = RandomWriter("file6.txt")
    await asyncio.gather(writer1.write_to_file(), writer2.write_to_file())
    while True:
        await asyncio.sleep(10)
        with open("counts.log2", "a") as count_file:
            count_file.write(f"File1: {writer1.maruti_count}, File2: {writer2.maruti_count}\n")
try:
    asyncio.run(monitor_files())
except Exception as e:
    print(f"Error in main function: {e}")
