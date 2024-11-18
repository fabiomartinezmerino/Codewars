a = [1, 2, 2, 3, 4, 4, 5]

# Create an empty list to store unique values
res = []

# Use list comprehension to append values to 'res'
# if they are not already present
[res.append(val) for val in a if val not in res]

print(res)