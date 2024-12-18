import psycopg2



def create_db(conn):

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS client(
        client_id INTEGER UNIQUE PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        email VARCHAR(30)
        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS phones(
        client_id INTEGER REFERENCES client(client_id),
        phone VARCHAR(20)
        );""")
    conn.commit()


def add_client(conn, client_id, first_name, last_name, email, phones=None):

    cur = conn.cursor()
    cur.execute("""
    INSERT INTO client(client_id, first_name, last_name, email) VALUES(%s, %s, %s, %s);
    """, (client_id, first_name, last_name, email))
    conn.commit()
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phones))
    conn.commit()



def add_phone(conn, client_id, phone):

    cur = conn.cursor()
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phone ))
    conn.commit()


def delete_phone(conn, client_id, phone=None):

    cur = conn.cursor()
    cur.execute("""
    DELETE FROM phones WHERE client_id = %s AND phone = %s;
    """, (client_id, phone))
    conn.commit()



def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    if first_name != None:
        cur = conn.cursor()
        cur.execute("""UPDATE client SET first_name = %s WHERE client_id = %s""", (first_name, client_id))
        conn.commit()
    if last_name != None:
        cur = conn.cursor()
        cur.execute("""UPDATE client SET last_name = %s WHERE client_id = %s""", (last_name, client_id))
        conn.commit()
    if email != None:
        cur = conn.cursor()
        cur.execute("""UPDATE client SET email = %s WHERE client_id = %s""", (email, client_id))
        conn.commit()
    if phones != None:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO phones(client_id, phone) VALUES(%s, %s);""", (client_id, phones))
        conn.commit()
        cur.close()

def delete_client(conn, client_id):
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM phones WHERE client_id = %s;
    """, (client_id))
    conn.commit()
    cur.execute("""
    DELETE FROM client WHERE client_id = %s;
    """, (client_id))
    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM client c 
        JOIN phones p ON c.client_id = p.client_id 
        WHERE first_name=%s OR last_name=%s 
        OR email=%s OR p.phone=%s;
        """, (first_name, last_name, email, phone)) ;
    print(cur.fetchall())
with psycopg2.connect(database='hw', user="postgres", password="postgres") as conn:
    #add_phone(conn, 2, '222333')
    #create_db(conn)
    #add_client(conn, 2, 'fff', 'fff', 'ttt', '4555')
    #delete_phone(conn, '2', '4555')
    #change_client(conn,1 , phones='22')
    #delete_client(conn, '1')
    #find_client(conn, first_name='fff')
conn.close()