def pay():
  try :
    hrs = input("Enter hours? ")
    rate = input("Enter rate ")
    pay = rate * hrs
    print("pay: ")
  except :
    print(" Enter the numeric value, pay ")

pay()