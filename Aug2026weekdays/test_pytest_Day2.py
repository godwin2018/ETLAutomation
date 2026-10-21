# Parametrisation
import pytest
import pandas as pd
from jupyter_builder import debug_log_file_mixin
from numpy.ma.core import equal
from sqlalchemy import create_engine
import oracledb

'''
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

#@pytest.mark.skip(reason="Not Required for now")
def test_compare_file_hardAssert_3():
    assert 3 == 3, "Numbers NOt Equal test 5"


# we can define custom markers as well e.g data extraction marker, data validation marker etc




myoracle_conn = create_engine('oracle+oracledb://repo:repo@localhost:1522/xe')
oracledb.init_oracle_client(lib_dir='C:\\Users\\USER\\Downloads\\instantclient-basic\\instantclient_23_26')

def test_count_check_1():
    df = pd.read_sql('select * from product', myoracle_conn)
    count_actual = df.size
    print(count_actual)
    count_expected = 140
    assert count_actual == count_expected, 'Count test failed because row count not matching'
   #pd.read_sql("select * from product")


def test_count_check_2():
    df = pd.read_sql('select * from product', myoracle_conn)
    count_actual = df.size
    print(count_actual)
    count_expected = 140
    assert count_actual == count_expected, 'Count test failed because row count not matching'


def test_count_check_3():
    df = pd.read_sql('select * from product', myoracle_conn)
    count_actual = df.size
    print(count_actual)
    count_expected = 140
    assert count_actual == count_expected, 'Count test failed because row count not matching'


# Using fixture to test


def test_count_check_1(get_dataframe):
    count_actual = get_dataframe.size
    print(count_actual)
    count_expected = 140
    assert count_actual == count_expected, 'Count test failed because row count not matching'


def test_compare_data_two_files(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'
'''
# Running parallel tests
@pytest.mark.order(5)
@pytest.mark.regression
def test_compare_data_two_files1(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'

@pytest.mark.order(1)
@pytest.mark.smoketest
def test_compare_data_two_files2(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'

@pytest.mark.order(2)
@pytest.mark.data_validation
def test_compare_data_two_files3(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'

@pytest.mark.order(3)
@pytest.mark.data_quality
def test_compare_data_two_files4(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'

@pytest.mark.order(4)
@pytest.mark.data_quality
def test_compare_data_two_files5(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'

@pytest.mark.order(6)
@pytest.mark.data_count
def test_compare_data_two_files6(read_src_file,read_tgt_file):

    print(read_src_file)
    print(read_tgt_file)
    #assert read_src_file == read_tgt_file,'data mismatch on both csv files'
    assert read_src_file.equals(read_tgt_file),'data mismatch on both csv files'



