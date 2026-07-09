import asyncio
async def task(name):
    await asyncio.sleep(1)
    print(name)
asyncio.run(task("A"))







import asyncio
async def print_line(name):
    await asyncio.sleep(3)
    print(name)
asyncio.run(print_line("raju"))