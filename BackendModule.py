class BackendModule:

    def __init__(self):
        self.first_choice_money = None
        self.first_choice = None
        self.second_choice = None

    def currency_choice_first(self):
        """Метод для определения ИЗ какой валюты необходимо произвести конвертацию.
        Доступно 4 варианта.
        1. Доллары
        2. Евро
        3. Гривны
        4. Рубли
        Так же записывается в self.first_choice_money - первая сумма конвертации"""
        while True:
            print("Выберите валюту из какой хотите конвертировать\n"
                  "1. Доллары\n"
                  "2. Евро\n"
                  "3. Гривны\n"
                  "4. Рубли\n")
            self.first_choice = input("Ввод: ")
            if self.first_choice not in ["1", "2", "3", "4"]:
                print("Нужно ввести в диапазоне 1 - 4. Выберите пожалуйста, в этом пределе.")
            else:
                print(f"Чудесно, вы выбрали -> {self.first_choice}, Введите теперь пожалуйста сумму")
                self.first_choice_money = input("Ввод: ")
                if not self.first_choice_money.isdigit():
                    print("Повторите попытку. Вы ввели не число")
                else:
                    if int(self.first_choice_money) > 0:
                        return self.first_choice, int(self.first_choice_money)
                    else:
                        print("Но как ведь мы можем конвертировать меньше нуля? ╮（╯＿╰）╭")

    def currency_choice_second(self):
        """Метод для определения В какую валюту необходимо произвести конвертацию.
                Доступно 4 варианта.
                1. Доллары
                2. Евро
                3. Гривны
                4. Рубли
                Так же записывается в self.second_choice - вторая сумма конвертации"""
        while True:
            print("Выберите в какую валюту хотите конвертировать\n"
                  "1. Доллары\n"
                  "2. Евро\n"
                  "3. Гривны\n"
                  "4. Рубли\n")
            self.second_choice = input("Ввод: ")
            if self.second_choice not in ["1", "2", "3", "4"]:
                print("Нужно ввести в диапазоне 1 - 4. Выберите пожалуйста, в этом пределе.")
            else:
                return self.second_choice

    def converter(self):
        """Метод Конвертирует валюты на основе заранее определенных курсов обмена.
        Примечание:
        1. Курсы фиксированы и могут изменяться в реальном времени. Рекомендуется обновлять курсы перед использованием.
        2. Метод конвертирует валюту на основе главных двух методов ↑↑↑"""
        dollar_in_euro = 0.91
        dollar_in_grivna = 41.27
        dollar_in_rub = 91.20
        euro_in_dollar = 1.10
        euro_in_grivna = 45.61
        euro_in_rub = 100.37
        grivna_in_dollar = 0.024
        grivna_in_euro = 0.022
        grivna_in_rub = 2.21
        rub_in_dollar = 0.011
        rub_in_euro = 0.01
        rub_in_grivna = 0.45

        if self.first_choice == "1" and self.second_choice == "2":  # С долларов в евро
            item = float(self.first_choice_money) * dollar_in_euro
            print(f"Сумма после обмена, будет составлять: {item} евро")
        elif self.first_choice == "1" and self.second_choice == "3":  # С долларов в гривны
            item = float(self.first_choice_money) * dollar_in_grivna
            print(f"Сумма после обмена, будет составлять: {item} гривен")
        elif self.first_choice == "1" and self.second_choice == "4":  # С долларов в рубли
            item = float(self.first_choice_money) * dollar_in_rub
            print(f"Сумма после обмена, будет составлять: {item} рублей")
        elif self.first_choice == "2" and self.second_choice == "1":  # С евро в доллары
            item = float(self.first_choice_money) * euro_in_dollar
            print(f"Сумма после обмена, будет составлять: {item} долларов")
        elif self.first_choice == "2" and self.second_choice == "3":  # С евро в гривны
            item = float(self.first_choice_money) * euro_in_grivna
            print(f"Сумма после обмена, будет составлять: {item} гривен")
        elif self.first_choice == "2" and self.second_choice == "4":  # С евро в рубли
            item = float(self.first_choice_money) * euro_in_rub
            print(f"Сумма после обмена, будет составлять: {item} рублей")
        elif self.first_choice == "3" and self.second_choice == "1":  # С гривен в доллары
            item = float(self.first_choice_money) * grivna_in_dollar
            print(f"Сумма после обмена, будет составлять: {item} долларов")
        elif self.first_choice == "3" and self.second_choice == "2":  # С гривен в евро
            item = float(self.first_choice_money) * grivna_in_euro
            print(f"Сумма после обмена, будет составлять: {item} евро")
        elif self.first_choice == "3" and self.second_choice == "4":  # С гривен в рубли
            item = float(self.first_choice_money) * grivna_in_rub
            print(f"Сумма после обмена, будет составлять: {item} рублей")
        elif self.first_choice == "4" and self.second_choice == "1":  # С рублей в доллары
            item = float(self.first_choice_money) * rub_in_dollar
            print(f"Сумма после обмена, будет составлять: {item} долларов")
        elif self.first_choice == "4" and self.second_choice == "2":  # С рублей в евро
            item = float(self.first_choice_money) * rub_in_euro
            print(f"Сумма после обмена, будет составлять: {item} евро")
        elif self.first_choice == "4" and self.second_choice == "3":  # С рублей в гривны
            item = float(self.first_choice_money) * rub_in_grivna
            print(f"Сумма после обмена, будет составлять: {item} гривен")
