class Customer:
    Name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print('added to : ',self.Name,self.lastName,'cart')

customer1 = Customer()
customer1.Name = "John"
customer1.lastName = "Doe"
customer1.addCart()
