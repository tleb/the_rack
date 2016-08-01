## Simple usage

```python
from the_rack import Rack
c = Rack()

# You have two ways to set a key:
c.set('foo', lambda get: 'bar')
c['foo'] = lambda get: 'bar'

# And two ways to get a key:
c.get('foo')
c['foo']
```

## Factory

```python
# By default, a callable is cached but this behaviour can be stopped:
c.set('foo', lambda get: 'bar', True)

# Another solution is by using .factory()
c.set('foo', lambda get: 'bar')
c.factory()

# By default, .factory() uses the most recently added key, but the can be
# overriden
c.factory('foo')

# You can chain .set() and .factory() as .set() returns the rack:
c.set('foo', lambda get: 'bar').factory()

# Or you can use the dict-like syntax to set and .factory():
c['foo'] = lambda get: 'bar'
c.factory()
```

## Exists

```python
# There are two ways available to see if a key exists:
c.exists('foo')
'foo' in c
```

## Delete

```python
# Again, two ways to do the same thing:
c.delete('foo')
del(c['foo'])
```

## Extending

```python
# You can easily modify an entry by extending it:
c.set('foo', lambda get: 'foo')
c.extend('foo', lambda get, prev: prev() + 'bar')

assert c.get('foo') == 'foobar'

# The extending function takes two parameters: get, which is the same as a
# standard function, and prev, which calls the previous function.

# A function can be extended as many times as needed.
```
