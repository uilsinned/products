products = []
while True:
	product = input('請輸入商品品項: ')
	if product == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([product, price])
print(products)

for d in products:
	print(d[0],'價格為', d[1])
