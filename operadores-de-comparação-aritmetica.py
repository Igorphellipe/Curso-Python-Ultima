print('\033[32m-=-\033[m' * 10)
print('\033[1;4mOPERADORES DE COMPARAÇÃO ARITMÉTICA\033[m')
print('\033[32m-=-\033[m' * 10)

#Ultilizando operador Maior igual >=
idade = 15
resultado = idade >= 18
print(resultado)

#Operadores de comparação aritmética (Fazem parte da logica boleana)
print('-=-' * 10)

prod_vendidos = 100
prod_estoque = 90

print(f'Produtos vendidos: {prod_vendidos}')
print(f'Produtos estoque: {prod_estoque}')
print('-=-' * 10)

print(f'Operador \033[1mIgual a (==)\033[m: Produtos vendidos == Produtos estoque:  {prod_vendidos == prod_estoque}')
print(f'Operador \033[1mDiferente de (!=)\033[m: Produtos vendidos != Produtos estoque: {prod_vendidos != prod_estoque}')
print(f'Operador \033[1mMenor que (<)\033[m: Produtos vendidos < produtos estoque: {prod_vendidos < prod_estoque}')
print(f'Operador \033[1mMenor ou igual a (<=)\033[m: Produtos vendidos <= Produtos estoque: {prod_vendidos <= prod_estoque}')
print(f'Operador \033[1mMaior que (>)\033[m: Produtos vendidos > produtos estoque: {prod_vendidos > prod_estoque}')
print(f'Operador \033[1mMaior ou igual a (>=)\033[m: Produtos vendidos >= Produtos estoque: {prod_vendidos >= prod_estoque}')