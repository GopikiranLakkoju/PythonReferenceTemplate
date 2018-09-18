class Enemy(object):
    def attack(self):
        print("Attack who?")

class Hero(Enemy): #inheritance
    def attack(self):
        #polymorphism, when child defines the same method name based on the instance created on it shows that method implementation
        print("I know who to attack")        
