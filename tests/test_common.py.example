import common

def test_checkKeys():
    assert common.checkKeys(None, []) == False

    assert common.checkKeys(1, []) == False
  
    
    assert common.checkKeys({'a':1, 'c':2}, ['a', 'b']) == False 

    assert common.checkKeys({'a':1, 'b': None}, ['a', 'b']) == False

    assert common.checkKeys({'a':1, 'b':2, 'c':3}, ['a', 'b']) == True
