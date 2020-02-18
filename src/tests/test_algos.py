from nameko.testing.services import worker_factory 
from src.algos import AlgosService 
 
def test_algos():
    # create worker with mock dependencies
    service = worker_factory(AlgosService)

    # test squareOddNumbers 
    squared = service.squareOddNumbers([2, 7, 5, 64, 14])
    assert squared == [2, 49, 25, 64, 14]

    # test huffmanEncode 
    encoded = service.huffmanEncode(['FR', 'UK', 'BE', 'IT', 'FR', 'IT', 'GR', 'FR', 'NL', 'BE', 'DE'])
    assert encoded == {'FR': '10', 'UK': '011', 'BE': '110', 'IT': '111', 'GR': '010', 'NL': '001', 'DE': '000'}
 