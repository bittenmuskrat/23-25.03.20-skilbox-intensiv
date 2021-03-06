# Игра "Угадай число" была представлена лектором как пример кода на языке Python. 
# Используется бинарный поиск


# Настройки
a = 1
b = 1000
print(f'Загадай число от {a} до {b}...')

# Определим свою функцию, которая напечатает правила
def print_rules():
  rules = '''Если я угадаю, напиши "=",
    если твое число меньше, то введи "меньше",
    а если больше, то "больше".
    И нажми на Enter.'''
  print()  # Пустая строка
  print(rules)
  print()

# Даем время на подумать
import time
time.sleep(1)
print('Загадал?')
time.sleep(1)
print('Тогда поехали!')
print()
time.sleep(1)
print_rules()
time.sleep(1)

# Отгадываем
steps = 0

while True:
    if a > b:
        print('Произошел конфуз...')
        print('Попробуй заново')
        break
    if a == b:
        print(f'Все понятно. Ответ - {a}')
        print(f'Потребовалось шагов: {steps}')
        break

    steps += 1

    number = (a + b) // 2
    answer = input(f'Это {number}? ')

    if answer == '=':
        print('Ура! Я отгадал!')
        print(f'Потребовалось шагов: {steps}')
        break
    elif answer == 'меньше':
        b = number - 1
    elif answer == 'больше':
        a = number + 1
    else:
        print('Не понял. На всякий случай напомню правила:')
        print_rules()
        steps -= 1
