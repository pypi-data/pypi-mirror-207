# This file is placed in the Public Domain.
# pylint: disable=C0114,C0115,C0116,W1503


"decoder tests"


import unittest


from operbot.objects import Object
from operbot.decoder import loads
from operbot.encoder import dumps


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")

    def test_doctest(self):
        """
            >>> from operbot.objects import Object, dumps, loads
            >>> obj = Object()
            >>> obj.test = "bla"
            >>> oobj = loads(dumps(obj))
            >>> oobj.test
            'bla'
        """
        self.assertTrue(True)
