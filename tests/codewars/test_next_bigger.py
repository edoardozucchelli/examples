from unittest import TestCase

from codewars.next_bigger import next_bigger


class TestNextBigger(TestCase):

    def test_next_bigger(self):
        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)
        self.assertEqual(next_bigger(9), -1)
        self.assertEqual(next_bigger(111), -1)
        self.assertEqual(next_bigger(36941), 39146)
        self.assertEqual(next_bigger(7716941), 7719146)
        self.assertEqual(next_bigger(7194), 7419)
