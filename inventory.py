"""Inventory management module."""

import json
from datetime import datetime

# Global inventory dictionary
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the stock with the given quantity."""
    if logs is None:
        logs = []
    if not item or not isinstance(qty, (int, float)):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a given quantity of an item from the stock."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in stock.")
    except TypeError:
        print(f"Invalid quantity type for item '{item}'.")


def get_qty(item):
    """Get the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty data.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with empty data.")


def save_data(file_path="inventory.json"):
    """Save stock data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data():
    """Print all inventory items and their quantities."""
    print("\nItems Report:")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """Return a list of items below the given stock threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Demonstration of inventory management operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
