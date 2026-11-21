import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    # 1. Establish the connection
    connection = mysql.connector.connect(
        host="localhost",        # Or your server IP address
        user="root",             # Your MySQL username
        password="root", # Your MySQL password
        database="sakila"  # Optional: omit if creating a new database
    )

    if connection.is_connected():
        # 2. Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # 3. Execute a query (Example: Fetch data)
        cursor.execute("select * from sakila.customer limit 10")
        records = cursor.fetchall()
        df=pd.DataFrame(records, columns=["customer_id","store_id","first_name","last_name","email","address_id","active","create_date","last_update"])
        print("*"*100)
        print(df.head())
        print("*"*100)
        print(df)
        print("*"*100)
        
        #for row in records:
        #    print(row)

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # 4. Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
