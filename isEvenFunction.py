'''1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен
нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. '''

'''Python example: '''

def isEven(value):
    return value % 2 == 0

def isEvenNew(value):
    zero = 0
    return int(value % 2) is zero

"""В примерах аналогичная функциональность нахождения результата (value % 2), далее происходит сравнение. Разница сути 
сравнения в операторах == и is. 
Оператор == сравнивает фактические значения, is сравнивает идентичность объектов (т.е. объекты ссылаются на одну ячейку 
памяти). В случае с нулем данная функция будет работать корректно. Т.к. два нулевых значения будут ссылаться на одну ячейку.
При вычислении четности числа с плавающей точкой, результат будет 0.0 (float), в этом случае функция отработает некорректо,
т.к. 0 и 0.0 не идентичны но равны (оператор == отработает корректно), для этого случая используется приведение 
результата вычисления к типу int. Так же заведена дополнительная переменная zero для хранения объекта сравнения, чтобы
избежать SyntaxWarning сравнения с литералом.
Использование is в таких случаях нежелательно.
"""