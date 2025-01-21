import dict_to_db as d_t_db
import pandas as pd

def csv_to_dict():
    df = pd.read_csv("Clientes.csv")
    d = df.to_dict(orient='list')
    return d

data = csv_to_dict()

for i in range(30) :
    d_t_db.send_data_to_db(i,data) (
        database="the bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )
    
    cur = conn.cursor()
    sql = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"