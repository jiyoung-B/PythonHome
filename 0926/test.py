import myfunction
    
def test_sum() :
    assert myfunction.sum(2, 5) == 7
    assert myfunction.sum(2.3, 5.2) == 7.5
    
def test_multiple() :
    assert myfunction.multiple(2, 5) == 10
    assert myfunction.multiple(2.0, 5.0) == 10.0