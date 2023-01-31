import asyncio
import random
import string
import os
import aiofiles


class RandomWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.maruti_count = 0

    async def string_generater(self):
        k = random.randint(10, 20)
        rand_string = ''.join(random.choices(string.ascii_letters, k=k))
        mylist = [rand_string, "MARUTI"]
        return random.choices(mylist,weights=[50,50],k=1)[0]

    async def write_to_file(self):
        while True:
            try:
                string_generater = await self.string_generater()
                async with aiofiles.open(self.file_name, 'a') as file:
                    await file.write(string_generater + '\n')
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Error writing to file {self.file_name}: {e}")
                break
                

async def monitor_files(writers):
    while True:
        await asyncio.sleep(10)
        for writer in writers:
            async with aiofiles.open(writer.file_name, "r") as file:
                content = await file.read()
                writer.maruti_count = content.count("MARUTI")
        async with aiofiles.open("counts.log", "a") as count_file:
            counts = [f"File{i}: {writer.maruti_count}" for i, writer in enumerate(writers, 1)]
            await count_file.write(", ".join(counts) + "\n")


async def main():
    writer1 = RandomWriter("file1.txt")
    writer2 = RandomWriter("file2.txt")
    await asyncio.gather(writer1.write_to_file(), writer2.write_to_file(), monitor_files([writer1, writer2]))


try:
    asyncio.run(main())
except Exception as e:
    print(f"Error in main function: {e}")
