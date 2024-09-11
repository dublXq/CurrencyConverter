import BackendModule

if __name__ == '__main__':

    BM = BackendModule.BackendModule()

    print("Здравствуйте ^_^\nВас приветствует конвертор валют.\nЗдесь вы можете конвертировать валюту, разных стран, в какую вам надо\n"
          "Создатель -> https://github.com/dublXq")

    while True:
        val = input("Пожалуйста, выберите действие:\n1.Конвертировать\n2.Выход\nВвод: ")

        if val == '1':
            BM.currency_choice_first()
            BM.currency_choice_second()
            BM.converter()
        elif val == '2':
            break
        else:
            print("Неправильный ввод. Пожалуйста, повторите.")
