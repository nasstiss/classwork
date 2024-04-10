class Dog:
    name='unknown'

    def __init__(self ):
       self.is_walked = False
       seif.speed = '22'
    
    def walked(self): 
        print('Dog walked')
        self.is_walked = True

class DogSpike(Dog): 
    name = 'Spike'

    class DogMike(Dog):
        name = 'Mike'
    
my_dog = DogSpike() 
friends_dog = DogMike() 

print('my dog name:', my_dog.name) 
# print(my_dog.is_walked)
# my_dog.walk()
print('friends dog name;', friends_dog.name) 