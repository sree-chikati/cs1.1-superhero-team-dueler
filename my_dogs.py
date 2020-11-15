# my_dogs.py
import dog


# instantiation call that creates a Dog object:
my_dog = dog.Dog("Rex", "SuperDog")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()

print("\n")

my_other_dog = dog.Dog("Mochi", "SuperFluffyDog")
print(my_other_dog.name)
print(my_other_dog.breed)
my_dog.sit_down()

print("\n")

my_third_dog = dog.Dog("Nova", "SuperSpaceDog")
print(my_third_dog.name)
print(my_third_dog.breed)
my_dog.roll_over()