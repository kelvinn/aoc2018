import unittest
import days.day_3


class TestDay3(unittest.TestCase):

    def setUp(self):
        with open('tests/data/day_3.txt', newline='') as f:
            self.data = f.read()

    def test_task_1(self):

        result_task_1 = days.day_3.solve_task_1(self.data)
        self.assertEqual(result_task_1, 101781)

    def test_task_2(self):

        result_task_2 = days.day_3.solve_task_2(self.data)
        self.assertEqual(result_task_2, '#909')


if __name__ == '__main__':
    unittest.main()
