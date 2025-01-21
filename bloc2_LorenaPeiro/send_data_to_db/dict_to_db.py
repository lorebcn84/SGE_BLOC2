import psycopg2

def send_data_to_db(pos, data) :
    print(data)
    conn = psycopg2.connect