# -*- coding: utf-8 -*-
import random
import sys
import math


def GetNewBoard():
    board=[]
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                board.append('~')
            else:
                board.append('`')
    return board


def DrawBoard(board):
    tensdigline='    '
    for i in range(1,6):
        tensdigline+=(' '*9)+str(i)

    print(tensdigline)
    print('   '+('0123456789'*6))
    print()

    for row in range(15):
        if row<10:
            extraspace=' '
        else:
            extraspace=''

        boardrow=''
        for column in range(60):
            boardrow+=board[column][row]

        print('%s%s %s %s'%(extraspace,row,boardrow,row))

    print()
    print('   '+('0123456789'*6))
    print(tensdigline)


def GetRandomChests(numchests):
    chests=[]
    while len(chests)<numchests:
        newchest=[random.randint(0,59),random.randint(0,14)]
        if newchest not in chests:
            chests.append(newchest)
    return chests


def IsOnBoard(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14


def MakeMove(board,chests,x,y):
    smalldist=100
    for cx,cy in chests:
        dist=math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))

        if dist<smalldist:
            smalldist=dist

    smalldist=round(smalldist)

    if smalldist==0:
        chests.remove([x,y])
        return 'Вы нашли затонувший сундук с сокровищами!'
    else:
        if smalldist<10:
            board[x][y]='X'
            return 'Сундуки не в зоне достигаемости.'


def EnterPlayerMove(previousmoves):
    print('Куда вы хотите уронить следующее эхолотное устройство? (0-59 0-14) (или введите quit)')
    while True:
        move=input()
        if move.lower()=='quit':
            print('Спасибо за игру!')
            sys.exit()

        move=move.split()
        if len(move)==2 and move[0].isdigit() and move[1].isdigit() and IsOnBoard(int(move[0]),int(move[1])):
            if [int(move[0]),int(move[1])] in previousmoves:
                print('Вы уже вводили эти координаты.')
                continue
            return[int(move[0]),int(move[1])]
        print('Введите число от 0 до 59, пробел, затем число от 0 до 14.')


def ShowInstructions():
    print(''' Инструкции:
109 Вы капитан Симона, корабля для поиска сокровищ. Ваша текущая миссия
110 использовать сонарные устройства, чтобы найти три сундука с сокровищами в нижней части
111 океан. Но у вас есть только дешевый сонар, который находит расстояние, а не направление.
112
113 Введите координаты, чтобы уронить гидролокатор. На карте океана будет помечено
114 как далеко находится ближайший сундук или X, если он находится за пределами гидролокатора
115 диапазона. Например, метки C - это место, где находятся сундуки. Гидролокатор показывает
116 3 потому что ближайший сундук находится в 3 местах.
117
118	                    1         2         3
119	          012345678901234567890123456789012
120
121	        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
122	        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
123	        2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
124	        3 ````````~~~`````~~~`~`````~`~``~` 3
125	        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
126
127	          012345678901234567890123456789012
128	                    1         2         3
129	(В настоящей игре сундуки не видны в океане.)
130
131	Press enter to continue...''')
input()

print('''Когда вы бросаете устройство эхолота прямо на сундук, вы получаете его, а другой
135      Обновление эхолотов показывает, как далеко находится ближайший сундук. Сундуки
136      находятся вне зоны действия сонарного устройства слева, поэтому на нем показан X.
137
138	                    1         2         3
139	          012345678901234567890123456789012
140
141	        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
142	        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
143	        2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
144	        3 ````````~~~`````~~~`~`````~`~``~` 3
145	        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
146
147	          012345678901234567890123456789012
148	                    1         2         3
149
150	Сундуки с сокровищами не двигаются. Устройства сонара могут обнаружить сундуки с сокровищами
151 до расстояния 9 пробелов. Попробуйте собрать все 3 сундука, прежде чем закончится
152 гидролокаторы. Удачи!
153
154	Press enter to continue...''')

input()

print('S O N A R !')
print()
print('Хотите просмотреть инструкции?? (yes/no)')
if input().lower().startswith('y'):
    ShowInstructions()


while True:
    sonardevices = 20
    theBoard = GetNewBoard()
    theChests = GetRandomChests(3)
    DrawBoard(theBoard)
    previousmoves = []

    while sonardevices > 0:
        print('у Вас осталось %s устройство (а). %s сундук с сокровищами остался.' % (sonardevices, len(theChests)))
        x,y=EnterPlayerMove(previousmoves)
        previousmoves.append([x,y])

        moveresult=MakeMove(theBoard,theChests,x,y)
        if moveresult==False:
            continue
        else:
            if moveresult=='Вы нашли затонувший сундук с сокровищами!':
                for x, y in previousmoves:
                    MakeMove(theBoard,theChests,x,y)
            DrawBoard(theBoard)
            print(moveresult)

        if len(theChests)==0:
            print('Вы нашли все затонувшие сундуки с сокровищами! Хорошая игра!')
            break

        sonardevices-=1

    if sonardevices==0:
        print('У нас закончились сонарные устройства! Теперь мы должны развернуть корабль и выйти')
        print('******************** Game over.************************')
        print('    Остальные сундуки были здесь:')
        for x, y in theChests:
            print('    %s, %s' % (x, y))

    print('Хочешь играть снова? (yes or no)')
    if not input().lower().startswith('y'):
        sys.exit()
