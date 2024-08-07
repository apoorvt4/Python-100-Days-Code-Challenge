# import time
# import asyncio
# import requests



# async def function1():
#     url = 'https://images.unsplash.com/photo-1660748054768-33282c43c318?q=80&w=377&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
#     r = requests.get(url, allow_redirects=True)
#     open('google.jpg', 'wb').write(r.content)
#     print("func1")
    
# async def function2():
#     url = 'http://google.com/favicon.ico'
#     r = requests.get(url, allow_redirects=True)
#     open('google2.ico', 'wb').write(r.content)
#     print("func2")

# async def function3():
#     url = 'http://google.com/favicon.ico'
#     r = requests.get(url, allow_redirects=True)
#     open('google3.ico', 'wb').write(r.content)
#     print("func3")

# async def main():
#     l = await asyncio.gather(
#         await function1(),
#         await function2(),
#         await function3(),
#     )
#     print(l)
    
#     # await function1()
#     # await function2()
#     # await function3()

# asyncio.run(main())


import asyncio


async def func1():
	print("Function 1 started..")
	await asyncio.sleep(2)
	print("Function 1 Ended")


async def func2():
	print("Function 2 started..")
	await asyncio.sleep(3)
	print("Function 2 Ended")


async def func3():
	print("Function 3 started..")
	await asyncio.sleep(1)
	print("Function 3 Ended")


async def main():
	L = await asyncio.gather(
		func1(),
		func2(),
		func3(),
	)
	print("Main Ended..")


asyncio.run(main())

