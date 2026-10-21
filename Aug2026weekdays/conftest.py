import pytest
import pandas as pd
from sqlalchemy import create_engine
import oracledb

@pytest.fixture(scope="session")
def greetings():
    print(f"Hello - you are using fixtures - before test...\n")
    yield
    print(f"Bye - You are using fixtures - after test...")


# implementing Auto use
@pytest.fixture(scope="function",autouse=True)
def message():
    print(f"Test started - before test...\n")
    yield
    print(f"Test Ended - after test...")


# define  fixture to get a dataframe
myoracle_conn = create_engine('oracle+oracledb://repo:repo@localhost:1522/xe')
oracledb.init_oracle_client(lib_dir='C:\\Users\\USER\\Downloads\\instantclient-basic\\instantclient_23_26')
@pytest.fixture(scope="session")
def get_dataframe():
    df = pd.read_sql('select * from product', myoracle_conn)
    yield df
    print("closing DB connection")



# read files
@pytest.fixture()
def read_src_file():
	df_src_emp2 = pd.read_csv('C:\\etlAutomation\\datapipeline\\Aug2026weekdays\\emp2.csv')
	yield df_src_emp2

@pytest.fixture()
def read_tgt_file():
    df_tgt_emp3 = pd.read_csv('C:\\etlAutomation\\datapipeline\\Aug2026weekdays\\emp3.csv')
    yield df_tgt_emp3



