# Step 1: Define the function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Step 4: Print the final price after applying the discount or the original price
if final_price == price:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
else:
    print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
# Step 5: Print the data types of the inputs and the result
print(f"\nData type of original price: {type(price)}")  
