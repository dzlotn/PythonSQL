import sqlite3
from sqlite3 import Error
def create_connection(db):
    try:
        conn = sqlite3.connect(db)          #create connection & return it
        print("Database connection established")
        return conn
    except Error as e: 
        print(e)
    return None
def select_orderItems(conn):
    cur = conn.cursor()
    cur.execute('''SELECT prod_id, quantity, item_price, quantity*item_price*1.07 AS 'taxed_price(7%)' FROM OrderItems WHERE order_num = 20006;''')
    rows= cur.fetchall()
    cur.close()
    return (rows)
def insert_product (conn,product):
    sql = '''INSERT INTO Products(prod_id,vend_id,prod_name,prod_price,
    prod_desc) VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,product)
    conn.commit()
    cur.close()
    return cur.lastrowid

def insert_vendor (conn,product):
    sql = '''INSERT INTO Vendors(vend_id,vend_name,vend_address,vend_city,vend_zip,
    vend_country, vend_web) VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,product)
    conn.commit()
    cur.close()
    return cur.lastrowid

def select_products(conn):
    cur=conn.cursor()
    cur.execute("SELECT * FROM Products;")
    rows=cur.fetchall()
    cur.close()
    return(rows)

def select_vendor(conn,vendor):

    cur=conn.cursor()
     
    cur.execute("SELECT * FROM Vendors WHERE vend_id = ?",vendor)
    rows=cur.fetchall()
    cur.close()
    return(rows)
def update_customer (conn,custID,contactInfo):
    cur = conn.cursor()
    cur.execute('''UPDATE Customers SET cust_name = ?, cust_email=? WHERE cust_id=?''',[contactInfo[0],contactInfo[1],custID])
    conn.commit()
    cur.close()
    return(cur.lastrowid)
    
def select_customer(conn,customer):
    cur=conn.cursor() 
    cur.execute("SELECT cust_name, cust_email FROM Customers WHERE cust_id = ?",customer)
    rows=cur.fetchall()
    cur.close()
    return(rows)
