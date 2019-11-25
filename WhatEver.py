def music():
    rock = int(input('Give it to me baby '))




# ##numero in range(1,5)
# True
# for numero in range(1,5):
#     print(numero)
#
# 1
# 2
# 3
# 4
# x = 5
# y = 1
# while y <= x:
#     print(y)
#     y = y + 1
#
# 1
# 2
# 3
# 4
# 5##


def licor():
    from math import sqrt
    ron = int(input('Give a number: '))
    if 1 <= ron <= 10:
        if ron%2 == 0:
            print('Pair: '+str(ron ** 2))
        else:
            print('Unpair '+str(sqrt(ron)))
    else:
        print('Yoy know nothing Jon Snow')


def cigarretsmentol():
    camels = int(input('Give a number: '))
    marlboro = False
    if (1 <= camels <= 10):
        if (camels%2 != 0):
            marlboro = True
    if marlboro:
        print('Yes its sir ' + str(camels))
    else:
        print('No is not sir %i' %camels)

def cigarrets():
    camels = int(input('Give a number: '))
    if (1 <= camels <= 10) and (camels%2 != 0):
        print('Yes its sir '+str(camels))
    else:
        print('No is not sir %i' %camels)

def color():
    blue = int(input('Number: '))
    if 5 <= blue <= 10:
        print('Yes '+str(blue))
    else:
        print('No '+str(blue))

def beer():
    pilsner = int(input('Number '))
    if pilsner%2 == 0:
        print('Par')
    else:
        print('Impar')

def canabis():
    indica = float(input('First number: '))
    satiba = float(input('Second number: '))

    print(indica + satiba)
    print((indica + satiba)*10)

def felinos():
    gato = 5
    gata = 7

    gatos = gato + gata

    print(gatos)

    gatos = gatos * 10

    print(gatos)

if __name__ == '__main__':
    licor()


