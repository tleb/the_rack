from unittest import TestCase, main
from the_rack import Rack

class Foo:
    pass

class RackTest(TestCase):
    def setUp(self):
        self.r = Rack()

    def test_get(self):
        self.r.set('foo', lambda get: 'foo')
        self.assertEqual('foo', self.r.get('foo'))
        self.assertEqual('foo', self.r.get('foo'))

    def test_factory_through_set(self):
        self.r.set('foo', lambda get: Foo(), True)
        self.assertNotEqual(self.r.get('foo'), self.r.get('foo'))

    def test_factory_through_method_without_key(self):
        self.r.set('foo', lambda get: Foo()).factory()
        self.assertNotEqual(self.r.get('foo'), self.r.get('foo'))

    def test_factory_through_method_with_key(self):
        self.r.set('foo', lambda get: Foo()).factory('foo')
        self.assertNotEqual(self.r.get('foo'), self.r.get('foo'))

    def test_get_in_lambda(self):
        self.r.set('foo', lambda get: 'foo')
        self.r.set('bar', lambda get: get('foo') + 'bar')

        self.assertEqual('foobar', self.r.get('bar'))

    def test_exists(self):
        self.r.set('foo', lambda get: 'foo')
        self.assertTrue(self.r.exists('foo'))
        self.assertFalse(self.r.exists('bar'))

    def test_set_wrong_type_key(self):
        with self.assertRaises(TypeError):
            self.r.set(1, lambda get: 'foo')
        with self.assertRaises(TypeError):
            self.r.set(True, lambda get: 'foo')
        with self.assertRaises(TypeError):
            self.r.set(1.5, lambda get: 'foo')
        with self.assertRaises(TypeError):
            self.r.set(['foo'], lambda get: 'foo')
        with self.assertRaises(TypeError):
            self.r.set(('foo',), lambda get: 'foo')

    def test_set_func(self):
        with self.assertRaises(Exception):
            self.r.set('foo', True)
        with self.assertRaises(Exception):
            self.r.set('foo', ['foo'])
        with self.assertRaises(Exception):
            self.r.set('foo', 1)
        with self.assertRaises(Exception):
            self.r.set('foo', 1.5)

    def test_dict_syntax(self):
        self.r['foo'] = lambda get: 'bar'
        self.assertEqual('bar', self.r['foo'])
        self.assertTrue('foo' in self.r)
        del self.r['foo']
        with self.assertRaises(IndexError):
            self.r['foo']
        self.assertFalse('foo' in self.r)

    def test_raise_when_factory_before_set(self):
        with self.assertRaises(Exception):
            self.r.factory()

    def test_delete_non_factory(self):
        self.r.set('foo', lambda get: 'bar')
        self.assertTrue(self.r.exists('foo'))
        self.r.delete('foo')
        self.assertFalse(self.r.exists('foo'))

    def test_delete_factory(self):
        self.r.set('foo', lambda get: 'bar', True)
        self.assertTrue(self.r.exists('foo'))
        self.r.delete('foo')
        self.assertFalse(self.r.exists('foo'))

    def test_extend(self):
        self.r.set('foo', lambda get: 'foo')
        self.assertEqual('foo', self.r.get('foo'))
        self.r.extend('foo', lambda get, prev: prev() + 'foo')

        self.assertEqual('foofoo', self.r.get('foo'))


if __name__ == '__main__':
    main()
