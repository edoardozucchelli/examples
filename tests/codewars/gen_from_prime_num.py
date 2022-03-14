from unittest import TestCase

from codewars.gen_from_prime_num import count_find_num


class TestGenFromPrimeNum(TestCase):

    def test_gen_from_prime_num(self):

        prime_nums = [2, 5, 7]
        limit = 500
        self.assertEqual(count_find_num(prime_nums, limit), [5, 490])

        prime_nums = [2, 3]
        limit = 200
        self.assertEqual(count_find_num(prime_nums, limit), [13, 192])

        prime_nums = [2, 5]
        limit = 200
        self.assertEqual(count_find_num(prime_nums, limit), [8, 200])

        prime_nums = [2, 3, 5]
        limit = 500
        self.assertEqual(count_find_num(prime_nums, limit), [12, 480])

        prime_nums = [3, 5, 7]
        limit = 500
        self.assertEqual(count_find_num(prime_nums, limit), [2, 315])

        prime_nums = [2, 3, 5]
        limit = 1000
        self.assertEqual(count_find_num(prime_nums, limit), [19, 960])

        prime_nums = [2, 3, 47]
        limit = 200
        self.assertEqual(count_find_num(prime_nums, limit), [])

        prime_nums = [2, 3, 47]
        limit = 282
        self.assertEqual(count_find_num(prime_nums, limit), [1, 282])
