# Given dictionaries
dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

# Find common keys using set intersection
common_keys = list(set(dict1.keys()) & set(dict2.keys()))

# Print result
print("Common keys:", common_keys)