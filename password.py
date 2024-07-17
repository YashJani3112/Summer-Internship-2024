def check_password_strength(password):
  """
  Evaluates the strength of a password based on various criteria.

  Args:
      password: The password to be assessed.

  Returns:
      A tuple containing:
          - Strength level (string: "Weak", "Medium", "Strong")
          - Feedback message (string) explaining the strength assessment
  """
  minimum_length = 8
  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_special = any(char in '!@#$%^&*()-_=+[]{};:,<.>/?\|`~' for char in password)

  score = 0
  if len(password) >= minimum_length:
    score += 1
  if has_uppercase:
    score += 1
  if has_lowercase:
    score += 1
  if has_digit:
    score += 1
  if has_special:
    score += 1

  strength_level = "Weak"
  feedback = ""
  if score == 0:
    feedback = "This password is extremely weak. Please consider using a longer password with a mix of uppercase, lowercase letters, numbers, and special characters."
  elif score <= 2:
    strength_level = "Medium"
    feedback = "This password is somewhat weak. It could be strengthened by adding more character types (uppercase, lowercase, numbers, special characters)."
  elif score == 3 or score == 4:
    strength_level = "Medium"
    feedback = "This password is moderately strong. Consider adding one more character type for extra security."
  else:
    strength_level = "Strong"
    feedback = "This is a strong password! It meets all the recommended criteria for password security."

  return strength_level, feedback

def main():
  password = input("Enter your password: ")
  strength_level, feedback = check_password_strength(password)
  print(f"Password Strength: {strength_level}")
  print(feedback)

if __name__ == "__main__":
  main()
