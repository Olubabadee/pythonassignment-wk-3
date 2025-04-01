# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.


def calculate_discount(price, discount_percentage):

    if discount_percentage >= 20:
        finalPrice = price - ((discount_percentage/100) * price)
        return finalPrice

    else:
        return price

price = float(input("Enter Original Price of Item - "))
discount_percentage = float(input("Enter Percentage - "))

fina_Price = calculate_discount(price, discount_percentage)

print(f"Final Price ${fina_Price}")