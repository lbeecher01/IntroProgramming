# This program will add cars and pickup trucks into a list using classes
print("Welcome to Virtual Garage.")
class Vehicle:
  
  def __init__ (self, make, model) :
    self.make = make
    self.model = model

  def getMake(self) :
    return self.make

  def getModel(self) :
    return self.model

class Car(Vehicle):

  def __init__(self, make , model, carDoors):
    super().__init__(make, model)
    self.carDoors = carDoors

  def getCarDoors(self):
    return self.carDoors

class Pickup(Vehicle):

  def __init__(self, make , model, bedLength):
    super().__init__(make, model)
    self.bedLength = bedLength

  def getBedLength(self):
    return self.bedLength

def main():
  garage = []

  while True:
    print("Menu:\n1. Add a car to the garage\n2. Add a pickup to the garage\n3. Exit")

    option = int(input("Enter a choice: "))

    while option < 1 or option > 3:
       option = int(input("Invalid choice. Try again: "))

    if option == 3:
      break

    make = input("Enter a make: ")
    model = input("Enter a model: ")

    if option == 1:
      carDoors = int(input("Enter a number of doors: "))

      garage.append(Car(make, model, carDoors))

      print()

    elif option == 2:
      bedLength = float(input("Enter the bed length: "))

      garage.append(Pickup(make, model, bedLength))
      

    if len(garage) == 0:
        print("The garage is empty.")

    else:
      print("The vehicles in the garge include:")
      for vehicle in garage:
        print("Make: " + vehicle.getMake())
        print("Model: " + vehicle.getModel())
        
      if isinstance(vehicle, Car):
        print("Number of Doors: " + str(vehicle.getCarDoors()))

      elif isinstance(vehicle, Pickup):
        print("Bed Length: " + str(vehicle.getBedLength()) + " foot") 

if __name__ == "__main__":
  main()
