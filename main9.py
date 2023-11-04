import random
import sys
import time
import yaml


global current_language
global translations

def set_current_language(language):
  global current_language
  """Sets the current language."""
  current_language = language

def get_current_language():
  global current_language
  """Returns the current language."""
  return current_language

def get_translation(key):
  global current_language
  global translations
  """Retrieves the translation for the given key based on the current language."""
  translation = translations.get(current_language, {}).get(key)
  if translation is None:
    translation = key  # Fallback to key if translation is not found

  return translation

def generate_random_number(range_start, range_end):
  """Generates a random number in the range `range_start` to `range_end`.

  Args:
    range_start: The start of the range to generate random numbers from.
    range_end: The end of the range to generate random numbers from.

  Returns:
    A random number in the range `range_start` to `range_end`.
  """

  random_number = random.randint(range_start, range_end)
  return random_number

def show_number_for_delay(number, delay):
  """Shows the given number on the console for the given delay in seconds.

  Args:
    number: The number to show.
    delay: The delay in seconds to show the number for.
  """

  # Move the cursor up one line
  sys.stdout.write("\033[1A")

  # Delete the previous line
  sys.stdout.write("\033[2K")

  # Print the number
  print(number)

  # Flush the console output
  sys.stdout.flush()

  # Sleep for the given delay
  time.sleep(delay)

def get_user_guess():
  """Prompts the user to enter a guess and returns the user's guess."""
  user_guess = input(get_translation("prompt_guess"))
  return user_guess

def check_user_guess(user_guess, correct_sum):
  """Checks the user's guess and returns True if the guess is correct, False otherwise.
  Args:
    user_guess: The user's guess.
    correct_sum: The correct sum of the random numbers.

  Returns:
    True if the user's guess is correct, False otherwise.
  """

  correct_sum_string = str(correct_sum)
  if user_guess == correct_sum_string:
    return True
  else:
    return False

def main():
  global current_language
  global translations

  # Load translations from external files
  with open('translations.yaml', 'r', encoding='utf-8') as file:
    translations = yaml.safe_load(file)

  # Get program settings from the user
  range_start = int(input(get_translation("prompt_range_start")))
  range_end = int(input(get_translation("prompt_range_end")))
  amount = int(input(get_translation("prompt_amount")))
  time_delay = float(input(get_translation("prompt_time_delay")))

  # Generate random numbers and calculate the correct sum
  random_numbers = []
  for i in range(amount):
    random_number = generate_random_number(range_start, range_end)
    random_numbers.append(random_number)

  correct_sum = sum(random_numbers)

  # Show random numbers with delay
  for random_number in random_numbers:
    show_number_for_delay(random_number, time_delay)

  # Get the user's guess
  user_guess = get_user_guess()

  # Check the user's guess
  is_correct_guess = check_user_guess(user_guess, correct_sum)

  # Display the result
  if is_correct_guess:
    print(get_translation("correct_guess"))
  else:
    print(get_translation("incorrect_guess") + str(correct_sum))


if __name__ == "__main__":
  set_current_language("el")
  main()
