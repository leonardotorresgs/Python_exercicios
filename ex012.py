preco = float(input('Qual é o preço do produto? R$'))

preco_novo = preco-(preco*0.05)

print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${preco_novo:.2f}')
