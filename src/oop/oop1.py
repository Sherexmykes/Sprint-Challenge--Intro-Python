# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle: #this is the base class of Vehichle
    pass

class FlightVehicle(Vehicle): # this is the parent class for airplane
    pass

class Starship(FlightVehicle): # this class has no children
    pass

class GroundVehicle(Vehicle): # this is the parent class for Car & Motorcycle
    pass

class Airplane(FlightVehicle): # child class
    pass

class Car(GroundVehicle):   # child class
    pass

class Motorcycle(GroundVehicle):  # child class
    pass