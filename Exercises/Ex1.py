# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def mult_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    
# first condition
result = mult_or_sum(20, 30)
print("The result is", result)

# Second condition
result = mult_or_sum(40, 30)
print("The result is", result)