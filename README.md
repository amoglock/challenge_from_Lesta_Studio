# challenge_from_Lesta_Studio
Задание:

1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

        Python example:

        def isEven(value):return value%2==0
                
         
        def isEvenNew(value):
        zero = 0
        return int(value % 2) is zero
  
[Файл кода](https://github.com/amoglock/challenge_from_Lesta_Studio/edit/main/isEvenFunction.py)  
                
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
Буфер реализован в виде [связанного списка](https://github.com/amoglock/challenge_from_Lesta_Studio/blob/main/circleQueueLinkedArray.py) и [простого списка](https://github.com/amoglock/challenge_from_Lesta_Studio/blob/main/circleQueueList.py).

В случае простого списка реализуется массив фиксированного размера, в котором хранятся данные очереди. При печати списка элементов, выводится содержимое массива без указания следующего элемента в очереди. Для получения значения этого элемента, применяется отдельный метод. При заполнении очереди, дальнейшее увеличение размера списка невозможно.

Связный список не хранит массив с объектами внутри класса. Очередность достигается с помощью атрибутов объекта класса, которые хранят ссылку на следующий объект. Очередь может быть бесконечной и ограничена только размером памяти. При печати элементов очереди, выводится список в соответсвии с порядком ее выполнения. По умолчанию, класс реализует FIFO. Но есть возможность явно указать объект как начало очереди (self.head). Таким образом буфер можно "вращать".
Для сохранения порядка очереди требуется явно указывать следующий элемент в очереди, при добавлении нового, для сохранения цикличности.



3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.

Т.к. массив может быть любого размера, так же примем, что тип числовых значений в массиве может разным (int, float).
В качестве реализиции используем [сортировку слиянием (merge sort)](https://github.com/amoglock/challenge_from_Lesta_Studio/blob/main/mergeSortFunction.py). Данный тип сортировки стабильно отработает с любыми
типами числовых значений, а так же в любых случаях (вне зависимости от размера массива) временная сложность выполнения 
алгоритма составит O(n log n). Более быстрые сортировки по лучшему времени, могуть выполняться за n**2 в худшем случае.
