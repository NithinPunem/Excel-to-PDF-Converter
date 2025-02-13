import pandas as pd
import mysql.connector

# MySQL connection details
mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'student_data'
}

# Function to insert data into MySQL with missing data handling
def insert_new_data(df):
    # Fill missing values with default values if needed, e.g., 'Unknown' for text fields
    df = df.fillna({'course': 'Unknown', 'hallticket_no': 'Unknown', 'name': 'Unknown', 
                    'examination': 'Unknown', 'month-year': 'Unknown', 'branch': 'Unknown', 
                    'subject_code': 'Unknown', 'subject_name': 'Unknown', 'doe': '0000-00-00', 
                    'year_code': 'Unknown'})

    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()

        # Delete old data before inserting new data
        cursor.execute("DELETE FROM records")
        print("Old data deleted successfully.")

        # Insert new data
        for _, row in df.iterrows():
            values = (row['course'], row['hallticket_no'], row['name'], row['examination'],
                      row['month_year'], row['branch'], row['subject_code'], row['subject_name'],
                      row['doe'], row['year_code'])

            cursor.execute("INSERT INTO records (course, hallticket_no, name, examination, month_year, branch, subject_code, subject_name, doe, year_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values)

        conn.commit()
        print("New data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Load data and call the function
excel_path = "C:\\Users\\NAGASREE\\Desktop\\git_projects\\student_data1.xlsx"
df = pd.read_excel(excel_path)

# Insert data into MySQL
insert_new_data(df)
