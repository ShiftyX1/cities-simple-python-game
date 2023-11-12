from game import GameCities, Checks
from cities_check import cities_list_all

check = Checks()

game = GameCities()

def game_with_bot(game=game, check=check):
    while True:
        computer = 0
        user_answer = str(input("Введите название города: ")).casefold()
        if check.match(user_answer) == True:
            print("Ввод доступен только кириллицой!")
            continue
        elif check.check_cities(user_answer=user_answer) == 1:
            print(f"Такого города нет в нашей базе данных :(\nПопробуйте написать название города в другом формате.\nИли сообщите об ошибке.")
            continue
        #if user_answer in cities_list_all:
        try:
            game.computer_plays(user_answer=user_answer)
            if game.player_win == 1:
                break
        except KeyError:
            print(f"Ух ты, кажется я не знаю города, названия которых начинаются с буквы {user_answer[-1].capitalize()} :(\nПохоже Вы победили!")
            break

        computer = game.computer_answer

        if computer != 0:
            i = True
            while i == True:
                user_answer = str(input("Компьютер ответил, ваш ответ: ")).casefold()
                if check.match(user_answer) == True:
                    print("Ввод доступен только кириллицой!")
                    continue
                elif check.check_cities(user_answer=user_answer) == 1:
                    print(f"Такого города нет в нашей базе данных :(\nПопробуйте написать название города в другом формате.\nИли сообщите об ошибке.")
                    continue
                game.player_plays(user_answer=user_answer)
                if game.fails == 3:
                    print("Вы проиграли!")
                    break
                elif game.player_win == 1:
                    break
        break

    
        #else:
            #print("Такого города нет в базе данных, попробуйте написать название с большой буквы или на русском языке и повторить попытку :(")

def hot_seat_play(game=game, check=check):
    print("COMING SOON... or not :)))")

while True:
    print("""Добро пожаловать в игру в города!
            Выберите режим игры: 
            1)Играть против компьютером
            2)Играть один на один с человеком (Hot-Seat) (Work In Progress)""")

    user_choice = int(input("Введите цифру соответствующую вашему выбору: "))

    if user_choice == 1:
        game_with_bot()
        break
    elif user_choice == 2:
        hot_seat_play()
        continue
    else:
        print("Недопустимый выбор, введите 1 или 2")
        continue
    