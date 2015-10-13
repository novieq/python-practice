Outside of Python, all but the simplest generators would be referred to as coroutines. I'll use the latter term later in the post. The important thing to remember is, in Python, everything described here as a coroutine is still a generator. Python formally defines the term generator; coroutine is used in discussion but has no formal definition in the language.

 If the body of a def contains yield, the function automatically becomes a generator function (even if it also contains a return statement).

 generator functions create generator iterators. That's the last time you'll see the term generator iterator, though, since they're almost always referred to as "generators". Just remember that a generator is a special type of iterator. To be considered an iterator, generators must define a few methods, one of which is __next__(). To get the next value from a generator, we use the same built-in function as for iterators: next()

 When a generator function calls yield, the "state" of the generator function is frozen; the values of all variables are saved and the next line of code to be executed is recorded until next() is called again. Once it is, the generator function simply resumes where it left off. If next() is never called again, the state recorded during the yield call is (eventually) discarded.

 The next line of get_primes takes a bit of explanation. While yield number would yield the value of number, a statement of the form other = yield foo means, "yield foo and, when a value is sent to me, set other to that value." You can "send" values to a generator using the generator's send method.

