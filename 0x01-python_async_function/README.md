# Python - Async
asyncio is a library to write concurrent code using the async/await syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level structured network code.

## asyncio provides a set of high-level APIs to:

* run Python coroutines concurrently and have full control over their execution;

* perform network IO and IPC;

* control subprocesses;

* distribute tasks via queues;

* synchronize concurrent code;

## Additionally, there are low-level APIs for library and framework developers to:

* create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc;

* implement efficient protocols using transports;

* bridge callback-based libraries and code with async/await syntax.

## 0-basic_async_syntax.py
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
## 1-concurrent_coroutines.py
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.
## 2-measure_runtime.py
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
