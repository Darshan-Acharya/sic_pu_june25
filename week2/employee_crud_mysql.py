import pymysql

def connect_db():
    connection = None
    try:
<<<<<<< HEAD
        connection = pymysql.Connect(
            host='localhost',
            user="root",
            password="dARSHAN@1802",
            database='darshan_db',  # Fixed typo here
            port=3306,
            charset="utf8"
        )
=======
        connection = pymysql.Connect(host='localhost', user="root", password="dARSHAN@1802", database = "darshan_db", port = 3306, charset = "utf8")
>>>>>>> df6f6f19a6ac4365eb380826c6044a55ecc1e1d0
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('DB disconnection failed')

def create_db():
    query = 'create database IF NOT EXISTS darshan_db'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Database creation failed')

def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, name varcahr(50) not null, designation varchar(30), phone_number	bigint unique, salary float, commission		float default(0), years_of_experience tinyint, technology		varchar(30)	not null)'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Table creation failed')

def read_all_employees():
    query = 'select * from employees'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchAll()
        for row in rows:
            print(row)
        print('All rows retrived')
        
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')

connection = connect_db()
<<<<<<< HEAD
disconnect_db(connection)
=======
create_table()
disconnect_db(connection)
#connection.close() # to disconnect the DB
>>>>>>> df6f6f19a6ac4365eb380826c6044a55ecc1e1d0
