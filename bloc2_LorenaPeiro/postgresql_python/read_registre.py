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
    #Les dades de l’Andreu
    print(results[9])
    #El correu de l’Andreu
    print(results[9][3])
    #Les dades de la Vivian
    print(results[14])
    #La direcció de la Vivian
    print(results[14][1])
    #Les dades de l’Albert
    print(results[19])
    #La data de cumpleanys de l’Albert
    print(results[19][4])

print (read_reg())

