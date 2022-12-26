move = int(input('Выберите день недели: 1 - понедельник, 2 - среда, 3 - пятница: '))

if move == 1:
    with open('ponedelnik.txt', 'r', encoding ='utf-8') as f:
        print(f.read())
        changes = str(input('Какие изменения вы хотите внести?: '))
        with open('ponedelnik.txt', 'a', encoding='utf-8') as f:
            f.write(changes)

if move == 2:
    with open('sreda.txt', 'r', encoding ='utf-8') as f:
        print(f.read())
        changes = str(input('Какие изменения вы хотите внести?: '))
        with open('sreda.txt', 'a', encoding='utf-8') as f:
            f.write(changes)

if move == 3:
    with open('piatnizza.txt', 'r', encoding ='utf-8') as f:
        print(f.read())
        changes = str(input('Какие изменения вы хотите внести?: '))
        with open('piatnizza.txt', 'a', encoding='utf-8') as f:
            f.write(changes)