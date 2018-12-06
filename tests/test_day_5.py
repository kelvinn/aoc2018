import unittest
import days.day_5


class TestDay5(unittest.TestCase):

    def setUp(self):
        with open('tests/data/day_5.txt', newline='') as f:
            self.data = f.read()

    def test_task_1(self):

        result_task_1 = days.day_5.solve_task_1(self.data)
        self.assertEqual(10978, result_task_1)  # 10978

    def test_task_2(self):

        result_task_2 = days.day_5.solve_task_2(self.data)
        self.assertEqual(result_task_2, 4840)


if __name__ == '__main__':
    unittest.main()
