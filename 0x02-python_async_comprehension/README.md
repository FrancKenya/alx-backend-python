Python Async Project
This project demonstrates the basics of Python asynchronous programming, including creating asynchronous generators, using async comprehensions, and measuring execution runtime for asynchronous tasks.

Learning Objectives
By the end of this project, you should be able to:

Write an asynchronous generator.
Use async comprehensions to work with asynchronous generators.
Measure runtime for coroutines executed in parallel using asyncio.gather.
Files
1. async_generator.py
Defines an asynchronous generator:

Loops 10 times.
Waits 1 second in each loop.
Yields a random number between 0 and 10.
2. async_comprehension.py
Defines an asynchronous comprehension:

Collects 10 random numbers from async_generator.
Returns the collected numbers as a list.
3. measure_runtime.py
Measures the runtime for parallel execution:

Executes async_comprehension four times in parallel using asyncio.gather.
Returns the total runtime (approximately 10 seconds).
