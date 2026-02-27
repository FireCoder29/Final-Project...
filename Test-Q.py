import unittest
from Quiz import (
    total_score,
    average_score,
    highest_score,
    lowest_score,
    score_
)


class TestQuizScorer(unittest.TestCase):

    def setUp(self):
        self.scores = [80, 90, 70, 60]

    def test_calculate_total(self):
        self.assertEqual(total_score(self.scores), 300)

    def test_calculate_average(self):
        self.assertEqual(average_score(self.scores), 75)

    def test_find_highest(self):
        self.assertEqual(highest_score(self.scores), 90)

    def test_find_lowest(self):
        self.assertEqual(lowest_score(self.scores), 60)

    def test_get_summary(self):
        summary = score_(self.scores)
        self.assertEqual(summary["total"], 300)
        self.assertEqual(summary["average"], 75)
        self.assertEqual(summary["highest"], 90)
        self.assertEqual(summary["lowest"], 60)


if __name__ == "__main__":
    unittest.main()