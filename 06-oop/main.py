# simple word we need to create normal maker (form OR tempelet)
# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
# attributes (variable)

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.
# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.
# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.
# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

# 1. class keyword name must be start with uppercase
# 2. function defination with __init__ (constructer) only that can use on other 
#  3. than any attribute possible
class Car:
    # here self for current contex for connsection b/w 
    def __init__(self,brand,model): # object creation
        self.brand = brand;
        self.model = model;
    
    # making connsection b/w brand and model attribute 
    def print_Car_Info(self): # method
        return f'{self.brand} and {self.model}'

car1 = Car('Mahindra','Thar');


# print(car1.print_Car_Info())


class ElectricCar(Car): # here car as per para due to inheritances
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model); 
        # super keyword for accessing Car class with all atribute and methd
        # __init__ for brand and model attribute 
        # and take brand and model attribute
        self.battery_size = battery_size
        
ev_car = ElectricCar('tesla','model s','100kwh')

# print(ev_car.print_Car_Info())
print(isinstance(Car,ElectricCar))