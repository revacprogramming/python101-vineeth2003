# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
class Car:
  Wheel = 6
  def __init__(self):
    self.mil = 10
    self.company = 'Honda'

c1 = Car()
c2 = Car()

#print(c1.company)

c2.company = 'Maruthi'

print(c1.company)
print(c2.company)

print('-------------------------')

print(c1.Wheel)
print(c2.Wheel)