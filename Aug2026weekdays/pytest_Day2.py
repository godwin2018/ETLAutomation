# Parametrisation
import pytest

@pytest.mark.regression
@pytest.mark.smoketest
@pytest.mark.parametrize('a,b,expected',[(1,2,3),(4,5,10),(10,10,20)])
def test_compare(a,b,expected):
    assert a + b == expected



# Markers - categorizing test cases
# There are predefined markers e.g. skip and xfail

def test_compare_file_hardAssert_1():
    assert 1==1, "Numbers NOt Equal test 3"

@pytest.mark.xfail
def test_compare_file_hardAssert_2():
    assert 1 == 2, "Numbers NOt Equal test 4"

@pytest.mark.skip(reason="Not Required for now")
def test_compare_file_hardAssert_3():
    assert 3 == 3, "Numbers NOt Equal test 5"


# we can define custom markers as well e.g data extraction marker, data validation marker etc





