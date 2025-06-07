# Flatten a nested tuple
# Example: (1, (2, 3), 4) -> [1, 2, 3, 4]

nested = (1, (2, 3), 4)
flat = []
for item in nested:
    if isinstance(item, tuple):
        flat.extend(item)
    else:
        flat.append(item)
print(flat)
