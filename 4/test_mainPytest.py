import pytest
from main import dodawanie
from main import funkcja_silni
from main import odejmowanie
from main import pierwiastek

testdataDod = [(1, 2, 3), (10, 5, 15), (-5, 6, 1)]
testdataDodTE = [(1, 'true', 3), (0b1000, 5, 13)]
testdataDodTV = [(-32767, 32767, 0), (5, 10, 15), (-2147483647, 2147483647, 0)]
testdataOdod = [(2, 2, 0), (-8, -2, -6), (2, -7, 9)]
testdataOdodTE = [(2, 0b10, 0), (-8, --2, -6), ('2', -7, 9)]
testdataOdodTV = [(-32767, 32767, -65534 ), (5, 10, -5), (-2147483647, 2147483647, -4294967294)]
testdataSilnia = [(1, 1), (0, 1)]
testdataSilniaTE = [(3 + 8j, 1), ('0', None)]
testdataSilniaTV = [(3 + 8j, 1), (-1, None)]
testSqrt = [(3, 27, 3.0), (2, 4, 2.0), (8, 1, 1.0)]
testSqrtTE = [(0b11, 27, 3.0), ("2", 4, 2.0)]
testSqrtTV = [(-3, 27, 3.0), (-2, 4, 0.5)]


@pytest.mark.parametrize("num1, num2, result", testdataDod)
def test_dodawanie(num1, num2, result):
    assert dodawanie(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testdataDodTE)
def test_dodawanie_Type_error(num1, num2, result):
    with pytest.raises(TypeError):
        assert dodawanie(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testdataDodTV)
def test_dodawanie_Type_value(num1, num2, result):
    with pytest.raises(ValueError):
        assert dodawanie(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testdataOdod)
def test_odejmowanie(num1, num2, result):
    assert odejmowanie(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testdataOdodTE)
def test_odejmowanie_Type_error(num1, num2, result):
    with pytest.raises(TypeError):
        assert odejmowanie(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testdataOdodTV)
def test_odejmowanie_Type_error(num1, num2, result):
    with pytest.raises(ValueError):
        assert odejmowanie(num1, num2) == result


@pytest.mark.parametrize("num1, result", testdataSilnia)
def test_silnia(num1, result):
    assert funkcja_silni(num1) == result


@pytest.mark.parametrize("num1, result", testdataSilniaTE)
def test_silnia(num1, result):
    assert funkcja_silni(num1) == result


@pytest.mark.parametrize("num1, result", testdataSilniaTE)
def test_silnia_Type_error(num1, result):
    with pytest.raises(TypeError):
        assert funkcja_silni(num1) == result


@pytest.mark.parametrize("num1, num2, result", testSqrt)
def test_pierwiastek(num1, num2, result):
    assert pierwiastek(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testSqrtTE)
def test_pierwiastek_Type_error(num1, num2, result):
    with pytest.raises(TypeError):
        assert pierwiastek(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", testSqrtTV)
def test_pierwiastek_Type_error(num1, num2, result):
    with pytest.raises(ValueError):
        assert pierwiastek(num1, num2) == result

