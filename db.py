# Agenda con base de datos SQL Server
import pyodbc

def connect():
    '''Conexión a la Base de datos'''

    server='localhost\SQLEXPRESS'
    database = 'agenda' 
    username = 'DESKTOP-96GJCG3C\nati' 
    password = ''

    try:
        conexion = pyodbc.connect('Trusted_Connection=Yes;DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conexion.cursor()
        #print("Conexión correcta")
        return conexion
    except Exception as e:
        print("Ocurrió un error al conectar: ", e)

def create_table(cursor=connect()):
    '''Creación de la Base de datos'''

    connect()
    query = 'CREATE TABLE CONTACTOS(id int IDENTITY(1,1) PRIMARY KEY NOT NULL, nombre varchar(20) NOT NULL, apellidos varchar(20) NOT NULL, telefono varchar(14) NOT NULL, email varchar(20) NOT NULL)'
    try:
        with cursor.cursor() as cursor:
            cursor.execute(query)
            print('La tabla fue creada con éxito')
    except Exception as e:
        print("No se pudo crear la tabla: ", e)
    finally:
        cursor.close()

def insert_data(nombre, apellidos, telefono, email, cursor=connect()):
    '''Agregar datos en la Base de Datos'''

    connect()

    query = 'INSERT INTO contactos(nombre,apellidos,telefono,email) VALUES (?, ?, ?,?)'
    
    try:
        with cursor.cursor() as cursor:
            cursor.execute(query, [nombre, apellidos, telefono,email])
            print("Datos guardados con exito")
    except Exception as e:
        print("Ocurrió un error al intentar guardar los datos: ", e)
    finally:
        cursor.commit()
        cursor.close()
        print("Se ha finalizado la inserción de datos")

def update_data(nombre, apellidos, telefono, email, nom_buscado, cursor=connect()):
    '''Actualizar datos en la Base de Datos'''

    connect()
    query= 'UPDATE contactos SET nombre =?,apellidos =?,telefono =?,email =? WHERE nombre=?'

    try:
        with cursor.cursor() as cursor:
            cursor.execute(query,[nombre,apellidos,telefono,email,nom_buscado])
            cursor.commit()
            print("Datos actualizados con exito")
    except Exception as e:
        print("Ocurrió un error al intentar actualizar los datos: ", e)
    finally:
        cursor.close()
        print("Se ha finalizado la actualización de datos")

def delete_data(nom_buscado, cursor=connect()):
    '''Eliminar datos en la Base de Datos'''
    connect()
    query= 'DELETE FROM contactos WHERE nombre=?'

    try:
        with cursor.cursor() as cursor:
            cursor.execute(query, nom_buscado)
            print("Se ha eliminado el registro con exito")
    except Exception as e:
        print("Ocurrió un error al intentar eliminar los datos: ", e)
    finally:
        cursor.commit()
        cursor.close()
        print("Se ha finalizado la eliminación de datos")

def get_all_data(cursor=connect()):
    '''Listar todos los datos de la Base de Datos'''
    connect()
    query= 'SELECT * FROM contactos'
    try:
        with cursor.cursor() as cursor:
            cursor.execute(query)
            records = cursor.fetchall()

        print(f'{"id":3s}{"nombre":15s}{"apellido":15s}{"telefono":11s}{"email":20s}')
        for row in records:
           if row=='':
               print("No hay contactos...")
           else:
               print(f"{row[0]:<3d}{row[1]:15s}{row[2]:15s}{row[3]:11s}{row[3]:20s}\n") #Mostramos La lista
    except Exception as e:
        print("Ocurrió un error al consultar los datos", e)
    finally:
        cursor.close()
        print("Se ha finalizado la consulta de datos")

def get_data(nombre_buscado, cursor=connect()):
    '''Buscar un solo valor en la Base de Datos'''

    connect()
    query='SELECT * FROM contactos WHERE nombre =?'
    try:
        with cursor.cursor() as cursor:
            cursor.execute(query, nombre_buscado)
            records = cursor.fetchall()

        print(f'{"id":3s}{"nombre":15s}{"apellido":15s}{"telefono":11s}{"email":20s}')
        for row in records:
            if row=='':
               print("No hay contactos...")
            else:
                print(f"{row[0]:<3d}{row[1]:15s}{row[2]:15s}{row[3]:11s}{row[3]:20s}\n") #Mostramos La lista
    except Exception as e:
        print("Ocurrió un error al consultar los datos", e)
    finally:
        cursor.close()
        print("Se ha finalizado la consulta de datos")
