import os
from posixpath import split
import sys


the_board = [i for i in range(1, 10)]
user_x = True
wins = {'x':0, '0':0}

wins_draw = []                                  # получаем значения побед из файла
with open('statistic.txt') as f:
    for line in f:
        wins_draw.append([int(x) for x in line.split()])
wins['x'] = wins_draw[0][0]
wins['0'] = wins_draw[1][0]
draw = wins_draw[2][0]


def show_menu():                        # функция вывода в терминал меню игры
    os.system('clear')
    print('_____MENU_____', end = '\n\n')
    print('1. Show statistic')
    print('2. Play tik tak', end = '\n\n')

    answer = input('What do you want to choose? ')
    while (answer != '1') and (answer != '2'):
        print('Please pick the right option')
        answer = input('What do you want to choose? ')
    return answer

def show_the_board():                   # функция вывода в терминал поле игры
    os.system('clear')
    print(f'{the_board[0]} | {the_board[1]} | {the_board[2]}')
    print('__|___|__')
    print(f'{the_board[3]} | {the_board[4]} | {the_board[5]}')
    print('__|___|__')
    print(f'{the_board[6]} | {the_board[7]} | {the_board[8]}')


def show_statistic():                   # функция вывода статистики
    print('Showing statistic')
    print('Побед "x" - ' + str(wins['x']))
    print('Побед "0" - ' + str(wins['0']))
    print('Ничьих - ' + str(draw))

def write_stat():                       # функция записи новых результатов в файл
    stat = open('statistic.txt', 'w')
    stat.write(str(wins['x']) + '\n')
    stat.write(str(wins['0'])+ '\n')
    stat.write(str(draw))
    stat.close

def get_user_turn():                    # функция получения номера клетки, куда будет ходить игрок
    while True:
        if user_x == True:
            turn = input('User_x pick (1-9): ')
        else:
            turn = input('User_0 pick (1-9): ')
        try:
            if int(turn) in range(1, 10):
                return int(turn)
            else:
                print('Enter correct value')
        except:
            print('Enter correct value')
 
def seeking_win(a):                      # поиск победных комбинаций
    for i in range(0, 9, 3):
        if the_board[i] == a and the_board[i + 1] == a and the_board[i + 2] == a:       # проверяем горизонтальный ряды
            print(f'User_{a} won')
            wins[a] += 1 
            write_stat()
            sys.exit(0)
    for i in range(0, 3, 1):
        if the_board[i] == a and the_board[i + 3] == a and the_board[i + 6] == a:       # проверяем вертикальные ряды
            print(f'User_{a} won')
            wins[a] += 1
            write_stat()
            sys.exit(0)
    if the_board[0] == a and the_board[4] == a and the_board[8] == a:       # проверяем диагонали ряды
            print(f'User_{a} won')
            wins[a] += 1
            write_stat()
            sys.exit(0)
    if the_board[2] == a and the_board[4] == a and the_board[6] == a:       # проверяем диагонали ряды
            print(f'User_{a} won')
            wins[a] += 1
            write_stat()
            sys.exit(0)
    

def play_game():                         # логика игры
    print("Playing the game")
    show_the_board()
    counter = 1
    global draw
    global user_x
    global the_board
    while True:
        if counter <= 9:
            turn = get_user_turn()
            if user_x == True:                                                   # ходит игрок 'x', с проверкой свободна ли клетка
                if the_board[turn-1] != 'x' and the_board[turn-1] != '0':       
                    the_board[turn-1] = 'x'
                    show_the_board()
                else:                                                             # если клетка уже занята
                    print('Select another field') 
                    turn = get_user_turn()
                    if the_board[turn-1] != 'x' and the_board[turn-1] != '0':       
                        the_board[turn-1] = 'x'
                        show_the_board()
            seeking_win('x')

            if user_x == False:                                                    # ходит игрок '0', с проверкой свободна ли клетка
                if the_board[turn-1] != '0' and the_board[turn-1] != 'x':    
                    the_board[turn-1] = '0'
                    show_the_board()
                else:                                                              # если клетка уже занята
                    print('Select another field') 
                    turn = get_user_turn()
                    if the_board[turn-1] != '0' and the_board[turn-1] != 'x':    
                        the_board[turn-1] = '0'
                        show_the_board()   
            seeking_win('0') 
            counter += 1
            user_x = not user_x
        else:                                                                      # если все клетки заполнены и в игре ничья
            print('No one has won')
            draw += 1
            write_stat()
            break


def main():
    answer = show_menu()
    if answer == '1':
        show_statistic()
    else:
        play_game()

main()
if __name__ == '_main_':
    main()