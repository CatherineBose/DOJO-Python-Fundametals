class Store(object):
    def __init__(self, location, ownerName):
        self.products = []
        self.location = location 
        self.owner = ownerName
    
    def add_product(self, productObj):
        # add_product: add a product to the store's product list
        print "Inside add_product"
        self.products.append(productObj)
        for i in range (0, len(self.products)):
        # def __init__(self,price,name,weight,brand,cost):# 
            print self.products[i].price
            print self.products[i].name
            print self.products[i].weight
            print self.products[i].brand
            print self.products[i].cost
        

        return self

    def remove_product(self, productName):
    # remove_product: should remove a product according to the product name
        print "Inside remove_product"
        print "remove", productName.name
        print len(self.products)
        lengthProducts =len(self.products)
        # for i in range (0,lengthProducts):
        #     print self.products[i].name 
        for i in range (0,len(self.products)):
            if (self.products[i].name == productName.name):
                print productName.name
                del self.products[i]
        #         index = i
                # # removedProduct = self.products[index]
                # del self.products[index]
                # # product = self.products[i]remove()
                # print "Removed product :: "
                # print self.removedProduct.price
                # print self.removedProduct.name
                # print self.removedProduct.weight
                # print self.removedProduct.brand
                # print self.removedProduct.cost
        return self

    def inventory(self):
    # inventory: print relevant information about each product in the store
       print "Inside Inventory method" 
       for i in range(0, len(self.products)):
            print self.products[i].price
            print self.products[i].name
            print self.products[i].weight
            print self.products[i].brand
            print self.products[i].cost
            return self

class Product(object):
    def __init__(self,price,name,weight,brand,cost):
         self.price = price
         self.name = name
         self.weight = weight
         self.brand = brand 
         self.cost = cost
         self.status="for sale"
         self.tax= 0
         
    def sell(self):
        self.status="sold"
        print "Status for 1st sale: ", self.status
        return self
    def addTax(self,percent):
        tax = self.price * percent
        totalPrice = self.price + tax
        print "Total Price: ", totalPrice
        return totalPrice
    def returnReason(self,reason):
        print "Product is being returned: check reason and see if it can be put back for sale!!!"
        if (reason=="defective"):
            self.status= "defective"
            self.price= 0
            print "reason: ",reason
            print "self.stat: ",self.status
            print "price: ", self.price
        elif(reason=="like new"):
            self.status="for sale"
            print "reason: ",reason
            print "self.stat: ",self.status
            print "price: ", self.price
        elif(reason=="opened box"):
            discount = self.price *.20
            print "Discount for a open box is :", discount
            self.status="used"
            self.price =  self.price - discount 
            print "reason: ",reason
            print "self.stat: ",self.status
            print "price: ", self.price  
        return self
    def dispayInfo(self):
        print "Price:", self.price
        print "name:", self.name
        print "weight:", self.weight
        print "brand:", self.brand
        print "cost:", self.cost
        print "status:", self.status

# def __init__(self,price,name,weight,brand,cost):# 
chair = Product(500,"Arm Chair","50 pound","Rooms To Go", 300 )
chair.sell()
chair.dispayInfo()
chair.addTax(.10)
chair.returnReason("like new")

sofa = Product(2500,"Sofa","150 pounds","Rooms To Go", 1700 )
sofa.sell()
sofa.dispayInfo()
sofa.addTax(.10)
sofa.returnReason("defective")


loveseat = Product(2500,"Love Seat","100 pounds","Rooms To Go", 1300 )
loveseat.sell()
loveseat.dispayInfo()
loveseat.addTax(.10)
loveseat.returnReason("opened box")

armChair = Product(2500,"armChair","100 pounds","Henley", 1500 )

# # location, ownerName
AshleyFurniture = Store("San Jose", "Lucas")
print "location {}  owner {}".format(AshleyFurniture.location, AshleyFurniture.owner)
#Adding a product
AshleyFurniture.add_product(loveseat)
AshleyFurniture.add_product(chair)
AshleyFurniture.add_product(sofa)
# AshleyFurniture.inventory()
AshleyFurniture.remove_product(chair)

# Ramos = Store("Fremont", "Sandy")
# Ramos.add_product(armChair)