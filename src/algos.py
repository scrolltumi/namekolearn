# algos.py

from nameko.rpc import rpc
import collections
import unittest
import huffman
from collections import Counter
from nameko.testing.services import worker_factory



class AlgosService:
    name = "algos_service"

    @rpc
    def squareOddNumbers(self, integers):
        for i in range(len(integers) - 1):
            if integers[i] % 2 != 0:
                integers[i] = integers[i]**2
        return integers
    
    @rpc
    def huffmanEncode(self, stringList):
        return huffman.codebook(Counter(stringList).items())

    @rpc
    def huffmanDecode(self, encodedString):
        #Some code to decode
        #Still to do. Not sure I understand
        return encodedString
    
def test_algos_service():
    # create worker with mock dependencies
    service = worker_factory(AlgosService)

    # test squareOddNumbers 
    squared = service.squareOddNumbers([2, 7, 5, 64, 14])
    assert squared == [2, 49, 25, 64, 14]

    # test huffmanEncode 
    encoded = service.huffmanEncode(['FR', 'UK', 'BE', 'IT', 'FR', 'IT', 'GR', 'FR', 'NL', 'BE', 'DE'])
    assert encoded == {'FR': '10', 'UK': '011', 'BE': '110', 'IT': '111', 'GR': '010', 'NL': '001', 'DE': '000'}

    

    

    