"""Связный список не хранит массив с объектами внутри класса. Очередность достигается с помощью атрибутов объекта класса,
которые хранят ссылку на следующий объект. Очередь может быть бесконечной и ограничена только размером памяти. 
При печати элементов очереди, выводится список в соответсвии с порядком ее выполнения. По умолчанию, класс реализует FIFO. 
Но есть возможность явно указать объект как начало очереди (self.head). Таким образом буфер можно "вращать".
Для сохранения порядка очереди требуется явно указывать следующий элемент в очереди, при добавлении нового, для
сохранения цикличности.
 """   

class Node:
    """The creation of the Node object"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CircularLinkedList:
    """The creation linked list from Node class objects"""

    def __init__(self):
        self.head = None


    def traverse(self, starting_point=None):
        """The traverse all linked list"""

        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        """Print all objects in order. If list is empty print None"""

        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))


    def get_last_node(self):
        """Find and return last node in order"""

        last_node = None
        for node in self.traverse():
            last_node = node
        return last_node


    def return_first_node(self):
        """Return first node and remove it from queue"""

        if self.head is None:
            raise Exception("list is empty.")

        if self.head == self.get_last_node():  # if only one item in queue
            item_to_return = self.head
            self.head = None  # now queue is epmty
            return item_to_return

        self.get_last_node().next = self.head.next
        item_to_return = self.head
        self.head = self.head.next
        return item_to_return
 

circular_llist = CircularLinkedList()

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = a
circular_llist.head = a
circular_llist.return_first_node()
circular_llist.head = c
circular_llist.print_list()
circular_llist.return_first_node()
circular_llist.print_list()
