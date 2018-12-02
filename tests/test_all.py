import unittest
from parameterized import parameterized
import days


# Not certain if I wish to parameterize all the tests...


class AddTestCase(unittest.TestCase):
    @parameterized.expand([
        ("day_2", 6888, 'icxjvbrobtunlelzpdmfksahgs'),
        ("day_1", 497, 558),
    ])
    def test_days(self, name, expected_task_1, expected_task_2):
        with open('tests/data/%s.txt' % name, newline='') as f:
            data = f.read()

        result_task_1 = getattr(days, name).solve_task_1(data)
        self.assertEqual(result_task_1, expected_task_1)

        result_task_2 = getattr(days, name).solve_task_2(data)
        self.assertEqual(result_task_2, expected_task_2)
