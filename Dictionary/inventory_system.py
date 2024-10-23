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
            {"name": "Laptop", "price": 1000, "quantity": 10},
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
    inventory = create_inventory()
    # print(inventory)
    for key in inventory:
        if key == category:
            (inventory[key][item_name]).update(update_info)
    return inventory

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    return {**inv1, **inv2}
def get_items_in_category(inventory, category):
    
    return inventory.get(category)

def find_most_expensive_item(inventory):
    max_value_product = None
    max_value = 0

    for value in inventory.values():
        for inside_value in value.values():
            if inside_value['price'] > max_value:
                max_value = inside_value['price']
                max_value_product = inside_value['name']
    return max_value_product

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    pass

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    for value in inventory.values():
        for inside_value in value.values():
            return inside_value

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    pass

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    return inventory.deepcopy() if deep else inventory.copy()
