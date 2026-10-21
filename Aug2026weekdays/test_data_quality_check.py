from pyspark.sql import pandas

import pandas as pd
import pytest


# Data quality check

def test_dataTypes(get_dataframe):
    print("Test data types... Test Started!!!")
    actual_datatypes = get_dataframe.dtypes.to_dict()
    print(f'Actual Data Types: {actual_datatypes}')
    expected_datatypes = {'product_id': 'int64','product_name': 'o','category': 'o'}
    print(f'Expected Data Types: {expected_datatypes}')
    assert actual_datatypes == expected_datatypes, 'they do not match'



# Foreign Key and referential integrity

def test_referential_integrity
'''def test_count_check_1(get_dataframe):
    count_actual = get_dataframe.size
    print(count_actual)
    count_expected = 140
    assert count_actual == count_expected, "Count test failed because row count not matching"'''