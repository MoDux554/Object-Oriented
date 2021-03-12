# class Dog:
#     species = "Three Heads" #same for all CLASS instances
#
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self): #the string will now be returned
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound ):
#         return f"{self.name} barks:{sound}"
#
#
#
# class JackRusselTerrier(Dog):
#     def speak(self, sound = "Arf" ): #method is the same name to be overriden
#         # return f"{self.name} says {sound}"
#         return super().speak(sound) #super allows the child to access the parent class dog for
#
# class GoldRetriever(Dog):
#     def speak(self, sound = "Bark" ):
#         return super().speak(sound) #accessing the parent class with super and passing the Bark sound into it
#
# class Dachshund(Dog):
#     pass
# class Bulldog(Dog):
#     pass
#
#
#
# buddy = Dachshund("Buddy", 4)
# print(buddy)
# jack = Bulldog("Jack", 3)
#
# miles = JackRusselTerrier("Miles", 2)
#
# print(miles.speak())
# print(buddy.speak("bark"))
#
# jim = Bulldog("Jim", 4)
# print(jim.speak("ARGH"))
#
# gold = GoldRetriever("Gold", 6)
# print(gold)
# print(gold.speak())


# class Car:
#
#     def __init__(self, colour, mileage):
#         self.colour = colour
#         self.mileage = mileage
#
#
# blue_car = Car(colour = "blue", mileage = 20000)
# red_car = Car(colour = "red", mileage= 30000)
#
# for car in blue_car, red_car:
#     print(f" the {car.colour} has {car.mileage} miles")


class MyClass():
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def instance_method(self):
        return f"This is the instance method and it can access the variables a={self.a} and b= {self.b} with the help of self"


obj = MyClass(1,2)
print(obj.instance_method())
