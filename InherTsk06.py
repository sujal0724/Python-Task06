
class Sales:
    def __init__(self, s_id, s_order_date, s_ship_date, s_ship_mode, s_customer_id, s_customer_name, s_segment):
        self.s_id = s_id
        self.s_order_date = s_order_date
        self.s_ship_date = s_ship_date
        self.s_ship_mode = s_ship_mode
        self.s_customer_id = s_customer_id
        self.s_customer_name = s_customer_name
        self.s_segment = s_segment
        self.s_country = 'India'

class Product(Sales):
    def __init__(self, s_id, s_order_date, s_ship_date, s_ship_mode, s_customer_id, s_customer_name, s_segment, product_id, product_name, category):
        super().__init__(s_id, s_order_date, s_ship_date, s_ship_mode, s_customer_id, s_customer_name, s_segment)
        self.product_id = product_id
        self.product_name = product_name
        self.category = category

class Customer(Sales):
    def __init__(self, s_id, s_order_date, s_ship_date, s_ship_mode, s_customer_id, s_customer_name, s_segment, email, phone, address):
        super().__init__(s_id, s_order_date, s_ship_date, s_ship_mode, s_customer_id, s_customer_name, s_segment)
        self.email = email
        self.phone = phone
        self.address = address


sales_obj = Sales(1, '2025-07-01', '2025-07-03', 'Express', 101, 'John Doe', 'Consumer')
print('Sales Object:')
print(vars(sales_obj))

product_obj = Product(2, '2025-07-02', '2025-07-04', 'Standard', 102, 'Jane Smith', 'Corporate', 'P001', 'Laptop', 'Electronics')
print('\nProduct Object:')
print(vars(product_obj))

customer_obj = Customer(3, '2025-07-03', '2025-07-05', 'Same Day', 103, 'Alice Brown', 'Home Office', 'alice@email.com', '1234567890', '123 Main St')
print('\nCustomer Object:')
print(vars(customer_obj))





