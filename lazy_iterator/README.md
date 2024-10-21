Rule of thumb to convert iter to lazyiter :

Converting an iterable to an iterator is as simple as using iter() on an iterable. 
For laziness, you can go the generator route or implement __iter__ and __next__ in your class. 
In either case, you’d be managing the iteration with an index or a similar mechanism.
It ensures you can keep track of your position in the sequence, yielding one element at a time without loading everything into memory

The lazy iterator class does not create a list of polygons upfront. Instead, it initializes an index to keep track of the current polygon.
The index starts at 3 because polygons with fewer than 3 sides are not valid.
Initialization:
  Initialize _current to keep track of the current position in the iteration.

Remove Precomputed List:

  Instead of precomputing and storing all polygons, we generate them on-the-fly.

Implement __iter__:

  Returns self because this object itself is an iterator.

Implement __next__:

  Generates the next polygon and increments the _current counter.

Raises StopIteration when the end is reached.

  when next is there we return self. when next is not there we return self og iterator
