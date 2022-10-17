class PredictDigit(object):
  def __init__(self):
    self.true_digit = 0
    self.digit_percentage = ""
    self.all_digits = []

  def predict(self, digits, digit):
    try:
      digits = list(digits)
    except TypeError:
      raise TypeError("Inappropriate Values Type")
    try:
      digit = int(digit)
    except TypeError:
      raise TypeError("Predicted Digit must Be INT")
    self.all_digits = digits
    self.true_digit = digit
    digit_num = 0
    denominator = len(digits)
    for i in digits:
      if i == digit:
        digit_num += 1
    percent = (100 / denominator) * digit_num
    self.digit_percentage = f"{percent}%"
    return self.digit_percentage