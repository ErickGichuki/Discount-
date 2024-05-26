def calculate_discount(price, discount_percent ):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent/ 100) 
        return final_price
    else:
        return price
    
original_price = int(input('Enter the original price: '))
discount = int(input('Enter the discount percentage: '))

finalprice = calculate_discount(original_price, discount)
if discount >= 20:
    print(f'Hi prospective customer! the final price after applying the discount is: Kshs {finalprice}')

else:
    print(f'No discount applied. The price is: Kshs{original_price}')