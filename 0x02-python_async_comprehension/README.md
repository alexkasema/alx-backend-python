# Python - Async Comprehension
Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax.
Implementing similar syntactic constructions for the asynchronous code.
To illustrate the readability improvement, consider the following example:

result = []
async for i in aiter():
    if i % 2:
        result.append(i)
With the proposed asynchronous comprehensions syntax, the above code becomes as short as:

result = [i async for i in aiter() if i % 2]
The PEP also makes it possible to use the await expressions in all kinds of comprehensions:

result = [await fun() for fun in funcs]
## Asynchronous Comprehensions
* set comprehension: {i async for i in agen()};
* list comprehension: [i async for i in agen()];
* dict comprehension: {i: i ** 2 async for i in agen()};
* generator expression: (i ** 2 async for i in agen()).
It is allowed to use async for along with if and for clauses in asynchronous comprehensions and generator expressions:

dataset = {data for line in aiter()
                async for data in line
                if check(data)}
Asynchronous comprehensions are only allowed inside an async def function.
## await in Comprehensions
The use of await expressions in both asynchronous and synchronous comprehensions:

result = [await fun() for fun in funcs]
result = {await fun() for fun in funcs}
result = {fun: await fun() for fun in funcs}

result = [await fun() for fun in funcs if await smth]
result = {await fun() for fun in funcs if await smth}
result = {fun: await fun() for fun in funcs if await smth}

result = [await fun() async for fun in funcs]
result = {await fun() async for fun in funcs}
result = {fun: await fun() async for fun in funcs}

result = [await fun() async for fun in funcs if await smth]
result = {await fun() async for fun in funcs if await smth}
result = {fun: await fun() async for fun in funcs if await smth}
This is only valid in async def function body.
## 0-async_generator.py
Async Generator
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

