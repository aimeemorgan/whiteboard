import ex01
import unittest


class TestFindSingle(unittest.TestCase):

    def setUp(self):
        self.array = [12, 3, 3, 1, 2, 12, 3, 12, 1, 1]
        self.array_single_at_head = [1, 12, 3, 3, 2, 12, 3, 12, 2, 2]
        self.array_single_at_end = [12, 3, 3, 1, 2, 3, 2, 1, 1, 2]
        self.array_missing_single = [12, 3, 3, 1, 12, 3, 12, 1, 1]

    def test_sort_solution(self):
        self.assertEqual(ex01.find_single(self.array), 2)
        self.assertEqual(ex01.find_single(self.array_single_at_head), 1)
        self.assertEqual(ex01.find_single(self.array_single_at_end), 12)
        self.assertEqual(ex01.find_single(self.array_missing_single), "Error -- input does not meet stated conditions.")

    def test_sort_solution_dictionary(self):
        self.assertEqual(ex01.find_single_dict(self.array), 2)
        self.assertEqual(ex01.find_single_dict(self.array_single_at_head), 1)
        self.assertEqual(ex01.find_single_dict(self.array_single_at_end), 12)
        self.assertEqual(ex01.find_single_dict(self.array_missing_single), "Error -- input does not meet stated conditions.")

if __name__ == '__main__':
    unittest.main()
