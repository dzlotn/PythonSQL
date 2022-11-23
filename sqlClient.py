import sqlite3,sqlLib
from sqlite3 import Error
def OIresult(rows):
    print("{0:^14} {1:^14} {2:^15} {3:^13}".format(
        "Product ID","Quantity","Item Price ($)","Tax Price ($)"
    ))

    print("{0:^14} {1:^14} {2:^15} {3:^13}".format("-"*14,"-"*14,"-"*14,"-"*13,))
    for row in rows:
        prodID=row[0]
        quant = int(row[1])
        itemPrice = float(row[2])
        taxPrice = float(row[3])
        print("{0:^14} {1:^14} {2:^15.2f} {3:^13.2f}".format(
        prodID,quant,itemPrice,taxPrice))

def prodInsertInputs():
    p=[]
    print("Please enter the following information: ")
    pid = input("Enter the product id: ")
    p.append(pid)
    vendor = input("Enter the vender id (BRS01, BRS02, DLL01, FRB01, JTS01): ")
    p.append(vendor)
    name= input("Enter the product name (255 char max): ")
    p.append(name)
    price = float(input("Enter the product price: "))
    p.append(price)
    desc = input("Enter the product description: ")
    p.append(desc)
    return(p)

def prodResult(rows):
    print("{0:^13} {1:^13} {2:^20} {3:^15} {4:^46}".format(
        "Product ID", "Vendor ID", "Name", "Price ($)", "Description"
    ))
    print("{0:13} {1:13} {2:20} {3:15} {4:46} ".format
    ("-"*13,"-"*13,"-"*20,"-"*15,"-"*46))
    for row in rows:
        prodID=row[0]
        vendID = row[1]
        name=row[2]
        price = float(row[3])
        desc = row[4] 
        print("{0:^13} {1:^14} {2:^20} {3:^16.2f} {4:<40}".format(
        prodID,vendID,name,price,desc))

def main():
    database = "tysql_copy.sqlite"
    conn = sqlLib.create_connection(database)

    # result = sqlLib.select_orderItems(conn)
    # OIresult(result)

    # product = prodInsertInputs()
    # rowID = sqlLib.insert_product(conn,product)
    # print(rowID)

    #  products = sqlLib.select_products(conn)
    #  prodResult(products)
    # print(sqlLib.update_customer(conn,1000000005,["Carolyn fklsdk","fern@toystore.com"]))
    print(sqlLib.select_customer(conn,[1000000004]))
if __name__ == '__main__':
    main()
