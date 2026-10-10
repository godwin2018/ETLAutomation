import pandas as pd
import oracledb
from sqlalchemy import create_engine



# This is for the Shop_db Database
postgress1_tgt_conn = create_engine('postgresql+psycopg://shop_user:test@localhost:5432/shop_db')
#%%
#postgress1_tgt_conn
#%%
def test_compare_data():
    query_target = 'select * from product'
    df_target = pd.read_sql(query_target, postgress1_tgt_conn)
    print(df_target)

    #df_csv_src = pd.read_csv('data/product.csv')
    data_loc = 'C:\\etlAutomation\\datapipeline\\Aug2026weekdays\\data\\product.csv'
    df_csv_src = pd.read_csv(data_loc)
    print(df_csv_src)

    #assert df_target.compare(df_csv_src), 'Data not matched for both tables'