# Original list with mixed data
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

# Create a new list with only numbers (integers or floats)
cleaned_list = [item for item in data_list if type(item) == int or type(item) == float]

# Print the cleaned list
print("Cleaned list with only numbers:", cleaned_list)