import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM clientes"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()  # Obtenim els resultats
    print(results)
    print(results[4])
    print(results[4][2])

print (read_reg())

