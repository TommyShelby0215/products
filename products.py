products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':#quick
		break
	price = input('請輸入商品價格: ')
	p = []#快寫法= p = {name, price}
	p.append(name)
	p.append(price)
	products.append(p)
	#也可以products.append([name, price])

print(products)
print(products[0][0])

for product in products:
	print(product)
	print(p[0])#每一個小清單的第0格
	print(p[0], '的價格是', p[1])