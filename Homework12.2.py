class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Product: {self.name}\nPrice: {self.price} uah\nDescription: {self.description}\nDimensions: {self.dimensions}"


class Customer:
    def __init__(self, first_name, last_name, middle_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"Buyer: {self.first_name} {self.middle_name} {self.last_name}\nTelephone: {self.phone}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product, quantity):
        self.products.append({'product': product, 'quantity': quantity})

    def total_cost(self):
        total = 0
        for item in self.products:
            total += item['product'].price * item['quantity']
        return total

    def __str__(self):
        order_details = f"Order for {self.customer.first_name} {self.customer.last_name}:\n"
        for item in self.products:
            order_details += f"- {item['product'].name}, Number: {item['quantity']}, Price: {item['product'].price} uah\n"
        order_details += f"Total order cost: {self.total_cost()} uah"
        return order_details

product1 = Product("Notebook", 15000, "new laptop", "35x24x2 length")
product2 = Product("Car", 350000000, "Luxus car", "very big")

customer1 = Customer("Valentyn", "Novikov", "admboxovich", "+80669848065")

order1 = Order(customer1)

order1.add_product(product1, 1)
order1.add_product(product2, 2)

print(order1)