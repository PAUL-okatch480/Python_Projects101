def get_low_stock_alerts(inventory_list):
    # Steps 2-5: Using a list comprehension to filter and extract names efficiently
    low_stock_items = [
        item['name'] for item in inventory_list if item.get('stock', 0) < 10
    ]
    
    # Steps 6-9: Handle the output formatting
    if not low_stock_items:
        return "All stock levels are good."
    else:
        # Join the list of strings into a single comma-separated string
        items_string = ", ".join(low_stock_items)
        return f"Low stock warning for: {items_string}"

# --- Testing the code ---
warehouse_inventory = [
    {"name": "Laptops", "stock": 45},
    {"name": "Keyboards", "stock": 8},
    {"name": "Monitors", "stock": 12},
    {"name": "Mice", "stock": 3}
]

print(get_low_stock_alerts(warehouse_inventory))
# Output: Low stock warning for: Keyboards, Mice
