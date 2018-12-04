import unittest
import days.day_4


class TestDay4(unittest.TestCase):

    def setUp(self):
        with open('tests/data/day_4.txt', newline='') as f:
            self.data = f.read()

    def test_task_1(self):

        result_task_1 = days.day_4.solve_task_1(self.data)
        self.assertEqual(result_task_1, 143415)

    def test_task_2(self):

        result_task_2 = days.day_4.solve_task_2(self.data)
        self.assertEqual(result_task_2, 49944)


if __name__ == '__main__':
    unittest.main()
