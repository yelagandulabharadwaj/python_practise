# import asyncio

# async def func1():
#     task=asyncio.create_task(func2())
#     print('func1 one')
#     await asyncio.sleep(1)
#     print('func1 two')
#     await asyncio.sleep(2)

# async def func2():
#     print('func2 one ')
#     await asyncio.sleep(1)
#     print('func2 two')


# asyncio.run(func1())


import asyncio 

async def task2():
    print('t2 one')
    await asyncio.sleep(1)
    print('t2 two')
    await asyncio.sleep(1)


async def task1():
    task=asyncio.create_task(task2())
    print('t1 one')
    await asyncio.sleep(1)
    print('t1 two')
    await asyncio.sleep(1)

asyncio.run(task1())