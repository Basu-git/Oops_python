#**Inheritance**:
 #  - Create a base class `Vehicle` with a `start` method. Then create a subclass `Bike` with an additional `ride()` method.
 #  - Demonstrate how the `Bike` can use both `start` and `ride`.
class vehicle:
    def __init__(self):
        pass
    def start(self):
        print("Vehicle is Starting")
class bike(vehicle):
        pass
v=bike()
v.start()