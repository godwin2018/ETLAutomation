


server = 'localhost'
server1 = 'localhost\\SQLEXPRESS'
database = 'shop_db'
username = 'shop_user'
password = 'test'
driver = '{ODBC Driver 18 for SQL Server}'
params = urllib.parse.quote_plus('driver;''server,1433;''database;''username;''password''Encrypt=no;')
mssql_src_conn = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
connection_url = sa.engine.URL.create('mssql+pyodbc','username','password','server1','1433','database',query={'driver': 'ODBC Driver 18 for SQL Server','Encrypt':'yes','TrustServerCertificate': 'yes'})


#mssql_src_conn
connection_url
#%%
engine1 = sa.create_engine(connection_url)
#%%
engine1
#%%
with engine1.connect() as connection:
    result = connection.exec_driver_sql("SELECT @@VERSION").scalar()
    print(f"Connected! Server Version: {result}")
#%%
with mssql_src_conn.connect() as connection:
    result = connection.exec_driver_sql("SELECT @@VERSION").scalar()
    print(f"Connected! Server Version: {result}")
#%%
print(pyodbc.drivers())
#%%
import mssql_python
from mssql_python import connect
Server='localhost'
Database='shop_db'
UID='shop_user'
PWD='test'
Encrypt='yes'
TrustServerCertificate='yes'
conn_str = "Server=localhost,1433;Database=shop_db;UID=shop_user;PWD=test;Encrypt=yes;TrustServerCertificate=yes;"
#%%
conn = connect(conn_str)
#%%
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 product_name, price FROM product")
#cursor.execute('select * from product')