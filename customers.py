from database_connection import create_connection

class CustomerManager:
    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def add_customer(self):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        
        self.cursor.execute('''
            INSERT INTO Customers (name, email, phone) 
            VALUES (%s, %s, %s)
        ''', (name, email, phone))
        
        self.conn.commit()
        print("Customer added successfully!")

    def view_customers(self):
        self.cursor.execute('SELECT * FROM Customers')
        customers = self.cursor.fetchall()
        for customer in customers:
            print(customer)

    def delete_customer(self):
        customer_id = int(input("Enter customer ID to delete: "))
        self.cursor.execute('DELETE FROM Customers WHERE id = %s', (customer_id,))
        self.conn.commit()
        print("Customer deleted successfully!")

    def close(self):
        self.conn.close()
