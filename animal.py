class Animal(object):
    #class variable
    count = 0 
    #def __init__(self, name,health =150):
    # this will protect u incase user does not provide a health input 
    def __init__(self, name, health):
        self.name = name
        self.health = health
        # count 
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -=5
        return self
    def displayHealth(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self,name,health = 150):
        print "inside dog"
        super (Dog, self).__init__(name, health)  
        # self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name, health =170):
        super(Dragon,self).__init__(name,health)
    def displayHealth(self):

        super(Dragon,self).displayHealth()
        print "Hi i am a dragon"
    def fly(self):
        self.health -= 10
dragon1 = Dragon("fireDragon")
dragon1.displayHealth()
dragon1.displayHealthDragon()
dragon1.fly()



# animal1 = Animal("tommy", 11)
# print ("name {} health {} ").format(animal1.name, animal1.health)
# # print animal1.walk().walk()
# print animal1.health

# myDog = Dog ("Rover")
# myDog.displayHealth()