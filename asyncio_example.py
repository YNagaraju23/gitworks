import asyncio
async def task(name):
    await asyncio.sleep(1)
    print(name)
asyncio.run(task("A"))

<<<<<<< HEAD
=======
import asyncio
async def task(name):
    await asyncio.sleep(1)
    print(name)
asyncio.run(task("a"))


>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03






import asyncio
async def print_line(name):
    await asyncio.sleep(3)
    print(name)
<<<<<<< HEAD
asyncio.run(print_line("raju"))


import asyncio
async def task(a):
    await asyncio.sleep(10)
    print(a)

asyncio.run(task("raju"))
=======
asyncio.run(print_line("raju"))
>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03
