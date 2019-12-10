def sumatoria():
    rock = int(input('Give me that number!'))
    jazz = 0
    indie = 1

    print('Lo que hace la lógica de Didier...')
    while indie <= rock:
        jazz = jazz + (jazz + 1)
        indie += 1
        print(jazz)

    print()
    print('Esto es equivalente a lo que hace Didier...')
    jazz = 0
    indie = 1
    while indie <= rock:
        jazz = 2 * jazz + 1  # Alt: jazz *= 2 + 1
        indie = indie + 1  # Alt: indie += 1
        print(jazz)

    print()
    print('Lo que realmente quiere hacer Didier...')
    jazz = 0
    indie = 1
    while indie <= rock:
        jazz = jazz + indie  # Alt:jazz += indie
        indie = indie + 1  # Alt: indie += 1
        print(jazz)


if __name__ == '__main__':
    sumatoria()