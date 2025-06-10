# Exercise: Activation Functions
def evaluate_f1_components(tp: int, fp:int, fn: int):
  """
  Compute precision, recall, and F1-score
  from counts of tp, fp, fn.
  """
  try:
    validate_input(tp, fp, fn)
    precision, recall, f1_score = compute_f1(tp, fp, fn)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")
  except ValueError as e:
    print(e)

def validate_input(tp: int, fp: int, fn: int) -> bool:
  for value, name in zip((tp, fp, fn), ("tp", "fp", "fn")):
    if not isinstance(value, int):
      raise ValueError(f"{name} must be int")
    elif value < 0:
      raise ValueError(f"{name} must >= 0")
  return True

def compute_f1(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
  if ((tp + fp) == 0) or ((tp + fn) == 0):
    raise ValueError("Dividend cannot be zero")
  else:
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

  if (precision + recall == 0):
    raise ValueError("Dividend cannot be zero")
  else:
    f1_score = 2 * (precision * recall)/(precision + recall)

  return precision, recall, f1_score

# Test Cases
evaluate_f1_components(tp=2, fp=3, fn=4)
evaluate_f1_components(tp="a", fp=3, fn=4)


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
