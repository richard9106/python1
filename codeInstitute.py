# complex functions
""" instructions

build a function that:
 Takes a list of numbers as a parameters
retunr a list only the odd numbers from the original list
"""

first_numbers = [12, 45, 60, 87, 999, 200, 85, 77, 2, 3, 77, 99, 20]


def my_funtion(lis_of_numbers):
  new_list = []
  for i in lis_of_numbers:
    if i % 2 != 0:
      new_list.append(i)
  return new_list

result = my_funtion(first_numbers)
print (result) 