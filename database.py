import pyodbc

SERVER = '10.50.10.127'
DATABASE = 'RCM_PatientReg'
USERNAME = 'sa'
PASSWORD = 'CNMIchc*2018'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Encrypt=no;TrustServerCertificate=yes'
conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT 
TOP 5 *
FROM 
dbo.PATIENT
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)


records = cursor.fetchall()
for r in records:
    print(f"{r}")