price = int(input("what is the price of the product : "))
sale = int(input("how much with sale: "))

new_price = price * sale // 100
sale_price = price - new_price

print(sale_price)