lista = ('julio', 'dyovana', 'pikachu', 'naruto', 'goku', 'ikki')
for palavra in lista:
    print(f'\nNa palavra {palavra}  temos ', end='')
    for letra in palavra:
        if letra.lower() in 'a e i o u ':
            print(letra, end='')
