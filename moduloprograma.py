import modulomoeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de R${p} é R${modulomoeda.metade(p)} ')
print(f'O dobro de R${p} é R${modulomoeda.dobro(p)} ')
print(f'Aumentando 10 porcentos de  R${p} , temos R${modulomoeda.aumentar(p, 10)} ')
print(f'Diminuindo 10 porcentos de  R${p} , temos R${modulomoeda.diminuir(p, 10)} ')
