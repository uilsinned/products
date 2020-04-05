import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8' ) as f:
        for line in f:
            if '商品名稱,商品價格' in line:
                continue #繼續
            [name, price] = line.strip().split(',')
            products.append([name, price])
    return products
    
#讓使用者輸入
def input_product(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products
#印出所有商品和價格
def print_products(products):
    for d in products:
        print(d[0],'的價格為', d[1], '元')
#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品名稱,商品價格\n')
        for d in products:
            f.write(d[0] + ',' + str(d[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('找到檔案了哦')
        products = read_file(filename)
        print(products)
    else:
        print('無法找到檔案')
    products = input_product(products)
    print_products(products)
    write_file('products.csv', products)


main()
