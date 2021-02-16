class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите число: '))
                    ex = input(f'Добавляем "{user_val}" в список.\nДля выхода введите stop: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'stop':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Вы ввели не число! Для выхода введите stop: ").lower()
                if ex == 'stop':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()