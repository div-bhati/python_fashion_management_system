from clothing import ClothingManager
from customers import CustomerManager
from orders import OrderManager

def main():
    clothing_manager = ClothingManager()
    customer_manager = CustomerManager()
    order_manager = OrderManager()

    while True:
        print("\nFashion Management System")
        print("1. Clothing Management")
        print("2. Customer Management")
        print("3. Order Management")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("\nClothing Menu")
                print("1. Add Clothing")
                print("2. View Clothing")
                print("3. Update Clothing")
                print("4. Delete Clothing")
                print("5. Back")
                
                clothing_choice = input("Enter your choice: ")
                
                if clothing_choice == '1':
                    clothing_manager.add_clothing()
                elif clothing_choice == '2':
                    clothing_manager.view_clothing()
                elif clothing_choice == '3':
                    clothing_manager.update_clothing()
                elif clothing_choice == '4':
                    clothing_manager.delete_clothing()
                elif clothing_choice == '5':
                    break
                else:
                    print("Invalid choice! Please try again.")

        elif choice == '2':
            while True:
                print("\nCustomer Menu")
                print("1. Add Customer")
                print("2. View Customers")
                print("3. Delete Customer")
                print("4. Back")
                
                customer_choice = input("Enter your choice: ")
                
                if customer_choice == '1':
                    customer_manager.add_customer()
                elif customer_choice == '2':
                    customer_manager.view_customers()
                elif customer_choice == '3':
                    customer_manager.delete_customer()
                elif customer_choice == '4':
                    break
                else:
                    print("Invalid choice! Please try again.")

        elif choice == '3':
            while True:
                print("\nOrder Menu")
                print("1. Create Order")
                print("2. View Orders")
                print("3. Delete Order")
                print("4. Back")
                
                order_choice = input("Enter your choice: ")
                
                if order_choice == '1':
                    order_manager.create_order()
                elif order_choice == '2':
                    order_manager.view_orders()
                elif order_choice == '3':
                    order_manager.delete_order()
                elif order_choice == '4':
                    break
                else:
                    print("Invalid choice! Please try again.")

        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

    clothing_manager.close()
    customer_manager.close()
    order_manager.close()

if __name__ == "__main__":
    main()
