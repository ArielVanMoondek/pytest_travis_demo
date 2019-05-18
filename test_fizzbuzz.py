import pytest
from fizzbuzz import fizzbuzz

def test_fb_is_called_with_1_argument():
    fizzbuzz(1)

def test_fb_returns_str():
    assert isinstance(fizzbuzz(1),str)
    # třídy jsou instancí stringu

@pytest.mark.parametrize('num', [1,2,4])
def test_fb_regular_is_self(num):
    assert int(fizzbuzz(num)) == num

@pytest.mark.parametrize('num', [3,6,9])
def test_fb_regular_is_fizz(num):
    assert fizzbuzz(num) == 'fizz'

@pytest.mark.parametrize('num', [5,20,50])
def test_fb_regular_is_buzz(num):
    assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [15,30,45])
def test_fb_regular_is_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'

#co ta fce ma dělat, když dostane co nemá dostat a výstupem bude vyjímka
def test_fb_raises_type_error_on_str():
    with pytest.raises(TypeError):
        fizzbuzz('')

@pytest.mark.parametrize('num', ["", 1.5, [], 4 + 3j])
def test_fb_raises_typeError_on_nonint(num):
    with pytest.raises(TypeError):
        fizzbuzz(num)

@pytest.mark.parametrize('num', [0, -1, -20])
def test_fb_raises_valiueError_on_nonint(num):
    with pytest.raises(ValueError):
        fizzbuzz(num)
