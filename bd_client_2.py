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


def add_client(conn, client_id, first_name, last_name, email, phones=None):

    cur = conn.cursor()
    cur.execute("""
    INSERT INTO client(client_id, first_name, last_name, email) VALUES(%s, %s, %s, %s);
    """, (client_id, first_name, last_name, email))
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phones))




def add_phone(conn, client_id, phone):

    cur = conn.cursor()
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phone ))


def delete_phone(conn, client_id, phone=None):

    cur = conn.cursor()
    cur.execute("""
    DELETE FROM phones WHERE client_id = %s AND phone = %s;
    """, (client_id, phone))



def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    if first_name != None:
        cur = conn.cursor()
        cur.execute("""UPDATE client SET first_name = %s WHERE client_id = %s""", (first_name, client_id))
    if last_name != None:
        cur = conn.cursor()
        cur.execute("""UPDATE client SET last_name = %s WHERE client_id = %s""", (last_name, client_id))
    if email != None:
        cur = conn.cursor()
        cur.execute("""UPDATE client SET email = %s WHERE client_id = %s""", (email, client_id))
    if phones != None:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO phones(client_id, phone) VALUES(%s, %s);""", (client_id, phones))
        cur.close()

def delete_client(conn, client_id):
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM phones WHERE client_id = %s;
    """, (client_id))
    cur.execute("""
    DELETE FROM client WHERE client_id = %s;
    """, (client_id))

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM client c 
        JOIN phones p ON c.client_id = p.client_id 
        WHERE (first_name = %(first_name)s OR %(first_name)s IS NULL)
        AND (last_name = %(last_name)s OR %(last_name)s IS NULL)
        AND (email = %(email)s OR %(email)s IS NULL)
        AND (phone = %(phone)s OR %(phone)s IS NULL);
        """, {"first_name": first_name, "last_name": last_name, "email": email, "phone": phone})
    print(cur.fetchall())
if __name__ == "__main__":
    with psycopg2.connect(database='hw', user="postgres", password="srwntxpa") as conn:
        #add_phone(conn, 5, '452')
        #create_db(conn)
        #add_client(conn, 5, 'f', 'l4', 'email', '4555')
        #delete_phone(conn, '2', '4555')
        #change_client(conn,1 , phones='22')
        #delete_client(conn, '4')
        find_client(conn, first_name='f', last_name='l')
    conn.close()