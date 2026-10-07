import pandas as pd
import xml.etree.ElementTree as ET
import json
import os

df = pd.read_csv("C:\\Users\\USER\\Documents\\ETL\\data\\order_raw.csv")
print(df.head())
type(df)
#df.info()
#df.describe()

# read JSON

#========== READ JSON ============
print("========== READ JSON ============")
json_data = pd.read_json('C:\\Users\\USER\\Documents\\ETL\\data\\orders.json')
print(json_data.head())


#========== READ XML ============
print("========== READ XML ============")

#xml_data = pd.read_xml('C:\\Users\\USER\\Documents\\ETL\\data\\Customers.xml')
#import xml.etree.ElementTree as ET
tree = ET.parse('C:\\Users\\USER\\Documents\\ETL\\data\\Customers.xml')
print(tree.findall('.//Customer'))
print(tree.getroot())
print("========== READ CHILD XML ============")
for child in tree.getroot():
    #print(child)
    print(child.tag)
    #print(child.attrib)
    print('------------------')
    print(child.tag, child.text)



#========== READ FLAT FILE ============
print("========== READ FLAT FILE ============")
flat_data = open('C:\\Users\\USER\\Documents\\ETL\\data\\order_raw2.txt')
print(flat_data.read(50))
flat_data.close()

print("----------------------")
flat_data = open('C:\\Users\\USER\\Documents\\ETL\\data\\Pythondata')
print(flat_data.read(1000))


#========== READ EXCEL FILE ============
print("========== READ EXCEL FILE ============")
excel_data = pd.read_excel('C:\\Users\\USER\\Documents\\ETL\\data\\Product.xlsx')
print(excel_data.head())
print("----------------------")
excel_sheet = pd.read_excel('C:\\Users\\USER\\Documents\\ETL\\data\\Product.xlsx', sheet_name='Product2')
print(excel_sheet.head())

print("-----------Read Multiple Sheets-----------")
all_sheets = pd.read_excel('C:\\Users\\USER\\Documents\\ETL\\data\\Product.xlsx')
for sheet_name, df in all_sheets.items():
    print(f'Sheet Name is:{sheet_name}')
    print(df.head())