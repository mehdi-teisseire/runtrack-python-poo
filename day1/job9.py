class Product:
    def __init__(self, name, price_without_tax, tax_rate):
        self.name = name
        self.price_without_tax = price_without_tax
        self.tax_rate = tax_rate
    
    def calculate_total_price(self):
        return self.price_without_tax * (1 + self.tax_rate)
    
    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price Without Tax: {self.price_without_tax} €")
        print(f"Tax Rate: {self.tax_rate * 100}%")
        print(f"Total Price: {self.calculate_total_price()} €")
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_price(self, new_price):
        self.price_without_tax = new_price
    
    def get_name(self):
        return self.name
    
    def get_price_without_tax(self):
        return self.price_without_tax
    
    def get_tax_rate(self):
        return self.tax_rate

product1 = Product("Smartphone", 500, 0.20)
product2 = Product("Laptop", 1200, 0.20)
product3 = Product("Earphones", 100, 0.10)

print("Initial Products:")
product1.display_info()
print("\n")
product2.display_info()
print("\n")
product3.display_info()

print("\nModifying Products:")
product1.change_name("Pro Smartphone")
product1.change_price(600)

product2.change_name("Gaming Laptop")
product2.change_price(1500)

product3.change_name("Wireless Earphones")
product3.change_price(150)

print("\nModified Products:")
product1.display_info()
print("\n")
product2.display_info()
print("\n")
product3.display_info()

print("\nRetrieving Information:")
print(f"First product name: {product1.get_name()}")
print(f"Second product price without tax: {product2.get_price_without_tax()} €")
print(f"Third product tax rate: {product3.get_tax_rate() * 100}%")