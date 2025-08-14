def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for the price and discount percent
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percent: "))

# Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Check if discount was applied and print appropriate message
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price:}")
else:
    print(f"No discount applied. The original price remains: {final_price:}")
    
