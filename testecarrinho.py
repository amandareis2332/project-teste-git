cart = []
#for i in range(3)
id_user = input("insira o id do usuario")
id_product = input("insira o id do produto")
price_product = float(input("insira o valor do produto"))
quantity_product = int(input("qual a quantidade"))

item = [id_user, id_product, price_product, quantity_product]

def add_item_carrinho():
    cart.append(item)
    return cart


add_item_carrinho()
