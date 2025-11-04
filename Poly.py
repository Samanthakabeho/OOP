class Animal:
    def speak(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        
class Cat(Animal):
    def speak(self):
        print("Cat meow get out of the way")
        
for animal in (Animal(), Dog(), Cat()):
    animal.speak()