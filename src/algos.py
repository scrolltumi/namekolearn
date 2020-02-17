# algos.py

from nameko.rpc import rpc
import collections
import unittest
import huffman
from collections import Counter



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
        
    