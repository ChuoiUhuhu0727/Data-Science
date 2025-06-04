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
