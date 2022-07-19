# challenge_from_Lesta_Studio
Задание:

1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

                Python example:

                def isEven(value):return value%2==0
    '''            
    def isEvenNew(value):
    zero = 0
    return int(value % 2) is zero
    '''
                
В примерах аналогичная функциональность нахождения результата (value % 2), далее происходит сравнение. Разница сути 
сравнения в операторах == и is. 
Оператор == сравнивает фактические значения, is сравнивает идентичность объектов (т.е. объекты ссылаются на одну ячейку 
памяти). В случае с нулем данная функция будет работать корректно. Т.к. два нулевых значения будут ссылаться на одну ячейку.
При вычислении четности числа с плавающей точкой, результат будет 0.0 (float), в этом случае функция отработает некорректо,
т.к. 0 и 0.0 не идентичны но равны (оператор == отработает корректно), для этого случая используется приведение 
результата вычисления к типу int. Так же заведена дополнительная переменная zero для хранения объекта сравнения, чтобы
избежать SyntaxWarning сравнения с литералом.
Использование is в таких случаях нежелательно.               

2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
https://github.com/amoglock/challenge_from_Lesta_Studio/blob/main/circleQueueLinkedArray.py

3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.
