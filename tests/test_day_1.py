import unittest
import days.day_1


class TestDay1(unittest.TestCase):

    def setUp(self):
        with open('data/day_1.txt', newline='') as f:
            self.data = f.read()

    def test_task_1(self):

        result_task_1 = days.day_1.solve_task_1(self.data)
        self.assertEqual(result_task_1, 497)

    def test_task_2(self):

        result_task_2 = days.day_1.solve_task_2(self.data)
        self.assertEqual(result_task_2, 558)


if __name__ == '__main__':
    unittest.main()
