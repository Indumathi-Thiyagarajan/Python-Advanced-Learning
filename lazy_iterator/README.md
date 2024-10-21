Rule of thumb to convert iter to lazyiter :

Converting an iterable to an iterator is as simple as using iter() on an iterable. 
For laziness, you can go the generator route or implement __iter__ and __next__ in your class. 
In either case, you’d be managing the iteration with an index or a similar mechanism.
It ensures you can keep track of your position in the sequence, yielding one element at a time without loading everything into memory
