import random
import json

class GameCities():
    def __init__(self):
        with open('cities.json', 'r', encoding='utf-8') as fh:
            self.cities_data = json.load(fh)
        self.computer_answer = 0
        self.list_of_used_cities = []
        self.fails = 0
        self.player_win = 0
        self.check_city_error = 0

    def computer_plays(self, user_answer):
        while True:
            letter_key_list = self.cities_data[user_answer[-1]]
        
            try:
                self.computer_answer = letter_key_list[random.randint(0, len(letter_key_list) - 1)]
            except ValueError:
                print(f"Похоже я не знаю больше городов на букву {user_answer[-1].capitalize()} :(\nПохоже Вы победили!")
                self.player_win = 1
                break

            letter_key_list.remove(self.computer_answer)
            self.list_of_used_cities.append(self.computer_answer.casefold())
            self.list_of_used_cities.append(user_answer)
            print(f"Ответ компьютера: {self.computer_answer}")
            return self.computer_answer
            break
    
    def player_plays(self, user_answer):
        while True:
            if user_answer[0] == self.computer_answer[-1]:
                try:
                    i = user_answer[-1]
                    letter_key_list = self.cities_data[i]
                except KeyError:
                    i = user_answer[-2]
                    letter_key_list = self.cities_data[i]
                try:    
                    self.computer_answer = letter_key_list[random.randint(0, len(letter_key_list) - 1)]
                except ValueError:
                    print(f"Похоже я не знаю больше городов на букву {i.capitalize()} :(\nПохоже Вы победили!")
                    self.player_win = 1
                    break

                letter_key_list.remove(self.computer_answer)
                self.list_of_used_cities.append(self.computer_answer.casefold())
                self.list_of_used_cities.append(user_answer)
                print(f"Ответ компьютера: {self.computer_answer}")
            else:
                self.fails += 1
                print(f"Неправильно! {self.fails}-я ошибка из 3 возможных!")
            break


class Checks(GameCities):
    def __init__(self):
        self.is_ru_alphabet = True

    def match(self, text, alphabet=set('abcdefghijklmnopqrstuvwxyz1234567890')):
        return not alphabet.isdisjoint(text.lower())

    def check_cities(self, user_answer):

        with open('cities.json', 'r', encoding='utf-8') as it:
            data = json.load(it)

        list = data[user_answer[0]]

        if user_answer.capitalize() in list:
            self.check_city_error = 0
        else:
            self.check_city_error = 1

        return self.check_city_error