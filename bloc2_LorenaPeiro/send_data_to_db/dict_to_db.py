import psycopg2

def send_data_to_db(pos, data) :
    print(data)
    conn = psycopg2.connect (
        database="the bear",
        password="admin",
        use="admin",
        host="localhost",
        port="5432"
    )
    
    cur = conn.cursor()
    sql = "INSERT INTO Clientes (nombre_clientes, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"
    
    values = data["Nombre_Cliente"] [pos], data[]