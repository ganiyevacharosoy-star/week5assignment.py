def add_product(products, prices, new_product, new_price):
    products.append(new_product)
    prices.append(new_price)
    
def remove_product(products, prices, product_to_remove):
    if product_to_remove in products:
        value = products.index(product_to_remove)
        products.pop(value)
        prices.pop(value)
        return True
    else:
        return False    
        
        
    
def get_most_valuable(products, prices, count):
    current_products = products[:]
    current_prices = prices[:]
    result = []
    
    for i in range(count):
        if not current_prices:
            break
        max_value = 0
        for j in range(1, len(current_prices)):
            if current_prices[j] > current_prices[max_value]:
                max_value = j
        result.append(current_products[max_value])
        current_products.pop(max_value)
        current_prices.pop(max_value)
    return result        
    
def manage_inventory(initial_products, initial_prices, new_product_data, product_to_remove, top_count):
    last_items_list = initial_products[:]
    last_prices = initial_prices[:]
    add_product(last_items_list, last_prices, new_product_data[0], new_product_data[1])
    remove_product(last_items_list, last_prices, product_to_remove)
    top_items_names= get_most_valuable(last_items_list, last_prices, top_count)
    
    return last_items_list, top_items_names
    
    
    
products = ["Watch", "Ring", "Bag", "Scarf", "Pen"]
prices = [5500.00, 7200.00, 3100.00, 800.00, 1200.00]
new_product = ["Statue", 6800.00]
remove_name = "Scarf"
count = 3

# When you call your function:
final_products, top_list = manage_inventory(products, prices, new_product, remove_name, count)
print(f"Final products: {final_products}")
print(f"Top list: {top_list}")    
    
         
