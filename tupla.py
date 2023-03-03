cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
while True:
    num = int(input('Digite um número de 0 a 5 : '))
    if 0 <= num <= 5:
        break
    print('Tente novamente : ', end='')
print(f'O número que você digitou é o {cont[num]}')
