
def add(a, b):
 (a,b) = input_two_numbers()


def output(a, b, sum):
  sum = a + b


def main():
    a, b = input_two_numbers()
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    sum = add(a, b)
    sum = a + b
    output(a, b, sum)


if __name__ == '__main__':
    main()
