eventloop.py - this code contains excellent code to implement an event loop from ground up
http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html

eventloop2.py - this code contains the fib written as a coroutine

After the addition of aynchio the asyncore module was replaced

threading - is using normal threads. You can improve it with futures. Threads are suitable for I/O bound tasks and
multiprocessing is suitable for CPU bound tasks.

GIL ensures that only one thread runs in the interpreter at once. When the thread is running it holds the GIL. GIL is
released on IO.

Futures are actually a very nice tool that helps bridge an annoying gap that always exists in concurrent execution - the
gap between launching some computation concurrently and obtaining the result of that computation. One of the common ways to deal with this gap is to pass a synchronized Queue object into every worker process (or thread)
and then collect the results once the workers are done. Futures make this much easier and more elegant, as we'll see.

The Future class encapsulates the asynchronous execution of a callable. Future instances are created by Executor.submit().

