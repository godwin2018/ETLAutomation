import pandas as pd
from sqlalchemy import create_engine
server= 'mysqldb.cvu2ys6a4k5a.eu-west-2.rds.amazonaws.com'
port = 3306
username = 'admin'
password =  'password'
database = 'aws_demo_db'

#rds_conn = create_engine("mysql+pymysql://username:password@server:port/mysqldb")
rds_conn = create_engine("mysql+pymysql://admin:password@mysqldb.cvu2ys6a4k5a.eu-west-2.rds.amazonaws.com:3306/aws_demo_db")

def read_data_from_rds():
    df = pd.read_sql("select * from product",rds_conn)
    print(df)

def write_data_to_rds():
    df = pd.read_sql("select * from product", rds_conn)
    #df = pd.read_csv("product.csv")
    df.to_sql("product_tgt",rds_conn,index=False)
    print("Data is written to the RDS DB!")


read_data_from_rds()
write_data_to_rds()