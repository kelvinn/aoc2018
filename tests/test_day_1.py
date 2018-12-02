import unittest
from days.day_1 import FrequencyTracker

DAY1_SAMPLE_DATA = """
+1
-2
+3
+1
"""

DAY1_SAMPLE_DATA_TASK_2 = """
+7
+7
-2
-7
-4
"""


class TestDay1(unittest.TestCase):

    def setUp(self):
        self.d = FrequencyTracker()

    def test_reader(self):
        file_name = 'tests/data/day1_sample_data_1.txt'
        result = self.d.read(file_name)
        self.assertEqual('+1\n-2\n+3\n+1', result)

    def test_calculate(self):
        result = '+1-2+3+1'
        num = self.d.calculate(result)
        self.assertEqual(num, 3)

    def test_repeat(self):

        num = self.d.repeat('+7\n+7\n-2\n-7\n-4')
        self.assertEqual(14, num)

        num = self.d.repeat('+3\n+3\n+4\n-2\n-4')
        self.assertEqual(10, num)

    def test_day_1(self):
        values = self.d.read('tests/data/day1_all_data.txt')
        result = self.d.calculate(values.replace('\n', ''))
        self.assertEqual(result, 497)

    def test_day_1_task_2(self):
        values = self.d.read('tests/data/day1_all_data.txt')
        num = self.d.repeat(values)
        self.assertEqual(num, 558)


if __name__ == '__main__':
    unittest.main()
