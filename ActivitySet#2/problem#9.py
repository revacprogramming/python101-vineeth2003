

class Menu(dict):
  def food(self,idly,vada):
    self.idly = self.idly + 20
    print("idly", self.idly)
    self.vada = self.vada + 20
    print("vada", self.vada)

class Order:
  def item(self,vada,pongal):
    self.vada = self.vada + 2
    print("vada", self.vada)
    self.pongal = self.pongal + 2
    print("pongal", self.pongal)
  


class Bill:
  def total(self,m,o):
    self.m = self.idly + self.vada
    print("bill of m", self.m)
    self.o = self.vada + self.pongal
    print("bill of o", self.o)


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
