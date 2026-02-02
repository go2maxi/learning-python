# Example 1: Missing 'self' on purpose
class Dog:
    def bark():
        print("woof")

my_dog = Dog()

# This will raise a TypeError because Python implicitly
# passes the instance as the first argument.
my_dog.bark()


# Example 2: Correct method definition
# Redefining the class correctly after observing the error
class Dog:
    def bark(self):
        # 'self' refers to the instance that calls the method.
        print("woof")

my_dog = Dog()
my_dog.bark()



# Experiment: self refers to the instance itself
class Dog:
    def show_id(self):
        print("id(self):", id(self))

my_dog = Dog()
print("id(my_dog):", id(my_dog))
my_dog.show_id()
