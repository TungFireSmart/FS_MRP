import pandas as pd
import mysql.connector

# Set up connection to SQL Server database


conn = mysql.connector.connect(user='root', password='btk123456', host='127.0.0.1', database='mrp')
mycur = conn.cursor(buffered=True)

# Read Excel file into a pandas DataFrame
df = pd.read_excel('ds_san_pham.xlsx', usecols=[0,1])

# mycur.execute('drop table if exists vat_tu_test')
# mycur.execute('create table vat_tu_test as select * from chi_tiet_linh_kien')
# mycur.execute('delete from vat_tu_test')

# Define the SQL query to insert data into the table
# query = "INSERT INTO gia_tong_hop (stt, ten_san_pham, model, don_vi, gia_cap_3) VALUES (?, ?, ?, ?, ?)"
query = "INSERT INTO ds_san_pham (Model, ten_san_pham) VALUES ('{}', '{}')"
# Iterate through rows in the DataFrame and execute the SQL query for each row

print(df)

for index, row in df.iterrows():

    values1 = df.iloc[index, 0]   # giá trị tại cột 1
    values2 = df.iloc[index, 1]   # giá trị tại cột 2

    mycur.execute(query.format(values1, values2))

# Commit changes to the database and close the connection
conn.commit()
conn.close()
