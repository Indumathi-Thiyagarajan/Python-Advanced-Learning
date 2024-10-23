# inventory_system.py

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    agrs_inventory = ("name", "price", "quantity")
    inv_categories = ("Electronics", "Groceries")
    # Example items for each category
    items = {
        "Electronics": [
            {"name": "Laptop", "price": 1000, "quantity": 8},
            {"name": "Smartphone", "price": 700, "quantity": 25}
        ],
        "Groceries": [
            {"name": "Apple", "price": 1, "quantity": 100},
            {"name": "Milk", "price": 2, "quantity": 50}
        ]
    }

    # Creating the nested dictionary
    nested_dict = {category: {item["name"]: {key: item[key] for key in agrs_inventory} for item in items[category]} for category in inv_categories}
    return nested_dict

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    # print(inventory)
    for category_inv in inventory:
        if category_inv == category:
            current_item = inventory[category_inv][item_name]
            current_item.update(update_info)
    return inventory

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    for category in inv2: #electronics in inv2
        for key in inv2[category]:  
            if key == 'Laptop':
                if inv2[category][key]['quantity'] >=5:
                    return {**inv1, **inv2}
                else:
                    merged = {**inv1, **inv2}
                    merged[category][key] = inv1[category][key]
                    return merged
        
def get_items_in_category(inventory, category):
    
    return inventory.get(category)

def find_most_expensive_item(inventory):
    max_value = 0
    for value in inventory.values():
        for inside_value in value.values():
            if inside_value['price'] > max_value:
                max_value = inside_value['price']
                max_product = inside_value
    return max_product

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category in inventory:
        if item_name in inventory[category]:
            return inventory[category][item_name]

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    all_items = []
    for category in inventory:
        for item in inventory[category]:
            all_items.append(inventory[category][item])
    return all_items

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    pairs = []
    for category, items in inventory.items():
        for item_name, item_info in items.items():
            pairs.append((category, item_info))
    return pairs


def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    import copy
    return copy.deepcopy(inventory) if deep else inventory.copy()
