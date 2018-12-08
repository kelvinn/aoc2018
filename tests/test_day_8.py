import unittest
import days.day_8


class TestDay8(unittest.TestCase):

    def setUp(self):
        with open('tests/data/day_8.txt', newline='') as f:
            self.data = f.read()

    def test_task_1(self):

        result_task_1 = days.day_8.solve_task_1(self.data)
        self.assertEqual(41849, result_task_1)

    def test_task_2(self):

        result_task_2 = days.day_8.solve_task_2(self.data)
        self.assertEqual(42, result_task_2)


if __name__ == '__main__':
    unittest.main()
