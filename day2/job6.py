class Order:
    def __init__(self,order_id,products,status):
        self.__order_id = order_id
        self.__products = products
        self.__status = status
    def add_product(self,product):
        self.__products.append(product)
    def get_products(self):
        return self.__products
    def get_order_id(self):
        return self.__order_id
    def get_status(self):
        return self.__status
    def set_status(self,status):
        self.__status = status
    def __str__(self):
        return 'Order ' + str(self.__order_id) + ' has ' + str(len(self.__products)) + ' products'
order = Order(1,['apple','banana','orange'],'pending')
print(order)
order.add_product('kiwi')
print(order.get_products())
print(order.get_status())
order.set_status('delivered')
print(order.get_status())
print(order)