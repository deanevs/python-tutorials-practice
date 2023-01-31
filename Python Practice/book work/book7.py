class animal:
    type = 'mammal'

class dog(animal):
    breed = "unknown"
    def setbreed(x):
        breed = x



mydog = dog()
print (mydog.breed)
mydog.setbreed('labradaor')
print (mydog.breed)