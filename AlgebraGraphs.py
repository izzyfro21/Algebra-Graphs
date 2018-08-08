#Will not run on this online IDE must have python installed and matplotlib to run on your computer

#This imports the libraries required for this program
from matplotlib import pyplot as plt
import math

#This function creates a quadratic equation
def QuadraticEquation():
  abc = str(raw_input(
      "In the equation y= ax^2+bx+c, what is a, b, and c (display split each answer up by one space. EX: 1 4 5): "))
  print("")

  x_axis = int(input(
      "What is the maximum size of the graph you would like (in units EX: 10): "))
  print("")

  a, b, c = abc.split()
  a = int(a)
  b = int(b)
  c = int(c)

  x = []
  y = []
  i = 0
  while(i <= x_axis):
    x.append(i)
    y.append((a*i**2) + (b*i) + (c))
    i = i+1

  plt.plot(x, y, color="green")
  plt.show()

#This function creates am Exponential equation
def ExponentialEquation():
  print("For the equation y = (a^x)+bx+c")
  abc = str(raw_input("What are a, b, and c (EX: 1 2 3): "))
  x_axis = int(input(
      "What is the maximum size of the graph you would like (in units EX: 10): "))*2

  aa, bb, cc = abc.split()
  a = int(aa)
  b = int(bb)
  c = int(cc)

  x = []
  y = []

  i = 0
  while(i <= x_axis):
    x.append(i)
    y.append((a**i) + (b*i) + c)
    i = i+1

  plt.plot(x, y)
  plt.show()
  print(x)

#This function creates a linear equation
def LinearEquation():
  print("For the equation y = mx+b")
  mb = str(raw_input("What are m and b (EX: 1 2): "))
  x_axis = int(input(
      "What is the maximum size of the graph you would like (in units EX: 10)"))

  m, b = mb.split()
  m = int(m)
  b = int(b)

  x = []
  y = []

  i = 0
  while(i <= x_axis):
    x.append(i)
    y.append(m*i+b)
    i = i+1
  plt.plot(x, y)
  plt.show()


while(True):  
  equation = str(raw_input("What type of equation would you like to graph - Linear, Quadratic or Exponential: ")).lower()

  if(equation == "linear"):
    LinearEquation()
    break
  else:
    if(equation == "quadratic"):
      QuadraticEquation()
      break
    if(equation == "exponential"):
      ExponentialEquation()
      break
    else:
      print("Please type ina valid input")
