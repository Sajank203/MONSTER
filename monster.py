class monster:


    #Attributes
    health = 90
    energy = 40
    

    # methods
def attack(self,amount):
    print('The onster has attacked!')
    print(f'{amount} damage was dealt')
    monster.energy -= 20
    print(monster.energy)

def move(self,speed):
    print('The monster has moved') 
    print(f' It has speed of {speed}')   

monster1 = monster() 
monster2 = monster()

print(monster1.health)
print(monster.health)


