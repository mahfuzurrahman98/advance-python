class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Woof! Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow!'


class Duck(Animal):
    def speak(self):
        return 'Quack!'

# Function demonstrating polymorphism


def animal_sound(animal):
    return animal.speak()


# Creating instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# Using the common interface (speak method) for different objects
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(duck))  # Output: Quack!
