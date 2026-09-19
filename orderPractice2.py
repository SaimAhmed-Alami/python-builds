

"""The Likely Scenario: B2B Order Fulfillment SystemThe Setup:
A restaurant places a bulk order containing multiple inventory items. 
You are given the order details and the supplier's current stock levels.
The Task: Write a function process_order(order, supplier_stock) that determines if the order can be completely fulfilled.

If it can be fulfilled, update the supplier's stock and return the total cost of the order.

If it cannot be fulfilled (due to insufficient stock), 
return a message indicating which items are short and by how much.Expected Input Data Structures:"""

# The items the restaurant wants to buy and the quantities
order = [
    {"item_id": "item_1",
      "quantity": 10},
    {"item_id": "item_3", 
     "quantity": 5}
]

# The supplier's current inventory and prices
supplier_stock = {
    "item_1": {"quantity": 15, "price_per_unit": 2.50},
    "item_2": {"quantity": 50, "price_per_unit": 1.20},
    "item_3": {"quantity": 5, "price_per_unit": 10.00} # Note: short on stock (3 vs 5 requested)
}



def process_order(order: list,supplier_stock: dict) -> str:
    cost=0
    for item in order:
        item_id = item["item_id"]
        if (supplier_stock[item_id]["quantity"]>=item["quantity"]):
            cost+=(item["quantity"]*supplier_stock[item_id]["price_per_unit"])
            supplier_stock[item_id]["quantity"] -= item["quantity"]
        else:
            cost=0
            return "The item that does not have enough in stock is: "+str(item_id) + " and it is short by " + str(item["quantity"]-supplier_stock[item_id]["quantity"])+" items"
    return "The total cost of the order is: " + str(cost)

print (process_order(order, supplier_stock))



