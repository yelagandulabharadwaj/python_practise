import asyncio

async def func1():
    task=asyncio.create_task(func2())
    print('func1 one')
    await asyncio.sleep(1)
    print('func1 two')
    await asyncio.sleep(2)

async def func2():
    print('func2 one ')
    await asyncio.sleep(1)
    print('func2 two')


asyncio.run(func1())