def get_keys_by_value(my_dict, target_value):
  return [key for key, value in my_dict.items() if value == target_value]

students = {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}
target = 20
matching_keys = get_keys_by_value(students, target)
print(matching_keys)
