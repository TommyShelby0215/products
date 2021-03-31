products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':#quick
		break
	price = input('請輸入商品價格: ')
	price = int(price)
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

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')#因為前面將price轉化成整數而字串是不能跟整數+在一起，因此前面加個str()把整數轉化成字串
		#\n是換行的意思
		#csv檔可用excel開啟