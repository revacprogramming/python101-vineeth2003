# Functions


def computepay(hrs, rte) :
  hrs = float(input("Enter hours? "))
  rte = float(input("Enter rate per hour? "))
  computepay = hrs * rte
  return computepay

p = computepay(45, 10)
print( p)


