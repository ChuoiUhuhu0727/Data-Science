def get_min(data) :
  return min(data)

data1 = [1 , 5 , 2 , 91 , -10]
assert get_min(data1) == -10

data2 = [2 , 5 , -5 , 10 , 11]
print(get_min(data2))

def count (data, value):
  return sum(1 for i in data if i == value)

data1 = [1 , 5 , 2 , -10 , 5 , 10 , 5]
assert count(data1, 5) == 3, "incorrect"
print("Hurayy that is correct")

data2 = [5 , 4 , 2 , 10 , 4 , 8 , 1 , 3]
print(count(data2, 4))

def get_sum(data):
  return sum(i for i in data)

data1 = [1,5,2,8,-1]
assert get_sum(data1) == 15

data2 = [5 , 4 , 2 , 10 , 4]
print (get_sum(data2))

def get_sum_even(data):
   return sum(i for i in data if i % 2 == 0)

data1 = [1 , 5 , 2 , 4 , -10 , 5]
assert get_sum_even ( data1 ) == -4

data2 = [5 , 4 , 2 , 10 , 3 , 8]
print ( get_sum_even ( data2 ) )

import numpy as np

def get_mean(data):
  return np.mean(data)

data1 = [1 , 5 , 2 , 7 , -3]
assert np.isclose(get_mean(data1), 2.4)

data2 = [2 , 5 , -5 , 10 , 11]
print(get_mean(data2))

def contain(data, value):
  return any(i == value for i in data)

data1 = [1 , 5 , 2 , 91 , -10]


# print(contain(data1, 5))
assert contain(data1, 5) == True

data2 = [2 , 5 , -5 , 10 , 11]
print(contain(data2, 3))

def compute_precision(TP, FP):
  return round(TP/(TP + FP), 2)

def compute_recall(TP, FN):
  return round(TP/(TP+FN), 2)

def compute_f1_score(precision, recall):
  return round(2 * (precision * recall)/(precision + recall), 2)

def lie_truth(y_hat, y):
  if (y_hat < 0.5 and y == 0) or (y_hat >= 0.5 and y == 1):
    r = 1
  else:
    r = 0
  return r

print(lie_truth(0.3, 0))
print(lie_truth(0.8, 0))
print(lie_truth(0.7, 0))
print(lie_truth(0.4, 0))


print(lie_truth(0.6, 1))
print(lie_truth(0.8, 1))
print(lie_truth(0.9, 1))
print(lie_truth(0.2, 1))

# Get accustomed to docstring function
def sum_function(num1, num2):
  '''
  Sum of two numbers
  input: num1, num2
  output: num1+num2
  '''
  return num1 + num1

print(sum_function.__doc__)

def reverse_string(x):
  res = ""
  for i in x: 
    res = i + res
    print("res here is: ", res)
  return res

x = "apricot"
print(reverse_string(x))

# PI Estimation: Gregory-Leibniz Series
n = 1000
PI = 0
for i in range(1, n + 1):
  PI += ((-1)**(i+1))/(2*i - 1)
PI = PI*4 

print("Estimated PI is ", PI)

# Calculate area of half circles
import math

length = 2
delta = 0.1
area = 0

num_rectangles = length/delta
print("num rectangles are: ", num_rectangles)

def get_y(x):
  return math.sqrt(1-x*x)

x = -1.0
for _ in range(int(num_rectangles)):
  # current
  y = get_y(x)
  print(x, y)

  area = area + y*delta

  # update
  x = x + delta

print(area*2)
