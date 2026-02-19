data_list = [
    ("apple", "fruit"),
    ("carrot", "vegetable"),
    ("banana", "fruit"),
    ("broccoli", "vegetable"),
    ("dog", "animal"),
    ("cat", "animal")
]
grouped_items = {}
for item, category in data_list:
    if category in grouped_items:
        grouped_items[category].append(item)
    else:
        grouped_items[category] = [item]
print(grouped_items)