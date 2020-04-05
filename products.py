import os #operating system

products = []

#讀取檔案
if os.path.isfile('products.csv'):#檢查有無檔案
	print('找到檔案了哦')
	with open('products.csv', 'r', encoding='utf-8' ) as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue #繼續
			[name, price] = line.strip().split(',')
			products.append([name, price])
	print(products)
else:		
	print('無法找到檔案')
	
#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)
#印出所有商品和價格
for d in products:
	print(d[0],'的價格為', d[1], '元')
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品名稱,商品價格\n')
	for d in products:
		f.write(d[0] + ',' + str(d[1]) + '\n')