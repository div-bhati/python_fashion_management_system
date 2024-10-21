from database_connection import create_connection
from datetime import datetime

class OrderManager:
    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def create_order(self):
        customer_id = int(input("Enter customer ID: "))
        clothing_id = int(input("Enter clothing ID: "))
        quantity = int(input("Enter quantity: "))
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.cursor.execute('''
            INSERT INTO Orders (customer_id, clothing_id, quantity, order_date) 
            VALUES (%s, %s, %s, %s)
        ''', (customer_id, clothing_id, quantity, order_date))
        
        self.conn.commit()
        print("Order created successfully!")

    def view_orders(self):
        self.cursor.execute('SELECT * FROM Orders')
        orders = self.cursor.fetchall()
        for order in orders:
            print(order)

    def delete_order(self):
        order_id = int(input("Enter order ID to delete: "))
        self.cursor.execute('DELETE FROM Orders WHERE id = %s', (order_id,))
        self.conn.commit()
        print("Order deleted successfully!")

    def close(self):
        self.conn.close()
