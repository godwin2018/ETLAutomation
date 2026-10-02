#%%
import pandas as pd
from openpyxl.styles.builtins import title
from pandas.core.missing import check_value_size
#%%
df = pd.read_csv('emp.csv')
#%%
df.head()
#%%
#specify which columns to read
df = pd.read_csv("emp.csv", usecols=["eno", "ename", "salary"])
#%%
df
#%%
# specfying on ly on colunms
df["ename"]
#%%
# Specify a primary key (eno)
df = pd.read_csv("emp.csv", usecols=["eno", "ename", "salary"], index_col="eno")
#%%
df
#%%
# Return record with eno = 8
df.iloc[8]
#%%
# Return record with emp # 8 and 10
df.iloc[[8,10]]
#%%
df.loc[[8,10]]
#%%
df.head()
#%%
df.loc[[2,8]]
#%%
df.iloc[[2,8]]
#%%
# Get specific colunms and rows
df[["salary","ename"]].iloc[[2,8]]
#%%
# Get specific range of rows
df[["salary","ename"]].iloc[2:8]
#%%
# Return range of rows while jumping by 2 - it is like slicing
df[["salary","ename"]].iloc[2:8:2]
#%%
df.dtypes
#%%
# Specify data types of the colunm
df= pd.read_csv("emp.csv",dtype={"salary":float})
#%%
df.head()
#%%
df = pd.read_csv("netflix_dataset.csv")
#%%
df
#%%
df.count()
#%%
# Read teh dat in chunk (chunk size)
for chunk in pd.read_csv("netflix_dataset.csv",chunksize=1000):
    print(chunk.head())
#%%
# show few colunms
for chunk in pd.read_csv("netflix_dataset.csv",usecols=["show_id","title"],chunksize=1000):
    print(chunk.head(10))
#%%
#Using iterator
iterator =  pd.read_csv("netflix_dataset.csv",usecols=["show_id","title"],chunksize=1000,iterator=True)
for chunk in iterator:
    print(chunk.head(10))
#%%
df = pd.read_csv('emp.csv')
#%%
df.head(20)
#%%
# use iloc t read the data from row 10 to row 20
# way 1
df.iloc[9:20]
#%%
# way 2 - Create a datafrae with rows 10 to 21
df = pd.read_csv("emp.csv",skiprows=10,nrows=11,header=None)
#%%
df
#%%
# Create a dataframe with names
df = pd.read_csv("emp.csv",skiprows=10,nrows=11,names=['empid','ename','sal','deptno','hiringdate'])
#%%
df
#%%
# It is not considering any header
df = pd.read_csv('emp.csv',header=0)
#%%
df
#%%
# using second  row a header
df = pd.read_csv('emp.csv',header=1)
df
#%%
# starting from the fourth row
df = pd.read_csv('emp.csv',header=4)
df.head()
#%%
# Check data type
df = pd.read_csv('emp.csv')
df.dtypes
#%%
#the the dtype of date to date_time
df = pd.read_csv('emp.csv',parse_dates=['doj'])
df.dtypes
#%%
df['doj'].head()
#%%
df['doj'].dt.year.head()
#%%
df['doj'].dt.month.head()
#%%
df['doj'].dt.day.head()
#%%
# Filtering (using where clause in SQL)
# get all emplyee that belong to dept 10 and 20 where salary >3000
df = pd.read_csv('emp.csv')
filter1 = df['deptno']==30
filter2 = df['salary']>3000
#%%
df[filter1&filter2]
#%%
# Sorting - we can sort by index or sort by value
df.sort_values(by='salary',ascending=False).head()
#%%
df.sort_values(by=['deptno','salary'],ascending=False).head()
#%%
df = pd.read_csv('emp.csv')