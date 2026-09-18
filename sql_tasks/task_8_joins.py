import sqlite3

def get_customer_spend():

    #print ("I am in the get customer spend function")
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query ="""
    SELECT i.price * i.quantity 
    FROM Customers c 
    JOIN Orders o
    JOIN Order_Items i 
    WHERE c.customer_id = o.customer_id 
    """
    
    cursor.execute(query)

    for row in cursor: 
        print(row)


    results = cursor.fetchall()

    
    conn.close()
    return results

if __name__ == "__main__":
    get_customer_spend()