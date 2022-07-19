import unittest
import isEvenFunction
import circleQueueList
import mergeSortFunction


array = [1, 3, 5, 18, 32, 4, 5 , 1, 0, -15, 2.6, -0.25]
sorted_array = [-15, -0.25, 0, 1, 1, 2.6, 3, 4, 5, 5, 18, 32]

class TestFile(unittest.TestCase):
    def test_isEven(self):
        self.assertEqual(isEvenFunction.isEven(2), True)
        self.assertEqual(isEvenFunction.isEven(2222), True)
        self.assertEqual(isEvenFunction.isEven(-4), True)
        self.assertEqual(isEvenFunction.isEven(3), False)
        self.assertEqual(isEvenFunction.isEven(-3), False)

    def test_isEven_new(self):
        self.assertEqual(isEvenFunction.isEven(2), True)
        self.assertEqual(isEvenFunction.isEven(2222), True)
        self.assertEqual(isEvenFunction.isEven(-4), True)
        self.assertEqual(isEvenFunction.isEven(3), False)
        self.assertEqual(isEvenFunction.isEven(-3), False)

    def test_circle_q(self):
        self.assertEqual(circleQueueList.a.enqueue(5), "5 in queue")
        self.assertEqual(circleQueueList.a.enqueue(7), "7 in queue")
        self.assertEqual(circleQueueList.a.enqueue(9), "9 in queue")
        self.assertEqual(circleQueueList.a.enqueue(10), "10 is not was apended. Queue is full!")
        self.assertEqual(circleQueueList.a.dequeue(), 5)
        self.assertEqual(circleQueueList.a.next_item(), 7)
        self.assertEqual(circleQueueList.a.last_item(), 9)
        self.assertEqual(circleQueueList.a.return_queue(), [7, 9])

    def test_sorting_function(self):
        self.assertEqual(mergeSortFunction.merge_sort(array), sorted_array)

if __name__ == "__main__":
    unittest.main()