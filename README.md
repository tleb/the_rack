the_rack
========

> A cachable collection with extension abilities

## Install using pip

    pip install the_rack

## Usage example

```python
from the_rack import Rack

class Foo: pass

c = Rack()
c['foo'] = lambda get: Foo()

c['foo'] # Foo object

class Bar:
    def __init__(self, foo): pass

c['bar'] = lambda get: Bar(get('foo'))

c['bar'] # Bar object

assert c['bar'] == c['bar'] # Caching
```

The complete usage is explained [in the doc](doc.md).

This code is licenced under [the MIT license](https://tleb.mit-license.org/).
