import pytest
from main import Rice


@pytest.mark.parametrize("w,res", [(1000, 1000), (1, 1)])
def test_1(w, res):
    r = Rice(w)
    r.get_rice()
    assert r.right == res


@pytest.mark.parametrize("w,res", [(1000, 10), (1, 1)])
def test_2(w, res):
    r = Rice(w)
    r.get_rice()
    assert r.counter == res
    assert r.counter == r.length


def test_3():
    with pytest.raises(ValueError):
        r = Rice('Ex')
