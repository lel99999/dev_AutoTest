import pyodbc
# May need to execute $kinit for kerberos authentication

_server = 'servername'
_database = 'DefaultDB'
_uid = '<domain>\<username>'  
_pwd = '<your_password>'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + _server + ';DATABASE=' + _database + ';UID="' + _uid + '";PWD=' + _pwd + ';Trusted_Connection=yes;')
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
