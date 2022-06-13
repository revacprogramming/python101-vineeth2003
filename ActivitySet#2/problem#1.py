
def add(a, b):
    return(a, b)


def main():
    a = input('enter first number: ')
    b = input('enter second number: ')
    c = a + b
    c = add(a, b)
    return(c)
    print(c)
