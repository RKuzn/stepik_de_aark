def calculator():
    """Простой калькулятор с выбором операции"""
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /, **, //, %")

    #error mesages
    error_div_zero = "Ошибка: деление на 0"
    while True:
        try:
            num1 = float(input("Первое число: "))
            op = input("Операция (или 'q' для выхода): ")
            if op.lower() == 'q':
                print("Выход из калькулятора")
                break
            num2 = float(input("Второе число: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '**':
                result = num1 ** num2
            elif op == '/':
                if num2 == 0:
                    print(error_div_zero)
                    continue
                result = num1 / num2
            elif op == '//':
                if num2 == 0:
                    print("Ошибка: деление на ноль")
                    continue
                result = num1 // num2
            elif op == '%':
                if num2 == 0:
                    print(error_div_zero)
                    continue
                result = num1 % num2
            else:
                print("Неизвестная операция")
                continue

            print(f"Результат: {num1} {op} {num2} = {result}\n")

        except ValueError:
            print("Ошибка: введите корректное число\n")

#вызов калькулятора
calculator()