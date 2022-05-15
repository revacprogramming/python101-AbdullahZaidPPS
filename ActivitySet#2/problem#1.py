

def add(a, b):
  c=a+b
  return c


def main():
    a = float(input("Enter number"))
    b = float(input("Enter number"))
    sum = add(a, b)
    print("The sum of %f and %f is %f".format(a,b,sum))
