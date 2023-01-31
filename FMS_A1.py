import asyncio
import random
import string
import logging
import aiofiles

logging.basicConfig(filename="newfile.log",
                    format='[%(asctime)s] - %(message)s',
                    filemode='a',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

class RandomWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    async def string_generator(self):
        k = random.randint(10, 20)
        rand_string = ''.join(random.choices(string.ascii_letters, k=k))
        mylist = [rand_string, "MARUTI"]
        return random.choice(mylist)

    async def write_to_file(self):
        while True:
            try:
                string_to_write = await self.string_generator()
                async with aiofiles.open(self.file_name, 'a') as file:
                    await file.write(string_to_write + '\n')
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"Error writing to file {self.file_name}: {e}")
                break

async def monitor_files(files):
    while True:
        await asyncio.sleep(10)
        for file in files:
            try:
                async with aiofiles.open(file, "r") as f:
                    content = await f.read()
                    count = content.count("MARUTI")
                    logger.info(f"MARUTI count in file {file}: {count}")
            except Exception as e:
                logger.error(f"Error reading file {file}: {e}")

async def main():
    writer1 = RandomWriter("file1.txt")
    writer2 = RandomWriter("file2.txt")
    await asyncio.gather(
        writer1.write_to_file(),
        writer2.write_to_file(),
        monitor_files(["file1.txt", "file2.txt"])
    )

try:
    asyncio.run(main())
except Exception as e:
    logger.error(f"Error in main function: {e}")
