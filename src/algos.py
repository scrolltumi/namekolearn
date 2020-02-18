# algos.py

from nameko.rpc import rpc
import collections
import unittest
import huffman
from collections import Counter
from nameko.testing.services import worker_factory



class AlgosService:
    name = "algos_service"
    codedDict = {}

    @rpc
    def squareOddNumbers(self, integers):
        for i in range(len(integers) - 1):
            if integers[i] % 2 != 0:
                integers[i] = integers[i]**2
        return integers
    
    @rpc
    def huffmanEncode(self, stringList):
        self.codedDict = huffman.codebook(Counter(stringList).items())
        return self.codedDict

    @rpc
    def huffmanDecode(self, encodedString):
        if (self.codedDict):
            originalStrings = list(self.codedDict.keys())
            encodedStrings = list(self.codedDict.values())
            return originalStrings[encodedStrings.index(encodedString)]
        return 'not in saved list.This is an inadequate solution'

def test_algos(self):
    # create worker with mock dependencies
    service = worker_factory(AlgosService)

    # test squareOddNumbers 
    squared = service.squareOddNumbers([2, 7, 5, 64, 14])
    assert squared == [2, 49, 25, 64, 14]

    # test huffmanEncode 
    encoded = service.huffmanEncode(['FR', 'UK', 'BE', 'IT', 'FR', 'IT', 'GR', 'FR', 'NL', 'BE', 'DE'])
    assert encoded == {'FR': '10', 'UK': '011', 'BE': '110', 'IT': '111', 'GR': '010', 'NL': '001', 'DE': '000'}
    