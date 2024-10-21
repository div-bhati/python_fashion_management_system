from database_connection import create_connection

class ClothingManager:
    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def add_clothing(self):
        name = input("Enter clothing name: ")
        category = input("Enter clothing category: ")
        price = float(input("Enter clothing price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        
        self.cursor.execute('''
            INSERT INTO Clothing (name, category, price, stock_quantity) 
            VALUES (%s, %s, %s, %s)
        ''', (name, category, price, stock_quantity))
        
        self.conn.commit()
        print("Clothing item added successfully!")

    def view_clothing(self):
        self.cursor.execute('SELECT * FROM Clothing')
        items = self.cursor.fetchall()
        for item in items:
            print(item)

    def update_clothing(self):
        clothing_id = int(input("Enter clothing ID to update: "))
        name = input("Enter new clothing name: ")
        category = input("Enter new clothing category: ")
        price = float(input("Enter new clothing price: "))
        stock_quantity = int(input("Enter new stock quantity: "))
        
        self.cursor.execute('''
            UPDATE Clothing 
            SET name = %s, category = %s, price = %s, stock_quantity = %s
            WHERE id = %s
        ''', (name, category, price, stock_quantity, clothing_id))
        
        self.conn.commit()
        print("Clothing item updated successfully!")

    def delete_clothing(self):
        clothing_id = int(input("Enter clothing ID to delete: "))
        self.cursor.execute('DELETE FROM Clothing WHERE id = %s', (clothing_id,))
        self.conn.commit()
        print("Clothing item deleted successfully!")

    def close(self):
        self.conn.close()
