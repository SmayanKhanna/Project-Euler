#Euler 2: Solved Easily: Final Answer 4613732

def Fib(n):
    x = 1
    y = 1
    z = 0
    while y < 4000000:
      x,y = y,x + y
      if y % 2 == 0:
          z += y
    return z
     
print(Fib(10))

