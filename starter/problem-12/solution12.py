# Given lists
list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

# Find common items (using set for unique values)
common_items = list(set(list1) & set(list2))

# Calculate the sum of common items
sum_common = sum(common_items)

# Print results
print("Common items:", common_items)
print("Sum of common items:", sum_common)