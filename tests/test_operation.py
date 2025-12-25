from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5 ## assert ena panuna intha add function la (2,3) input kodutha 5 nu o/p varthantu check panu.
    assert add(-1,1)==0 ## ithu mathritha ella i/p ku test panu
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1