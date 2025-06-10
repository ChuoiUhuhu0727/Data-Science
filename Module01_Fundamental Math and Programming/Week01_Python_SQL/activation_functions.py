
# Exercise 2
import numpy as np

def calc_func(input_x: float, input_f: str) -> float:
  """
  Calculate activation function value
  Parameters:
    input_x (float): Input value
    input_f (str): Activation function name (sigmoid|relu|elu)
  Returns:
    output_calc (float): Activation function result
  """
  if input_f == "sigmoid":
    return (1 / (1 + np.exp(-input_x)))
  elif input_f == "relu":
    return max(0, input_x)
  elif input_f == "elu":
    return (0.01*(np.exp(input_x) - 1) if input_x <= 0 else input_x)
  else:
    raise ValueError("Function name not supported")

def interactive_activation_function():
  '''
  Main function:
    Input: the value and name of the function
    Output: calculate that function based on the value
  '''
  try:
    input_x = float(input("Input x = "))
  except (TypeError, ValueError):
    print("x must be a number")
    return

  input_f = input("Input activation Function (sigmoid|relu|elu): ").strip().lower().replace(" ", "")
  if input_f in ("sigmoid", "relu", "elu"):
    output_calc = calc_func(input_x, input_f)
    print(f"{input_f}: f({input_x}) = {output_calc}")
  else:
    raise ValueError("Function name not supported. Please choose from: sigmoid, relu, elu")

if __name__ == "__main__":
  interactive_activation_function()
