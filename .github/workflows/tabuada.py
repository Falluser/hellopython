num = int(input('digite um número para ver sua tabuada:'))
for c in range(0,11):
    print('{} x {:2} = {}'.format(num, c, num*c)) # c está vininculado ao contador de 0 á 11, mas contara só
# até 10, multiplicando sem ter que colocar vários prints!
    #obs: {:2} é espaço para duas casas !!
# abaixo é apenas uma versão  mais demorada
'''
num = int(input('digite um número para ver sua tabuada:'))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
'''
# com laços posso reduzir em 3 linhas de código!
