the_rack
========

A simpler DI Container.

Install it using pip:

    pip install the_rack

Usage example:

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
