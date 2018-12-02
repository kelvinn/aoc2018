import unittest
import days.day_2


class TestDay2(unittest.TestCase):

    def setUp(self):
        with open('data/day_2.txt', newline='') as f:
            self.data = f.read()

    def test_task_1(self):

        result_task_1 = days.day_2.solve_task_1(self.data)
        self.assertEqual(result_task_1, 6888)

    def test_task_2(self):

        result_task_2 = days.day_2.solve_task_2(self.data)
        self.assertEqual(result_task_2, 'icxjvbrobtunlelzpdmfksahgs')


if __name__ == '__main__':
    unittest.main()
